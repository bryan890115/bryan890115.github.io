# Issue #14 Study Notes Navigation Maintenance Plan

State: COMPLETE  
Specification state: APPROVED  
Final project verdict: PASS  
Repository: `bryan890115/bryan890115.github.io`  
Issue: `#14`  
Default branch: `main`  
Planning branch: `agent/issue-14-study-notes-navigation-plan`  
Implementation branch: `agent/issue-14-study-notes-navigation`  
Base SHA: `7149c5b3305ffb2fe5bfcbc0a1cb3f05105331fc`  
Approval date: 2026-08-04  
Completion date: 2026-08-04

## Strategy

One bounded maintenance milestone was completed: repair the shared Study Notes navigation destination, add a direct recurrence guard, verify both course collections and every established route, then stop.

## M-001 — Repair Study Notes discoverability

State: ACCEPTED  
Accepted review: R-0001 at PR #16 head `4d48092ae7535cde542e4c5c4374194869b40daf`  
Directive: D-0001  
Covers: AC-001 through AC-007

### Completed scope

- Changed `_includes/header.html` so **Study notes** targets `{{ '/pages/study-notes.html' | relative_url }}`.
- Preserved the `page.nav_key == 'resources'` active-state condition.
- Preserved `/study-notes/` as the ACTL3162 landing page, representative ACTL3162 deep routes, `/study-notes/comp6713/`, and all nine COMP6713 module routes.
- Added `tests/test_study_notes_navigation.py`, which requires the selector destination, rejects the ACTL3162-only landing page as the primary destination, and verifies both course-selector links.
- Changed no note content, CSS, JavaScript, metadata, routes, dependencies, workflow permissions, deployment settings, Pages, DNS, or custom-domain configuration.
- Verified desktop and compact navigation at 360 px and 1440 px, including visible focus, compact Menu open/Escape close/focus restoration, selector links, active state, route resolution, responsive containment, and zero console warnings/errors.

### Accepted validation

- Starting SHA: `8c079bce2225b95db77101f2b165ba4c17f2d052`.
- Implementation commit: `5d9c642bdbc5a32d643cbefbd3383ce7a54ad85f`.
- Reviewed implementation head: `4d48092ae7535cde542e4c5c4374194869b40daf`.
- Jekyll build: 25 HTML pages.
- Generated-site checker: 25 pages, 428 references, zero exemptions.
- COMP6713 checker: nine modules and nine executable examples.
- Unit suite: 18 tests passed.
- JavaScript syntax, Python compilation, YAML, source-only `_site`, forbidden-copy, required-route, and diff checks passed.
- Exact-head `Validate site` run `30878891079`, job `91895808077`, passed every step.

## Final state and ownership

All maintenance acceptance criteria and quality gates are satisfied. Issue #14 is resolved from the repository/source perspective.

PR #16 remains on a non-default branch. Bryan owns final merge and post-merge publication verification. Codex and the Project Director must not merge or deploy.

## Preserved risks and boundaries

- `/study-notes/` remains the ACTL3162 canonical route.
- `/pages/study-notes.html` remains the two-course selector.
- The regression test protects the primary destination and both course links.
- The fix remains a navigation correction rather than a redesign or route migration.
- GitHub Pages propagation is separate from source correctness; no Pages or DNS setting changed.

The completed COMP6713 cycle remains archived under `.project-loop/archive/2026-08-04-comp6713-course-notes/`.
