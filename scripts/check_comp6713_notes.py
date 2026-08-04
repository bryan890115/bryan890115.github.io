#!/usr/bin/env python3
"""Validate the public COMP6713 notes and execute marked Python examples."""

from __future__ import annotations

import argparse
import ast
import html
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


TITLE = "COMP6713 Natural Language Processing — Personal Study Notes"
DISCLAIMER = (
    "These are Bryan Jen’s personal study notes for COMP6713 Natural Language "
    "Processing. They are not official UNSW course materials and are not endorsed "
    "by UNSW. Assessment questions, solutions, marking guidance, restricted course "
    "content, and copied teaching materials are intentionally excluded. Any errors "
    "are my own."
)
MODULES = (
    ("foundations-of-nlp.html", "Foundations of NLP"),
    ("representation-learning.html", "Representation Learning"),
    ("attention-and-transformers.html", "Attention and Transformers"),
    ("modern-language-models.html", "Modern Language Models"),
    ("sentiment-analysis.html", "Sentiment Analysis"),
    ("sequence-tagging.html", "Sequence Tagging"),
    ("machine-translation.html", "Machine Translation"),
    (
        "summarisation-and-question-answering.html",
        "Summarisation and Question Answering",
    ),
    (
        "nlp-applications-and-responsible-deployment.html",
        "NLP Applications and Responsible Deployment",
    ),
)

EXECUTABLE_PATTERN = re.compile(
    r"<pre\b(?=[^>]*\bdata-executable=[\"']python[\"'])[^>]*>\s*"
    r"<code\b[^>]*>(.*?)</code>\s*</pre>",
    re.IGNORECASE | re.DOTALL,
)
H1_PATTERN = re.compile(r"<h1\b[^>]*>(.*?)</h1>", re.IGNORECASE | re.DOTALL)
NAV_PATTERN = re.compile(
    r"<nav\b(?=[^>]*\bclass=[\"'][^\"']*\bnote-nav\b[^\"']*[\"'])[^>]*>"
    r"(.*?)</nav>",
    re.IGNORECASE | re.DOTALL,
)
MODULE_LIST_PATTERN = re.compile(
    r"<ol\b(?=[^>]*\bclass=[\"'][^\"']*\bmodule-list\b[^\"']*[\"'])[^>]*>"
    r"(.*?)</ol>",
    re.IGNORECASE | re.DOTALL,
)
HREF_PATTERN = re.compile(r"<a\b[^>]*\bhref=[\"']([^\"']+)[\"']", re.IGNORECASE)
TAG_PATTERN = re.compile(r"<[^>]+>")
FORBIDDEN_PATTERNS = (
    ("private storage reference", re.compile(r"onedrive|sharepoint", re.IGNORECASE)),
    ("local URL", re.compile(r"(?:file|obsidian)://|https?://(?:localhost|127\.0\.0\.1)", re.IGNORECASE)),
    ("local filesystem path", re.compile(r"/Users/|[A-Za-z]:\\")),
    ("vault embed or wiki link", re.compile(r"!\[\[|\[\[[^\]]+\]\]")),
    ("external URL", re.compile(r"https?://", re.IGNORECASE)),
    (
        "non-relative link",
        re.compile(
            r"\b(?:href|action)=[\"'](?:[a-z][a-z0-9+.-]*:|//|/)",
            re.IGNORECASE,
        ),
    ),
    ("image element", re.compile(r"<img\b", re.IGNORECASE)),
    ("embedded media", re.compile(r"<(?:iframe|video|audio|object|embed)\b", re.IGNORECASE)),
    ("page-level script or stylesheet", re.compile(r"<(?:script|link)\b", re.IGNORECASE)),
    (
        "raw document, data, or notebook",
        re.compile(
            r"\.(?:csv|docx?|ipynb|json|md|pdf|pptx?|py|tex|txt|xlsx?|zip)"
            r"(?:[\"'#?]|$)",
            re.IGNORECASE,
        ),
    ),
    ("external source attribute", re.compile(r"\b(?:src|srcset)=[\"']", re.IGNORECASE)),
)
BLOCKED_IMPORTS = {
    "asyncio",
    "ftplib",
    "http",
    "multiprocessing",
    "os",
    "pathlib",
    "pickle",
    "shutil",
    "socket",
    "subprocess",
    "tempfile",
    "urllib",
}
BLOCKED_CALLS = {"__import__", "compile", "eval", "exec", "input", "open"}


@dataclass(frozen=True, order=True)
class Finding:
    path: str
    line: int
    message: str

    def render(self) -> str:
        return f"{self.path}:{self.line}: {self.message}"


@dataclass(frozen=True)
class CheckReport:
    findings: tuple[Finding, ...]
    module_count: int
    executable_count: int
    executable_modules: int

    @property
    def ok(self) -> bool:
        return not self.findings


def _normalise_text(value: str) -> str:
    return " ".join(html.unescape(TAG_PATTERN.sub(" ", value)).split())


def _line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _read(path: Path, relative: str, findings: list[Finding]) -> str | None:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        findings.append(Finding(relative, 1, f"cannot read UTF-8 source: {error}"))
        return None


def _find_h1s(source: str) -> list[str]:
    return [_normalise_text(match.group(1)) for match in H1_PATTERN.finditer(source)]


def _find_note_nav(source: str) -> tuple[list[str], int]:
    match = NAV_PATTERN.search(source)
    if not match:
        return [], 1
    return HREF_PATTERN.findall(match.group(1)), _line_number(source, match.start())


def _expected_navigation(index: int) -> list[str]:
    links: list[str] = []
    if index:
        links.append(MODULES[index - 1][0])
    links.append("../index.html")
    if index + 1 < len(MODULES):
        links.append(MODULES[index + 1][0])
    return links


def _validate_imports_and_calls(code: str, source: str, line: int) -> list[Finding]:
    findings: list[Finding] = []
    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        findings.append(Finding(source, line + (error.lineno or 1) - 1, f"invalid Python: {error.msg}"))
        return findings

    stdlib = getattr(sys, "stdlib_module_names", frozenset())
    for node in ast.walk(tree):
        imported: Iterable[str] = ()
        if isinstance(node, ast.Import):
            imported = (alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported = (node.module or "",)
        for name in imported:
            root = name.split(".", 1)[0]
            if not root or root not in stdlib:
                findings.append(Finding(source, line + node.lineno - 1, f"non-standard-library import {name!r}"))
            elif root in BLOCKED_IMPORTS:
                findings.append(Finding(source, line + node.lineno - 1, f"file, process, or network-capable import {name!r} is not allowed"))
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in BLOCKED_CALLS:
            findings.append(Finding(source, line + node.lineno - 1, f"unsafe call {node.func.id}() is not allowed"))
    return findings


def _execute_example(code: str, source: str, line: int) -> list[Finding]:
    findings = _validate_imports_and_calls(code, source, line)
    if findings:
        return findings
    outputs: list[str] = []
    with tempfile.TemporaryDirectory(prefix="comp6713-example-") as directory:
        for _ in range(2):
            try:
                result = subprocess.run(
                    [sys.executable, "-I", "-c", code],
                    cwd=directory,
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=3,
                )
            except subprocess.TimeoutExpired:
                return [Finding(source, line, "executable example exceeded the 3 second timeout")]
            if result.returncode:
                detail = (result.stderr or result.stdout).strip().splitlines()
                summary = detail[-1] if detail else f"exit {result.returncode}"
                return [Finding(source, line, f"executable example failed: {summary}")]
            outputs.append(result.stdout)
    if outputs[0] != outputs[1]:
        findings.append(Finding(source, line, "executable example output is not deterministic"))
    return findings


def _scan_forbidden(source: str, relative: str) -> list[Finding]:
    findings: list[Finding] = []
    for label, pattern in FORBIDDEN_PATTERNS:
        for match in pattern.finditer(source):
            findings.append(Finding(relative, _line_number(source, match.start()), f"forbidden {label}"))
    return findings


def check_notes(root: Path) -> CheckReport:
    root = root.resolve()
    findings: list[Finding] = []
    expected_files = {"index.html", *(f"notes/{filename}" for filename, _ in MODULES)}
    actual_files = {
        path.relative_to(root).as_posix()
        for path in root.rglob("*")
        if path.is_file()
    } if root.is_dir() else set()

    for missing in sorted(expected_files - actual_files):
        findings.append(Finding(missing, 1, "required source file is missing"))
    for unexpected in sorted(actual_files - expected_files):
        findings.append(Finding(unexpected, 1, "unapproved file or asset in COMP6713 source"))

    index_path = root / "index.html"
    index_source = _read(index_path, "index.html", findings) if index_path.is_file() else None
    if index_source is not None:
        findings.extend(_scan_forbidden(index_source, "index.html"))
        if _find_h1s(index_source) != [TITLE]:
            findings.append(Finding("index.html", 1, "index must contain exactly the approved H1 title"))
        if DISCLAIMER not in _normalise_text(index_source):
            findings.append(Finding("index.html", 1, "exact approved disclaimer is missing"))
        module_list = MODULE_LIST_PATTERN.search(index_source)
        module_links = HREF_PATTERN.findall(module_list.group(1)) if module_list else []
        expected_links = [f"notes/{filename}" for filename, _ in MODULES]
        if module_links != expected_links:
            findings.append(Finding("index.html", 1, "module links are missing, duplicated, or out of approved order"))
        nav_links, nav_line = _find_note_nav(index_source)
        if nav_links != ["../../pages/study-notes.html", f"notes/{MODULES[0][0]}"]:
            findings.append(Finding("index.html", nav_line, "index navigation is incomplete or not relative"))

    executable_count = 0
    executable_modules = 0
    checked_modules = 0
    for index, (filename, title) in enumerate(MODULES):
        relative = f"notes/{filename}"
        path = root / relative
        if not path.is_file():
            continue
        source = _read(path, relative, findings)
        if source is None:
            continue
        checked_modules += 1
        findings.extend(_scan_forbidden(source, relative))
        if _find_h1s(source) != [title]:
            findings.append(Finding(relative, 1, f"module must contain exactly one H1 named {title!r}"))
        nav_links, nav_line = _find_note_nav(source)
        if nav_links != _expected_navigation(index):
            findings.append(Finding(relative, nav_line, "previous/index/next navigation is incomplete or not relative"))
        blocks = list(EXECUTABLE_PATTERN.finditer(source))
        if blocks:
            executable_modules += 1
        executable_count += len(blocks)
        for block in blocks:
            code = html.unescape(TAG_PATTERN.sub("", block.group(1)))
            line = _line_number(source, block.start())
            findings.extend(_execute_example(code, relative, line))
        unmarked_pre = re.search(r"<pre\b(?![^>]*\bdata-(?:executable|pseudocode)=)[^>]*>", source, re.IGNORECASE)
        if unmarked_pre:
            findings.append(Finding(relative, _line_number(source, unmarked_pre.start()), "code block must be marked executable or pseudocode"))

    if executable_modules < 6:
        findings.append(Finding(".", 1, f"executable examples appear in {executable_modules} modules; at least 6 are required"))

    return CheckReport(tuple(sorted(set(findings))), checked_modules, executable_count, executable_modules)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="COMP6713 source directory")
    args = parser.parse_args(argv)
    report = check_notes(args.root)
    if not report.ok:
        for finding in report.findings:
            print(f"ERROR: {finding.render()}")
        print(f"FAIL: {len(report.findings)} finding(s)")
        return 1
    print(
        "COMP6713 notes check passed: "
        f"{report.module_count} modules, {report.executable_count} executable examples "
        f"across {report.executable_modules} modules"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
