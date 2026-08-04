from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.check_comp6713_notes import DISCLAIMER, MODULES, TITLE, check_notes


class Comp6713NotesCheckerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def write(self, relative: str, content: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def valid_tree(self, executable_modules: int = 6) -> None:
        items = "\n".join(
            f'<li><a href="notes/{filename}">{title}</a></li>'
            for filename, title in MODULES
        )
        self.write(
            "index.html",
            f'''<h1>{TITLE}</h1>
<p>{DISCLAIMER}</p>
<ol class="module-list">{items}</ol>
<nav class="note-nav"><a href="../../pages/study-notes.html">All</a><a href="notes/{MODULES[0][0]}">Start</a></nav>''',
        )
        for index, (filename, title) in enumerate(MODULES):
            links = []
            if index:
                links.append(MODULES[index - 1][0])
            links.append("../index.html")
            if index + 1 < len(MODULES):
                links.append(MODULES[index + 1][0])
            anchors = "".join(f'<a href="{href}">Link</a>' for href in links)
            example = ""
            if index < executable_modules:
                example = '<pre data-executable="python"><code>value = 2 + 2\nassert value == 4\nprint(value)</code></pre>'
            self.write(
                f"notes/{filename}",
                f'<h1>{title}</h1>{example}<nav class="note-nav">{anchors}</nav>',
            )

    def messages(self) -> list[str]:
        return [finding.render() for finding in check_notes(self.root).findings]

    def test_valid_exact_tree_and_examples_pass(self) -> None:
        self.valid_tree()

        report = check_notes(self.root)

        self.assertTrue(report.ok, self.messages())
        self.assertEqual(report.module_count, 9)
        self.assertEqual(report.executable_count, 6)

    def test_missing_module_fails(self) -> None:
        self.valid_tree()
        (self.root / "notes" / MODULES[4][0]).unlink()

        self.assertTrue(any("required source file is missing" in item for item in self.messages()))

    def test_private_and_local_syntax_fails(self) -> None:
        self.valid_tree()
        target = self.root / "notes" / MODULES[0][0]
        target.write_text(target.read_text() + "\n<p>Open obsidian://vault from /Users/name.</p>", encoding="utf-8")

        messages = self.messages()
        self.assertTrue(any("local URL" in item for item in messages))
        self.assertTrue(any("local filesystem path" in item for item in messages))

    def test_external_link_and_asset_fail(self) -> None:
        self.valid_tree()
        target = self.root / "notes" / MODULES[1][0]
        target.write_text(
            target.read_text()
            + '\n<a href="https://example.test">External</a>'
            + '<a href="mailto:person@example.test">Email</a>'
            + '<img src="figure.png" alt="">',
            encoding="utf-8",
        )

        messages = self.messages()
        self.assertTrue(any("external URL" in item for item in messages))
        self.assertTrue(any("non-relative link" in item for item in messages))
        self.assertTrue(any("image element" in item for item in messages))
        self.assertTrue(any("external source attribute" in item for item in messages))

    def test_broken_navigation_fails(self) -> None:
        self.valid_tree()
        target = self.root / "notes" / MODULES[2][0]
        target.write_text(target.read_text().replace("../index.html", "/study-notes/comp6713/"), encoding="utf-8")

        self.assertTrue(any("navigation is incomplete or not relative" in item for item in self.messages()))

    def test_failing_executable_example_fails(self) -> None:
        self.valid_tree()
        target = self.root / "notes" / MODULES[0][0]
        target.write_text(target.read_text().replace("assert value == 4", "assert value == 5"), encoding="utf-8")

        self.assertTrue(any("executable example failed" in item for item in self.messages()))

    def test_pseudocode_is_not_counted_as_executable(self) -> None:
        self.valid_tree(executable_modules=5)
        target = self.root / "notes" / MODULES[5][0]
        target.write_text(
            target.read_text().replace(
                f"<h1>{MODULES[5][1]}</h1>",
                f'<h1>{MODULES[5][1]}</h1><pre data-pseudocode="true"><code>RETURN an idea</code></pre>',
            ),
            encoding="utf-8",
        )

        report = check_notes(self.root)
        self.assertEqual(report.executable_modules, 5)
        self.assertTrue(any("at least 6 are required" in item.message for item in report.findings))

    def test_unapproved_extra_file_fails(self) -> None:
        self.valid_tree()
        self.write("notes/download.pdf", "not permitted")

        self.assertTrue(any("unapproved file or asset" in item for item in self.messages()))


if __name__ == "__main__":
    unittest.main()
