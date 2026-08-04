# Project Decisions

## DEC-001 — Approve Issue #14 maintenance scope

State: APPROVED  
Date: 2026-08-04  
Decision owner: Bryan Jen

### Context

Issue #14 records a post-merge navigation-discoverability defect: the shared **Study notes** navigation points to `/study-notes/`, the ACTL3162-only landing page, while the existing two-course selector is at `/pages/study-notes.html`.

Bryan reviewed the maintenance specification and plan in PR #15 and explicitly approved them on 2026-08-04.

### Decision

- Fix only the shared navigation target so **Study notes** opens `/pages/study-notes.html`.
- Preserve `page.nav_key == 'resources'` and all existing ACTL3162 and COMP6713 routes.
- Add a focused automated regression guard for the primary navigation destination and both selector links.
- Verify desktop/compact keyboard behaviour and the complete existing validation suite.
- Do not change note content, visual design, route structure, dependencies, deployment settings, Pages, DNS, or custom-domain configuration.
- Deliver the implementation on `agent/issue-14-study-notes-navigation` through a draft pull request linked to Issue #14.
- Codex and the Project Director must not merge or deploy.

### Consequences

- The specification and plan are approved.
- M-001 and D-0001 are active.
- Codex must still wait until PR #15 is merged into canonical `main` before creating the implementation branch or changing source.

### Affected acceptance criteria, milestone, and directive

- Acceptance criteria: AC-001 through AC-007
- Active milestone: M-001
- Active directive: D-0001

The completed COMP6713 course-notes publication decisions are preserved under:

`.project-loop/archive/2026-08-04-comp6713-course-notes/DECISIONS.md`
