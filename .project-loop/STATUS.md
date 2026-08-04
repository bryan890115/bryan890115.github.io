# Codex Implementation Status

Protocol version: 1
Directive ID: D-0001
Milestone ID: M-001
State: READY_FOR_REVIEW
Branch: `agent/issue-14-study-notes-navigation`
Starting SHA: `8c079bce2225b95db77101f2b165ba4c17f2d052`
Implementation commit SHA: `5d9c642bdbc5a32d643cbefbd3383ce7a54ad85f`
Updated at: `2026-08-04T04:48:57Z`

## Implemented work

- Changed the shared primary **Study notes** link in `_includes/header.html` from
  `/study-notes/` to `/pages/study-notes.html`.
- Preserved the existing `page.nav_key == 'resources'` active-state condition.
- Added one focused regression test that identifies the primary link, requires the
  selector destination, rejects the ACTL3162 landing page as the primary destination,
  and requires both ACTL3162 and COMP6713 links on the selector.

## Files changed

- `_includes/header.html`
- `tests/test_study_notes_navigation.py`
- `.project-loop/STATUS.md`

No note content, CSS, JavaScript, metadata, routes, dependencies, workflows,
deployment configuration, Pages, DNS, or custom-domain configuration changed.

## Authority evidence

- Current remote `main` and the implementation starting SHA were
  `8c079bce2225b95db77101f2b165ba4c17f2d052`, the merge of planning PR #15.
- D-0001 base `7149c5b3305ffb2fe5bfcbc0a1cb3f05105331fc` is an ancestor of the starting SHA.
- Every file changed between the directive base and starting SHA is under
  `.project-loop/` and belongs to the Director archive or approved Issue #14 handoff.
- The implementation branch was created directly from current `origin/main`; an
  unrelated local edit in the older `main` worktree was left untouched.

## Acceptance evidence

- **AC-001:** Source and rendered desktop/compact primary navigation target
  `/pages/study-notes.html`.
- **AC-002:** The rendered selector links to `/study-notes/` and
  `/study-notes/comp6713/`; both links resolve successfully.
- **AC-003:** `/study-notes/`, representative ACTL3162 routes including modules 0
  and 5, the COMP6713 index, and all nine COMP6713 module routes build non-empty.
- **AC-004:** The unchanged `resources` condition renders
  `aria-current="page"` on the selector, ACTL3162 landing page, and COMP6713 landing
  page at both 360 px and 1440 px. Focus, compact Menu open, Escape close, and focus
  restoration passed.
- **AC-005:** `test_primary_navigation_uses_selector_with_both_course_links` passes
  and directly guards the primary destination and both selector targets.
- **AC-006:** Complete local validation passed; exact-head pull-request CI is
  recorded in the draft PR and ready notification after the status-bearing commit
  is pushed.
- **AC-007:** Delivery is limited to the requested non-default branch and a draft PR
  linked to Issue #14. No merge or deployment was performed.

## Browser evidence

- At 360 px and 1440 px, the selector, ACTL3162 landing page, and COMP6713 landing
  page all rendered the primary **Study notes** link with the selector destination
  and the correct `aria-current` state: 6/6 route-width checks passed.
- At 360 px, the Menu control showed a visible 3 px focus outline, opened the primary
  navigation, closed on Escape, and restored focus to `#nav-toggle`.
- At 360 px and 1440 px, both course-selector cards showed visible 3 px focus
  outlines and resolved to their preserved collection routes: 4/4 checks passed.
- At 1440 px, the visible desktop **Study notes** link showed a 3 px focus outline
  and resolved to `/pages/study-notes.html`.
- The tested pages had no horizontal overflow. Fresh console checks at both widths
  reported zero warnings and zero errors.

## Validation

- `git merge-base --is-ancestor 7149c5b3305ffb2fe5bfcbc0a1cb3f05105331fc 8c079bce2225b95db77101f2b165ba4c17f2d052` — exit 0.
- Director-handoff changed-file inventory — all entries under `.project-loop/`.
- Jekyll build — exit 0; 25 HTML pages generated.
- `python3 scripts/check_site.py _site` — exit 0; 25 HTML files, 428 references,
  zero exemptions.
- `python3 scripts/check_comp6713_notes.py study-notes/comp6713` — exit 0; 9
  modules and 9 executable examples across 9 modules.
- `python3 -m unittest discover -s tests -v` — exit 0; 18 tests passed.
- Focused navigation regression test — exit 0; 1 test passed.
- JavaScript syntax, Python compilation, YAML configuration, source-only `_site`,
  zero-exemption, forbidden-copy, required-route, and `git diff --check` checks —
  exit 0.
- The default system Bundler entrypoint could not load pinned Bundler 2.5.23. As
  permitted by repository guidance, the build used the supported Homebrew
  Ruby/Bundler 2.5.23 launcher with an existing local dependency bundle whose
  `Gemfile.lock` hash exactly matches this worktree. No dependency changed.

## Pull request and exact-head evidence

- The final status-bearing head and exact `Validate site` workflow run/job IDs are
  recorded in the draft PR and `CODEX_READY` notification after this status commit
  is pushed. A commit cannot include its own SHA or future workflow identity without
  changing that identity.

## Deviations, risks, and blockers

- Deviations: supported Homebrew Ruby/Bundler launcher used as documented above.
- Known risks: none within the bounded maintenance scope.
- Blockers: none.

## Review focus

- The one-line shared-header target change and preservation of the `resources`
  active-state condition.
- The regression test's direct coverage of the selector destination and both course
  links.
- Exact-head CI and confirmation that the diff contains no unrelated public or
  operational changes.
