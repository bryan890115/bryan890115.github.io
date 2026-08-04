# Current Codex Directive

Directive ID: D-0001  
Status: ACTIVE  
Milestone ID: M-001  
Repository: `bryan890115/bryan890115.github.io`  
Issue: `#14`  
Intended implementation branch: `agent/issue-14-study-notes-navigation`  
Base SHA: `7149c5b3305ffb2fe5bfcbc0a1cb3f05105331fc`  
Issued timestamp: `2026-08-04T14:20:00+10:00`  
Activated timestamp: `2026-08-04T14:37:00+10:00`  
Replaced directive ID: None

## Approval

Bryan explicitly approved the Issue #14 maintenance specification and plan on 2026-08-04. D-0001 is active.

Codex must still wait until planning PR #15 is merged into canonical `main` before creating the implementation branch or changing source.

## Required outcome

Fix Issue #14 by making the shared desktop and compact **Study notes** navigation open `/pages/study-notes.html`, the existing two-course selector, while preserving `/study-notes/` as the ACTL3162 landing page and preserving every COMP6713 route.

## Required implementation

1. After PR #15 is merged, create `agent/issue-14-study-notes-navigation` from the then-current `main` and record the exact starting SHA in `.project-loop/STATUS.md`.
2. Verify the directive base is an ancestor of the starting SHA and that intervening changes are limited to the Director-owned `.project-loop/` archive and maintenance handoff.
3. In `_includes/header.html`, change only the Study Notes link target from `{{ '/study-notes/' | relative_url }}` to `{{ '/pages/study-notes.html' | relative_url }}`.
4. Keep the `page.nav_key == 'resources'` active-state condition unchanged.
5. Add or update one focused automated regression check that:
   - identifies the primary Study Notes navigation link;
   - requires `/pages/study-notes.html` as its destination;
   - rejects `/study-notes/` as the primary-navigation destination; and
   - confirms `/pages/study-notes.html` links to both `/study-notes/` and `/study-notes/comp6713/`.
6. Make no change to ACTL3162 or COMP6713 note source, wording, examples, routes, metadata, or styling.
7. Build and validate the complete site.
8. Verify the desktop and compact navigation at 360 px and 1440 px, including keyboard focus, compact Menu open, Escape close, focus restoration, and `aria-current` behaviour.
9. Update `.project-loop/STATUS.md` with exact SHAs, changed files, test evidence, rendered-link evidence, route preservation, browser results, deviations, risks, and blockers.
10. Open a draft implementation PR targeting `main`, link it to Issue #14, and post `CODEX_READY D-0001 at <FULL_SHA>` only after local checks and exact-head PR CI pass.

## Expected changed-file boundary

- `_includes/header.html`
- one focused file under `tests/` or a narrowly scoped checker/test file
- `.project-loop/STATUS.md`

Documentation may change only if it currently states the wrong navigation destination. CSS, JavaScript, page content, note source, route structure, dependencies, workflow permissions, deployment automation, Pages settings, DNS, and custom-domain configuration are out of scope.

## Required validation

- Jekyll build succeeds.
- `scripts/check_site.py` passes with zero exemptions.
- `scripts/check_comp6713_notes.py` passes.
- Full unit tests, JavaScript syntax, Python compilation, and YAML validation pass.
- `_site/` remains untracked.
- The selector, ACTL3162 landing and representative deep routes, COMP6713 index, and all nine COMP6713 modules build non-empty.
- The regression check proves the primary navigation points to the selector and the selector exposes both collections.
- `git diff --check` passes and the working tree is clean.
- Exact-head `Validate site` CI passes.

## Explicitly out of scope

- Redirecting or replacing `/study-notes/`.
- Rewriting or redesigning study notes.
- Adding, removing, renaming, or reordering courses or modules.
- Changing accepted public content, CSS, JavaScript, metadata, dependencies, workflows beyond a strictly necessary validation assertion, or deployment settings.
- Merging, deploying, marking a PR ready, pushing directly to `main`, or changing repository settings.

## Stop and escalate conditions

Stop and report `BLOCKED` if:

- the implementation starting head contains unexpected production changes after the base SHA;
- the selector does not already contain both course links;
- the fix requires changing a canonical route, note content, styling, JavaScript, dependency, or deployment setting;
- the `resources` active state cannot be preserved generically;
- any existing ACTL3162 or COMP6713 route breaks;
- exact-head CI fails and cannot be fixed within the narrow navigation/test scope.

## Publication permission

After PR #15 is merged into `main`, Codex may implement this bounded fix on `agent/issue-14-study-notes-navigation`, open a draft PR, and request review.

Codex must not merge, deploy, mark the implementation PR ready, push directly to `main`, or change repository settings.
