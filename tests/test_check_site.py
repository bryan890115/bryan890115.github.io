from __future__ import annotations

import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from scripts.check_site import CheckConfig, Exemption, check_site, load_config, main


class SiteCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        self.config = CheckConfig(("Placeholder",), ())

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative_path: str, content: str) -> None:
        path = self.root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def messages(self, report) -> list[str]:
        return [finding.render() for finding in report.findings]

    def test_valid_routes_assets_fragments_and_external_urls(self) -> None:
        self.write("CNAME", "example.test\n")
        self.write("assets/site.css", "body {}")
        self.write(
            "index.html",
            """<!doctype html>
<a href="/docs/?from=home#intro">Docs</a>
<a href="https://example.test/about.html#bio">About</a>
<a href="https://other.test/missing.html">External</a>
<a href="mailto:person@example.test">Email</a>
<a href="tel:+61000000000">Phone</a>
<img src="data:image/gif;base64,AA==" alt="">
<link href="assets/site.css" rel="stylesheet">
<div data-href="/about.html"></div>
""",
        )
        self.write("docs/index.html", '<h1 id="intro">Docs</h1>')
        self.write("about.html", '<h1 id="bio">About</h1>')

        report = check_site(self.root, self.config)

        self.assertTrue(report.ok, self.messages(report))
        self.assertEqual(report.html_files, 3)

    def test_missing_case_sensitive_directory_asset_and_data_links_fail(self) -> None:
        self.write(
            "index.html",
            """<a href="About.html">Wrong case</a>
<a href="empty-directory/">No index</a>
<img src="assets/missing.png" alt="">
<div data-href="missing.html"></div>
<a href="../outside.html">Outside</a>
""",
        )
        self.write("about.html", "<p>lowercase target</p>")
        (self.root / "empty-directory").mkdir()

        report = check_site(self.root, self.config)
        messages = self.messages(report)

        self.assertEqual(len(messages), 5)
        self.assertTrue(any("resolved to 'About.html'" in item for item in messages))
        self.assertTrue(any("resolved to 'empty-directory'" in item for item in messages))
        self.assertTrue(any("broken src 'assets/missing.png'" in item for item in messages))
        self.assertTrue(any("broken data-href 'missing.html'" in item for item in messages))
        self.assertTrue(any("path escapes build root" in item for item in messages))
        self.assertEqual([finding.line for finding in report.findings], [1, 2, 3, 4, 5])

    def test_missing_same_origin_absolute_url_is_internal(self) -> None:
        self.write("CNAME", "example.test\n")
        self.write(
            "index.html",
            """<a href="https://example.test/missing.html">Same origin</a>
<a href="https://external.test/missing.html">External</a>
""",
        )

        report = check_site(self.root, self.config)

        self.assertEqual(len(report.findings), 1)
        self.assertIn("https://example.test/missing.html", report.findings[0].message)

    def test_fragments_check_ids_and_legacy_named_anchors(self) -> None:
        self.write(
            "index.html",
            """<main id="main"></main>
<a href="#main">Local</a>
<a href="page.html#legacy">Legacy</a>
<a href="page.html#missing">Missing remote</a>
<a href="#absent">Missing local</a>
""",
        )
        self.write("page.html", '<a name="legacy">Target</a>')

        report = check_site(self.root, self.config)

        self.assertEqual(len(report.findings), 2)
        self.assertEqual([finding.line for finding in report.findings], [4, 5])
        self.assertTrue(all("missing fragment" in item for item in self.messages(report)))

    def test_empty_html_and_no_html_are_errors(self) -> None:
        self.write("empty.html", " \n\t")
        report = check_site(self.root, self.config)
        self.assertEqual(len(report.findings), 1)
        self.assertIn("HTML file is empty", report.findings[0].message)

        (self.root / "empty.html").unlink()
        self.write("asset.txt", "not HTML")
        report = check_site(self.root, self.config)
        self.assertEqual(len(report.findings), 1)
        self.assertIn("no HTML files found", report.findings[0].message)

    def test_forbidden_phrases_are_case_insensitive_and_exemptions_are_exact(self) -> None:
        config = CheckConfig(
            ("Placeholder", "© 2024"),
            (
                Exemption(
                    "pages/projects.html",
                    frozenset({"Placeholder"}),
                    "deferred project copy",
                ),
            ),
        )
        self.write(
            "pages/projects.html",
            "<p>PLACEHOLDER project</p>\n<footer>&copy; 2024 Bryan</footer>",
        )
        self.write("pages/about.html", "<p>placeholder biography</p>")

        report = check_site(self.root, config)

        self.assertEqual(len(report.exemptions), 1)
        self.assertEqual(report.exemptions[0].source, "pages/projects.html")
        self.assertEqual(len(report.findings), 2)
        self.assertTrue(any("'© 2024'" in item for item in self.messages(report)))
        self.assertTrue(any("pages/about.html" in item for item in self.messages(report)))

    def test_longest_flexible_whitespace_phrase_wins(self) -> None:
        config = CheckConfig(("Coming Soon", "More details coming soon"), ())
        self.write("index.html", "<p>MORE DETAILS\n   COMING SOON</p>")

        report = check_site(self.root, config)

        self.assertEqual(len(report.findings), 1)
        self.assertIn("'More details coming soon'", report.findings[0].message)

    def test_cli_reports_applied_exemptions_and_returns_success(self) -> None:
        self.write("index.html", "<p>Placeholder</p>")
        config_path = self.root / "config.json"
        config_path.write_text(
            json.dumps(
                {
                    "version": 1,
                    "forbidden_phrases": ["Placeholder"],
                    "exemptions": [
                        {
                            "path": "index.html",
                            "phrases": ["Placeholder"],
                            "reason": "test-only deferred copy",
                        }
                    ],
                }
            ),
            encoding="utf-8",
        )
        output = io.StringIO()

        with redirect_stdout(output):
            exit_code = main([str(self.root), "--config", str(config_path)])

        self.assertEqual(exit_code, 0)
        self.assertIn("EXEMPT: index.html:1", output.getvalue())
        self.assertIn("1 exemption(s) applied", output.getvalue())

    def test_repository_config_has_only_narrow_deferred_path_exemptions(self) -> None:
        config_path = Path(__file__).resolve().parents[1] / "site-check.json"
        config = load_config(config_path)

        self.assertEqual(len(config.exemptions), 1)
        self.assertEqual(config.exemptions[0].path, "pages/contact.html")
        self.assertEqual(
            config.exemptions[0].phrases,
            frozenset(
                {
                    "Typically within 24-48 hours",
                    "Available for consulting opportunities",
                    "Available for consulting engagements",
                    "consulting services",
                    "Open to professional inquiries and collaboration discussions",
                }
            ),
        )
        self.assertTrue(config.phrases)


if __name__ == "__main__":
    unittest.main()
