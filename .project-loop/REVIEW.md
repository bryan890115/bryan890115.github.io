# Project Reviews

## R-0001 — Issue #14 Study Notes navigation maintenance

Timestamp: `2026-08-04T14:54:00+10:00`  
Directive ID: D-0001  
Milestone ID: M-001  
Pull request: `#16` (`agent/issue-14-study-notes-navigation`)  
Starting SHA: `8c079bce2225b95db77101f2b165ba4c17f2d052`  
Implementation commit SHA: `5d9c642bdbc5a32d643cbefbd3383ce7a54ad85f`  
Exact reviewed head SHA: `4d48092ae7535cde542e4c5c4374194869b40daf`  
Exact-head workflow run: `30878891079`  
Exact-head workflow job: `91895808077`  
Verdict: PASS

### Evidence inspected

- PR #16 metadata, exact head, open/draft/mergeable state, Issue #14 linkage, and `CODEX_READY D-0001` notification.
- Complete three-file changed inventory and exact patches for `_includes/header.html`, `tests/test_study_notes_navigation.py`, and `.project-loop/STATUS.md`.
- The one-line primary-navigation correction and preservation of the existing `resources` active-state condition.
- The focused regression test requiring `/pages/study-notes.html`, rejecting `/study-notes/` as the primary destination, and requiring both ACTL3162 and COMP6713 selector links.
- Codex's recorded 360 px and 1440 px keyboard, focus, compact-menu, active-state, route, responsive, and browser-console results.
- Exact-head `Validate site` run `30878891079`; job `91895808077` passed every checkout, Ruby setup, Jekyll build, generated-site checker, COMP6713 checker, eighteen-test, JavaScript, Python, YAML, source-only `_site`, zero-exemption, forbidden-copy, and required-route step.

### Acceptance results

- **AC-001 — PASS:** The shared desktop and compact **Study notes** link now targets `/pages/study-notes.html`.
- **AC-002 — PASS:** The selector retains semantic links to `/study-notes/` and `/study-notes/comp6713/`.
- **AC-003 — PASS:** The ACTL3162 landing/deep routes, COMP6713 index, and all nine COMP6713 module routes remain unchanged and validated.
- **AC-004 — PASS:** `page.nav_key == 'resources'` is unchanged. Recorded browser QA passed visible focus, keyboard navigation, compact Menu open/Escape close/focus restoration, and `aria-current` behaviour.
- **AC-005 — PASS:** The new focused regression test directly prevents recurrence of the incorrect primary destination and verifies both course links.
- **AC-006 — PASS:** The complete local suite and exact-head PR workflow passed with eighteen tests, zero checker exemptions, and no tracked `_site` output.
- **AC-007 — PASS:** Work is limited to the approved implementation branch and draft PR. Codex and the Project Director did not merge, deploy, push directly to `main`, or change repository settings.

### Findings

No critical or important defect remains. The implementation is the smallest generic fix: one shared-header target change, one focused regression test, and a public-safe Codex status update. No note content, route, styling, JavaScript, metadata, dependency, workflow permission, deployment, Pages, DNS, or custom-domain setting changed.

The browser interaction evidence is recorded by Codex rather than independently rerun through the GitHub connector. The source change, regression coverage, route-preservation checks, exact changed-file boundary, and exact-head CI were independently verified from GitHub.

### Final assessment

Issue #14 is resolved from the repository and source perspective at exact reviewed head `4d48092ae7535cde542e4c5c4374194869b40daf`.

### Single next action

Bryan may merge PR #16. Its `Closes #14` linkage will close the issue when merged. The Project Director and Codex must not merge or deploy.

The completed COMP6713 course-notes publication review history is preserved under:

`.project-loop/archive/2026-08-04-comp6713-course-notes/REVIEW.md`
