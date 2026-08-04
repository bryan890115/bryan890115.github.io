#!/usr/bin/env python3
"""Validate links and forbidden placeholder text in a built static site."""

from __future__ import annotations

import argparse
import html
import json
import posixpath
import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, Sequence
from urllib.parse import unquote, urlsplit


LINK_ATTRIBUTES = frozenset({"href", "src", "data-href"})
HTTP_SCHEMES = frozenset({"http", "https"})


class ConfigurationError(ValueError):
    """Raised when site-check.json is missing or invalid."""


@dataclass(frozen=True)
class Exemption:
    path: str
    phrases: frozenset[str]
    reason: str


@dataclass(frozen=True)
class CheckConfig:
    phrases: tuple[str, ...]
    exemptions: tuple[Exemption, ...]

    def exemption_for(self, path: str, phrase: str) -> Exemption | None:
        for exemption in self.exemptions:
            if exemption.path == path and phrase in exemption.phrases:
                return exemption
        return None


@dataclass(frozen=True, order=True)
class Finding:
    source: str
    line: int
    category: str
    message: str

    def render(self) -> str:
        return f"{self.source}:{self.line}: {self.category}: {self.message}"


@dataclass(frozen=True, order=True)
class AppliedExemption:
    source: str
    line: int
    phrase: str
    reason: str

    def render(self) -> str:
        return (
            f'{self.source}:{self.line}: forbidden phrase {self.phrase!r} '
            f"({self.reason})"
        )


@dataclass(frozen=True)
class Reference:
    source: str
    line: int
    attribute: str
    value: str


@dataclass(frozen=True)
class CheckReport:
    findings: tuple[Finding, ...]
    exemptions: tuple[AppliedExemption, ...]
    html_files: int
    references: int

    @property
    def ok(self) -> bool:
        return not self.findings


class DocumentParser(HTMLParser):
    """Collect URL-bearing attributes and fragment targets from one document."""

    def __init__(self, source: str) -> None:
        super().__init__(convert_charrefs=True)
        self.source = source
        self.anchors: set[str] = set()
        self.references: list[Reference] = []

    def handle_starttag(
        self, tag: str, attrs: list[tuple[str, str | None]]
    ) -> None:
        line, _ = self.getpos()
        for name, value in attrs:
            normalized_name = name.casefold()
            if value is None:
                continue
            if normalized_name == "id" and value:
                self.anchors.add(value)
            elif tag.casefold() == "a" and normalized_name == "name" and value:
                self.anchors.add(value)
            if normalized_name in LINK_ATTRIBUTES:
                self.references.append(
                    Reference(self.source, line, normalized_name, value.strip())
                )


def _validate_site_path(value: object, label: str) -> str:
    if not isinstance(value, str) or not value:
        raise ConfigurationError(f"{label} must be a non-empty string")
    if "\\" in value or value.startswith("/"):
        raise ConfigurationError(f"{label} must be a relative POSIX path")
    normalized = posixpath.normpath(value)
    if normalized != value or normalized in {".", ".."} or normalized.startswith("../"):
        raise ConfigurationError(f"{label} must be a normalized in-site path")
    return value


def load_config(path: Path) -> CheckConfig:
    """Load and validate a site-check configuration file."""

    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except OSError as error:
        raise ConfigurationError(f"cannot read {path}: {error}") from error
    except json.JSONDecodeError as error:
        raise ConfigurationError(f"invalid JSON in {path}: {error}") from error

    if not isinstance(raw, dict):
        raise ConfigurationError("configuration root must be an object")
    if raw.get("version") != 1:
        raise ConfigurationError("configuration version must be 1")

    raw_phrases = raw.get("forbidden_phrases")
    if not isinstance(raw_phrases, list) or not raw_phrases:
        raise ConfigurationError("forbidden_phrases must be a non-empty array")
    phrases: list[str] = []
    seen_phrases: set[str] = set()
    for index, phrase in enumerate(raw_phrases):
        if not isinstance(phrase, str) or not phrase.strip():
            raise ConfigurationError(
                f"forbidden_phrases[{index}] must be a non-empty string"
            )
        if phrase in seen_phrases:
            raise ConfigurationError(f"duplicate forbidden phrase: {phrase!r}")
        seen_phrases.add(phrase)
        phrases.append(phrase)

    raw_exemptions = raw.get("exemptions", [])
    if not isinstance(raw_exemptions, list):
        raise ConfigurationError("exemptions must be an array")
    exemptions: list[Exemption] = []
    seen_pairs: set[tuple[str, str]] = set()
    for index, item in enumerate(raw_exemptions):
        if not isinstance(item, dict):
            raise ConfigurationError(f"exemptions[{index}] must be an object")
        site_path = _validate_site_path(item.get("path"), f"exemptions[{index}].path")
        reason = item.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise ConfigurationError(
                f"exemptions[{index}].reason must be a non-empty string"
            )
        exempt_phrases = item.get("phrases")
        if not isinstance(exempt_phrases, list) or not exempt_phrases:
            raise ConfigurationError(
                f"exemptions[{index}].phrases must be a non-empty array"
            )
        normalized_phrases: set[str] = set()
        for phrase in exempt_phrases:
            if phrase not in seen_phrases:
                raise ConfigurationError(
                    f"exemption for {site_path} names unknown phrase {phrase!r}"
                )
            pair = (site_path, phrase)
            if pair in seen_pairs:
                raise ConfigurationError(
                    f"duplicate exemption for {site_path}: {phrase!r}"
                )
            seen_pairs.add(pair)
            normalized_phrases.add(phrase)
        exemptions.append(Exemption(site_path, frozenset(normalized_phrases), reason))

    return CheckConfig(tuple(phrases), tuple(exemptions))


def _phrase_pattern(phrase: str) -> re.Pattern[str]:
    pieces = re.split(r"(\s+)", phrase)
    expression = "".join(r"\s+" if piece.isspace() else re.escape(piece) for piece in pieces)
    return re.compile(expression, re.IGNORECASE)


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _phrase_occurrences(
    source: str, text: str, config: CheckConfig
) -> tuple[list[Finding], list[AppliedExemption]]:
    decoded = html.unescape(text)
    candidates: list[tuple[int, int, int, str]] = []
    for phrase_index, phrase in enumerate(config.phrases):
        for match in _phrase_pattern(phrase).finditer(decoded):
            candidates.append((match.start(), match.end(), phrase_index, phrase))

    # Prefer the longest configured phrase when phrases overlap, so a sentence such
    # as "More details coming soon" produces one useful result rather than two.
    candidates.sort(key=lambda item: (item[0], -(item[1] - item[0]), item[2]))
    selected: list[tuple[int, int, int, str]] = []
    for candidate in candidates:
        start, end, _, _ = candidate
        if any(start < other_end and end > other_start for other_start, other_end, _, _ in selected):
            continue
        selected.append(candidate)

    findings: list[Finding] = []
    exemptions: list[AppliedExemption] = []
    for start, _, _, phrase in selected:
        line = _line_number(decoded, start)
        exemption = config.exemption_for(source, phrase)
        if exemption is None:
            findings.append(
                Finding(source, line, "forbidden-text", f"forbidden phrase {phrase!r}")
            )
        else:
            exemptions.append(
                AppliedExemption(source, line, phrase, exemption.reason)
            )
    return findings, exemptions


def _cname_hosts(root: Path, manifest: set[str]) -> set[str]:
    if "CNAME" not in manifest:
        return set()
    try:
        lines = (root / "CNAME").read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return set()
    hosts: set[str] = set()
    for line in lines:
        candidate = line.strip()
        if not candidate:
            continue
        parsed = urlsplit(candidate if "://" in candidate else f"//{candidate}")
        if parsed.hostname:
            hosts.add(parsed.hostname.casefold().rstrip("."))
    return hosts


def _resolve_reference(
    reference: Reference,
    manifest: set[str],
    cname_hosts: set[str],
) -> tuple[str | None, str | None, str | None]:
    """Return (target, fragment, error); target None means an external URL."""

    try:
        parsed = urlsplit(reference.value)
    except ValueError as error:
        return None, None, f"invalid URL {reference.value!r}: {error}"

    scheme = parsed.scheme.casefold()
    if parsed.netloc or scheme in HTTP_SCHEMES:
        hostname = (parsed.hostname or "").casefold().rstrip(".")
        if hostname not in cname_hosts:
            return None, None, None
    elif scheme:
        # mailto, tel, data, and other non-file schemes do not name build files.
        return None, None, None

    try:
        url_path = unquote(parsed.path)
        fragment = unquote(parsed.fragment)
    except UnicodeError as error:
        return None, None, f"invalid URL encoding in {reference.value!r}: {error}"
    if "\x00" in url_path or "\\" in url_path:
        return None, None, f"invalid in-site path {reference.value!r}"

    if not url_path:
        target = reference.source
    elif url_path.startswith("/"):
        target = posixpath.normpath(url_path).lstrip("/")
    else:
        target = posixpath.normpath(
            posixpath.join(posixpath.dirname(reference.source), url_path)
        )

    if target in {"", "."}:
        target = "index.html"
    if target == ".." or target.startswith("../"):
        return None, None, f"path escapes build root: {reference.value!r}"

    if target in manifest:
        return target, fragment, None
    index_target = posixpath.join(target.rstrip("/"), "index.html")
    if index_target in manifest:
        return index_target, fragment, None
    return None, None, (
        f"broken {reference.attribute} {reference.value!r} "
        f"(resolved to {target!r})"
    )


def _iter_files(root: Path) -> Iterable[Path]:
    return (path for path in root.rglob("*") if path.is_file())


def check_site(root: Path, config: CheckConfig) -> CheckReport:
    """Check a built site and return deterministic findings and exemptions."""

    root = root.resolve()
    files = sorted(_iter_files(root), key=lambda path: path.relative_to(root).as_posix())
    manifest = {path.relative_to(root).as_posix() for path in files}
    html_paths = [path for path in files if path.suffix.casefold() == ".html"]
    findings: list[Finding] = []
    applied_exemptions: list[AppliedExemption] = []
    references: list[Reference] = []
    anchors: dict[str, set[str]] = {}

    if not html_paths:
        findings.append(Finding("<site>", 1, "build", "no HTML files found"))

    for path in html_paths:
        source = path.relative_to(root).as_posix()
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as error:
            findings.append(
                Finding(source, 1, "html", f"cannot read HTML as UTF-8: {error}")
            )
            anchors[source] = set()
            continue
        if not text.strip():
            findings.append(Finding(source, 1, "html", "HTML file is empty"))

        parser = DocumentParser(source)
        try:
            parser.feed(text)
            parser.close()
        except Exception as error:  # HTMLParser extensions may raise on malformed input.
            findings.append(Finding(source, 1, "html", f"cannot parse HTML: {error}"))
        anchors[source] = parser.anchors
        references.extend(parser.references)

        phrase_findings, phrase_exemptions = _phrase_occurrences(source, text, config)
        findings.extend(phrase_findings)
        applied_exemptions.extend(phrase_exemptions)

    cname_hosts = _cname_hosts(root, manifest)
    for reference in references:
        target, fragment, error = _resolve_reference(reference, manifest, cname_hosts)
        if error:
            findings.append(
                Finding(reference.source, reference.line, "link", error)
            )
            continue
        if target and fragment and target.endswith(".html"):
            if fragment not in anchors.get(target, set()):
                findings.append(
                    Finding(
                        reference.source,
                        reference.line,
                        "link",
                        f"missing fragment {fragment!r} in {target!r} "
                        f"from {reference.attribute} {reference.value!r}",
                    )
                )

    return CheckReport(
        tuple(sorted(findings)),
        tuple(sorted(applied_exemptions)),
        len(html_paths),
        len(references),
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check built HTML for broken internal links and forbidden text."
    )
    parser.add_argument("site_root", type=Path, help="built site directory")
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "site-check.json",
        help="checker configuration (default: repository site-check.json)",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    if not args.site_root.is_dir():
        print(f"ERROR: site root is not a directory: {args.site_root}", file=sys.stderr)
        return 2
    try:
        config = load_config(args.config)
    except ConfigurationError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2

    report = check_site(args.site_root, config)
    for exemption in report.exemptions:
        print(f"EXEMPT: {exemption.render()}")
    for finding in report.findings:
        print(f"ERROR: {finding.render()}")

    exemption_summary = f"{len(report.exemptions)} exemption(s) applied"
    if report.ok:
        print(
            f"Site check passed: {report.html_files} HTML file(s), "
            f"{report.references} reference(s), {exemption_summary}."
        )
        return 0
    print(
        f"Site check failed: {len(report.findings)} issue(s), "
        f"{report.html_files} HTML file(s), {report.references} reference(s), "
        f"{exemption_summary}."
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
