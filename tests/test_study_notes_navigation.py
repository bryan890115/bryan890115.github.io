from __future__ import annotations

import re
import unittest
from pathlib import Path


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
LIQUID_LINK_PATTERN = re.compile(
    r'href="\{\{\s*\'(?P<path>[^\']+)\'\s*\|\s*relative_url\s*\}\}"'
)


class StudyNotesNavigationTests(unittest.TestCase):
    def test_primary_navigation_uses_selector_with_both_course_links(self) -> None:
        header = (REPOSITORY_ROOT / "_includes/header.html").read_text(
            encoding="utf-8"
        )
        selector = (REPOSITORY_ROOT / "pages/study-notes.html").read_text(
            encoding="utf-8"
        )

        primary_navigation = re.search(
            r'<nav\b[^>]*\bid="primary-navigation"[^>]*>(?P<body>.*?)</nav>',
            header,
            flags=re.DOTALL,
        )
        self.assertIsNotNone(primary_navigation, "primary navigation is missing")

        study_notes_link = re.search(
            r'<a\s+href="\{\{\s*\'(?P<path>[^\']+)\'\s*\|\s*relative_url\s*\}\}"'
            r'(?P<attributes>[^>]*)>Study notes</a>',
            primary_navigation.group("body"),
        )
        self.assertIsNotNone(study_notes_link, "primary Study notes link is missing")
        self.assertEqual(study_notes_link.group("path"), "/pages/study-notes.html")
        self.assertNotEqual(study_notes_link.group("path"), "/study-notes/")
        self.assertIn(
            "{% if page.nav_key == 'resources' %} aria-current=\"page\"{% endif %}",
            study_notes_link.group("attributes"),
        )

        selector_targets = {
            match.group("path") for match in LIQUID_LINK_PATTERN.finditer(selector)
        }
        self.assertTrue(
            {"/study-notes/", "/study-notes/comp6713/"}.issubset(selector_targets),
            "course selector must link to both ACTL3162 and COMP6713",
        )


if __name__ == "__main__":
    unittest.main()
