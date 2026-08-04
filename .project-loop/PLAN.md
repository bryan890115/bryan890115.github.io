# Issue #14 Study Notes Navigation Maintenance Plan

State: APPROVED  
Specification state: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Issue: `#14`  
Default branch: `main`  
Planning branch: `agent/issue-14-study-notes-navigation-plan`  
Intended implementation branch: `agent/issue-14-study-notes-navigation`  
Base SHA: `7149c5b3305ffb2fe5bfcbc0a1cb3f05105331fc`  
Draft date: 2026-08-04  
Approval date: 2026-08-04

## Strategy

Use one bounded maintenance milestone. Change the shared Study Notes navigation target, add a regression guard, verify both course collections and all existing routes, then stop. No content, route, design, dependency, or deployment expansion is allowed.

## M-001 — Repair Study Notes discoverability

State: ACTIVE  
Dependencies: Specification and plan approved by Bryan on 2026-08-04; planning PR #15 must be merged into `main` before Codex begins  
Active directive: D-0001  
Covers: AC-001 through AC-007

### Scope

- Create `agent/issue-14-study-notes-navigation` from canonical `main` after planning approval is merged.
- Change `_includes/header.html` so **Study notes** targets `{{ '/pages/study-notes.html' | relative_url }}`.
- Keep the `resources` active-state condition unchanged.
- Add a focused automated regression check that requires the selector target and confirms the selector links to both `/study-notes/` and `/study-notes/comp6713/`.
- Do not change ACTL3162 or COMP6713 note source, routes, wording, examples, or styling.
- Verify desktop and compact navigation, keyboard focus, Escape/focus restoration, and `aria-current` behaviour.
- Run the full existing build, checker, test, syntax, zero-exemption, route, and source-only `_site` suite.
- Update `.project-loop/STATUS.md`, open a draft PR linked to Issue #14, and post `CODEX_READY D-0001 at <FULL_SHA>` only after local checks and exact-head CI pass.

### Expected implementation files

- `_includes/header.html`
- one focused file under `tests/` or a narrowly scoped existing checker/test file
- `.project-loop/STATUS.md`

Documentation may change only if it incorrectly describes the navigation destination. CSS, JavaScript, note content, routes, metadata, dependencies, workflow permissions, and deployment settings are out of scope.

### Required validation

- D-0001 base is an ancestor of the starting SHA.
- Changes between the base and starting SHA are limited to the Director archive/planning handoff under `.project-loop/`.
- Jekyll build passes.
- Generated-site checker passes with zero exemptions.
- COMP6713 checker passes.
- Full unit suite, JavaScript syntax, Python compilation, and YAML validation pass.
- `_site/` remains untracked.
- Selector, ACTL3162 routes, COMP6713 index, and all nine COMP6713 modules build non-empty.
- `git diff --check` passes and the working tree is clean.

### Browser and interaction evidence

At 360 px and 1440 px verify:

- Study Notes navigation opens `/pages/study-notes.html`.
- The selector offers ACTL3162 and COMP6713.
- The `resources` active state is visible on the selector and both collections.
- Compact Menu opens, closes with Escape, and restores focus.
- Keyboard activation reaches both course collections.
- No browser-console warning or error is introduced.

### Exit evidence

- Exact starting, implementation, and final review SHAs.
- Focused changed-file inventory.
- Source and rendered navigation-target evidence.
- Regression-test evidence.
- Selector and route-preservation evidence.
- Keyboard, active-state, responsive, and console results.
- Successful local validation and exact-head workflow IDs.
- Confirmation that no unrelated content, design, dependency, route, or deployment setting changed.

## Risks

- Preserve `/study-notes/` as the ACTL3162 canonical route.
- Preserve `page.nav_key == 'resources'` across the selector and both collections.
- Prevent recurrence with a direct automated assertion.
- Do not turn the fix into a navigation redesign.
- Treat GitHub Pages propagation separately from source correctness; do not change Pages or DNS settings.

## Ownership

The completed COMP6713 cycle is archived under `.project-loop/archive/2026-08-04-comp6713-course-notes/`. Codex and the Project Director must not merge or deploy. Bryan owns final merge and post-merge verification.
