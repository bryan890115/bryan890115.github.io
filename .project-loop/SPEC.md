# Issue #14 Study Notes Navigation Maintenance Specification

Protocol version: 1  
State: DRAFT  
Repository: `bryan890115/bryan890115.github.io`  
Issue: `#14` — Fix Study Notes navigation to show both course collections  
Default branch: `main`  
Planning branch: `agent/issue-14-study-notes-navigation-plan`  
Intended implementation branch: `agent/issue-14-study-notes-navigation`  
Approval state: PENDING BRYAN REVIEW  
Draft date: 2026-08-04  
Base SHA: `7149c5b3305ffb2fe5bfcbc0a1cb3f05105331fc`

## Problem

The merged site contains both public course collections and a two-course selector at `/pages/study-notes.html`, but the shared primary-navigation **Study notes** link still targets `/study-notes/`. That route is intentionally the ACTL3162 landing page, so visitors do not discover COMP6713 through the primary navigation.

## Goal

Make the shared desktop and compact **Study notes** navigation open `/pages/study-notes.html`, where visitors can choose ACTL3162 or COMP6713, while preserving every existing course-note route and all accepted public content.

## Required outcome

- Change the shared Study Notes navigation target in `_includes/header.html` from `/study-notes/` to `/pages/study-notes.html`.
- Keep `page.nav_key == 'resources'` so the active state remains correct on the selector and both note collections.
- Add a durable regression check that fails if the primary Study Notes navigation points directly to the ACTL3162-only landing page again.
- Verify the selector links to both collections and that all established ACTL3162 and COMP6713 routes remain functional.

## Non-goals

- Rewriting or redesigning either course-note collection.
- Changing `/study-notes/`, `/study-notes/notes/*.html`, `/study-notes/comp6713/`, or any COMP6713 module route.
- Changing note content, examples, mathematics, disclaimers, metadata, visual design, typography, layout, contact details, biography, projects, research content, custom-domain configuration, or deployment settings.
- Introducing redirects, a new landing-page hierarchy, a framework, dependency, backend, CMS, or analytics.
- Merging or deploying by Codex or the Project Director.

## Constraints

- Implement the smallest generic fix in the shared header.
- Preserve the two-course selector at `/pages/study-notes.html`.
- Preserve the canonical ACTL3162 landing page at `/study-notes/`.
- Preserve the COMP6713 landing page at `/study-notes/comp6713/` and all nine module routes.
- Preserve semantic links, keyboard operation, visible focus, compact-menu behaviour, and `aria-current` handling.
- Keep `site-check.json` at zero exemptions and `_site/` untracked.
- Existing validation CI must continue to pass without deployment or write permissions.

## Acceptance criteria

- **AC-001:** The shared desktop and compact **Study notes** navigation resolves to `/pages/study-notes.html`.
- **AC-002:** `/pages/study-notes.html` visibly and semantically links to both `/study-notes/` and `/study-notes/comp6713/`.
- **AC-003:** `/study-notes/`, representative ACTL3162 deep routes, `/study-notes/comp6713/`, and all nine COMP6713 module routes remain unchanged and functional.
- **AC-004:** `page.nav_key == 'resources'`, visible focus, keyboard navigation, compact Menu open/close/Escape/focus restoration, and `aria-current` behaviour remain correct.
- **AC-005:** A focused regression test or checker assertion prevents the primary Study Notes navigation from silently reverting to `/study-notes/`.
- **AC-006:** Jekyll build, generated-site checker, COMP6713 checker, full unit suite, JavaScript syntax, Python compilation, YAML validation, zero-exemption policy, source-only `_site`, required-route checks, and exact-head PR CI all pass.
- **AC-007:** Work is delivered on `agent/issue-14-study-notes-navigation` through a draft pull request linked to Issue #14; Codex and the Project Director do not merge or deploy.

## Final quality gates

1. The implementation diff is limited to the shared header, one focused regression test or checker change, `.project-loop/STATUS.md`, and only strictly necessary documentation.
2. The primary Study Notes link is verified in rendered desktop and compact navigation.
3. The selector exposes both course collections.
4. Existing ACTL3162 and COMP6713 routes pass the full build/check suite.
5. Keyboard and active-navigation behaviour pass at a mobile and desktop width.
6. Exact-head pull-request CI passes.
7. No unrelated public content, styling, route, dependency, or deployment setting changes.
