# Project Decisions

## DEC-001 — Approve private research and project publication set

State: APPROVED  
Date: 2026-08-03  
Decision owner: Bryan Jen

### Context

D-0002 used Bryan-authorized read-only access to private project material to prepare a private candidate packet. The public repository records only that discovery occurred; it does not contain the OneDrive evidence, private paths, raw files, candidate notes, unpublished details, or the private future-upload reminder.

Bryan reviewed the private packet and explicitly approved its research summary, selected general-project candidates, and Codex's conservative publication decisions.

### Decision

- The exact research summary approved in the private D-0002 packet may be implemented on the public research page.
- The project candidates marked selected and publishable in that private packet may be implemented as general-project cards using only the approved public-facing summaries, contribution statements, methods, outcomes or learnings, public links, and assets.
- Codex must retain the conservative exclusions and redactions proposed in the private packet.
- OneDrive evidence, private paths, raw files, private links, candidate notes, rejected candidates, uncertainty notes, and the reminder to upload more projects must remain outside GitHub and outside built website output.
- No public placeholder or future-project card may be added.
- Any ambiguity about which copy, link, result, or asset was approved requires Codex to stop rather than infer or disclose more.

### Consequences

- The M-002 content-approval dependency is satisfied and implementation may proceed through D-0003.
- Public project and research content is limited to the exact conservative publication set Bryan approved privately.
- The repository will contain the final approved public page content, but not its private discovery evidence or internal candidate packet.
- PR #11 remains draft; neither Codex nor the Project Director may merge or deploy.

### Affected acceptance criteria, milestones, and directives

- Acceptance criteria: AC-002, AC-004, AC-005, AC-011, AC-012, AC-014
- Milestone: M-002
- Completed approval gate: D-0002
- Implementation directive: D-0003
