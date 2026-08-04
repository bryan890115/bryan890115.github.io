# Current Codex Directive

Directive ID: D-0001  
Status: ACTIVE  
Milestone ID: M-001  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/comp6713-notes`  
Base SHA: `a19fe81dadcc03e7de85f2268bc0b5666d20d031`  
Issued timestamp: `2026-08-04T11:37:00+10:00`  
Activated timestamp: `2026-08-04T12:03:00+10:00`  
Replaced directive ID: None

## Approval

Bryan explicitly approved the COMP6713 specification and plan on 2026-08-04. D-0001 is active. Codex must still wait until the activation PR containing this handoff is merged into `main`, so that the approved state is canonical.

## Required outcome

Inspect Bryan's accessible COMP6713 note material in OneDrive as private read-only evidence and return a private publication-eligibility packet. Do not publish, copy, transform into public pages, or commit any note content under this directive.

The packet must identify which material is Bryan-authored and suitable for public notes, which material needs redaction or rewriting into Bryan's own words, which material is official or third-party and requires permission, and which material is restricted or assessment-related and must be excluded.

## In-scope work

1. After the activation PR is merged, create or use `agent/comp6713-notes` from the then-current `main` and record the exact pre-work branch head as `Starting SHA` in `.project-loop/STATUS.md`.
2. Verify the directive base is an ancestor of the implementation starting head. If `main` changed materially after approval, stop and request Project Director recovery.
3. Inspect only OneDrive files and folders clearly associated with Bryan's COMP6713 course notes.
4. Inventory the material privately, including file type, broad contents, apparent authorship, presence of code/mathematics/tables/diagrams, and likely module grouping.
5. Classify every candidate file, section, and asset as one of:
   - Bryan-authored and publishable;
   - potentially publishable after redaction or rewriting into Bryan's own words;
   - official/third-party material requiring publication permission; or
   - restricted/assessment material that must be excluded.
6. Treat assignment specifications, assessment questions, marking rubrics, answer keys, solutions, current assessment work, official lecture/tutorial material, copied readings, private course communications, student information, and unclear-ownership content as excluded unless Bryan supplies clear publication authority.
7. Prepare a private approval packet containing:
   - proposed public course title and personal-notes disclaimer;
   - proposed module titles, order, and one-sentence summaries;
   - proposed public route/file structure;
   - proposed treatment of code, mathematics, tables, diagrams, citations, and assets;
   - authorship, copyright, confidentiality, and assessment-risk notes;
   - exact proposed public links/assets or intentional no-link/no-asset treatment;
   - excluded and uncertain material with reasons; and
   - every decision Bryan must make before implementation.
8. Include no raw file content beyond the minimum short identifiers or descriptions needed for Bryan's private review. Do not reproduce long excerpts.
9. Update `.project-loop/STATUS.md` only with a non-sensitive summary: starting SHA, number of files/note bodies inspected, number proposed, number excluded or uncertain, packet-delivery status, validation, deviations, risks, and blockers.
10. Push only the non-sensitive `STATUS.md` update to `agent/comp6713-notes`, open or update a draft implementation PR targeting `main`, and post only `CODEX_APPROVAL_REQUIRED D-0001` after privately delivering the packet.

## Explicitly out of scope

- Changing `study-notes/`, `pages/study-notes.html`, navigation, CSS, layouts, metadata, tests, CI, README, or any public website source.
- Committing candidate titles, module summaries, excerpts, screenshots, diagrams, note content, converted files, or public note structure before Bryan approves them.
- Uploading, copying, or linking raw OneDrive files.
- Exposing OneDrive paths, private sharing URLs, credentials, comments, revision history, metadata, or private notes in GitHub.
- Publishing official course slides, tutorial sheets, handouts, readings, textbook content, assignment specifications, questions, rubrics, answer keys, solutions, current restricted material, private communications, or third-party personal data.
- Guessing authorship, ownership, permission, course title, module names, assessment status, or publication eligibility.
- Using generative rewriting to convert restricted or third-party material into something publishable without clear authority.
- Adding missing educational content or completing incomplete notes.
- Merging, deploying, marking a PR ready, pushing implementation directly to `main`, or changing repository/Pages/DNS settings.

## Mapped acceptance criteria

- AC-001
- AC-002
- AC-003
- AC-004

## Required evidence

- Exact implementation starting and final SHAs.
- Number of OneDrive files or distinct note bodies inspected.
- Number proposed for publication, number requiring redaction/permission, number excluded, and number unresolved.
- Private approval packet delivered directly to Bryan with all required fields.
- Confirmation that no public website source, candidate content, raw file, private path, URL, excerpt, image, restricted material, or unapproved content was committed or posted.
- A concise, public-safe `.project-loop/STATUS.md` update.
- Exact validation outcomes.

## Exact validation commands

Set `STARTING_SHA` to the exact implementation branch head before Codex edits, then run:

```bash
git merge-base --is-ancestor a19fe81dadcc03e7de85f2268bc0b5666d20d031 "$STARTING_SHA"
git diff --name-only a19fe81dadcc03e7de85f2268bc0b5666d20d031..."$STARTING_SHA"
git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

The final diff from `STARTING_SHA` to the review head must contain only `.project-loop/STATUS.md`. If the starting branch includes later Director-owned approval commits, record them separately and verify that no production source changed before discovery began.

## Publication permission

After the activation PR is merged into `main`, Codex may:

- create or use `agent/comp6713-notes` from current `main`;
- inspect accessible OneDrive material read-only;
- commit and push only a non-sensitive `.project-loop/STATUS.md` update;
- open or update a draft pull request; and
- post a generic approval-required notification.

Codex may not commit any public notes or website implementation under D-0001.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- The activation PR has not been merged into `main`.
- OneDrive access is unavailable or the relevant COMP6713 location cannot be identified safely.
- Material ownership, authorship, copyright permission, confidentiality, or assessment status is unclear.
- The source contains current or restricted assessment material that cannot be separated safely.
- A note depends substantially on official slides, copied readings, textbook passages, third-party diagrams, or private communications.
- Private information would need to enter GitHub to continue.
- The implementation starting head contains unexpected code changes after the directive base.
- Completing discovery would require changing public site source or weakening the publication boundary.

## Next Project Director review focus

- Whether the private packet is sufficiently complete for Bryan to approve an exact module set.
- Whether publication candidates are genuinely Bryan-authored rather than lightly copied course material.
- Whether assessment, confidentiality, copyright, ownership, and third-party risks are surfaced conservatively.
- Whether proposed module structure fits the existing site without breaking ACTL3162 routes.
- Whether no private or restricted material entered GitHub.
- Whether the fastest safe next step is public implementation, a bounded redaction pass, or remaining blocked.
