# COMP6713 Course Notes Publication Plan

State: COMPLETE  
Specification state: APPROVED  
Final project verdict: PASS  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Implementation branch: `agent/comp6713-notes`  
Base SHA: `a19fe81dadcc03e7de85f2268bc0b5666d20d031`  
Approval date: 2026-08-04  
Completion date: 2026-08-04

## Delivery strategy

Three independently reviewed milestones were completed. Private OneDrive eligibility review was separated from public implementation; the approved public edition was independently authored; final route, accessibility, responsive, CI, integrity, factual-content, and visual-presentation gates passed.

## M-001 — Private discovery and publication eligibility

State: ACCEPTED  
Accepted review: R-0001 at PR #13 head `249ab50c7f8d89f397e41f3e80f01bcf8da5ad86`  
Approval decision: DEC-001  
Covers: AC-001, AC-002, AC-003, AC-004

### Completed scope

- Inspected 255 COMP6713-associated files read-only, including 133 Markdown note bodies.
- Classified 0 files as directly publishable, 97 as potentially usable after authorship confirmation and independent rewriting, 53 as official/third-party or permission-sensitive, and 105 as restricted, assessment-related, duplicate, private-metadata, or otherwise excluded.
- Delivered the detailed packet privately to Bryan.
- Bryan confirmed the 97 candidate notes are his own synthesis and approved their use only as private conceptual input for an independently authored public edition.
- Bryan approved all nine modules, exact title, disclaimer, order, routes, original synthetic code examples, and permanent exclusions.
- Changed only `.project-loop/STATUS.md`; no private evidence or public website source entered GitHub.
- Exact-head CI run `30872531021` passed.

## M-002 — Approved COMP6713 clean public edition

State: ACCEPTED  
Accepted review: R-0002 at PR #13 head `3681324c37d2876190c4fcc01cf2564ac422151e`  
Covers: AC-005, AC-006, AC-007, AC-008, AC-009, AC-012

### Completed scope

- Added `/study-notes/comp6713/` with the exact approved title and disclaimer.
- Added all nine approved module routes in the approved order.
- Independently authored conceptual explanations, mathematics, worked examples, and one original deterministic standard-library Python example using tiny synthetic data in every module.
- Updated `/pages/study-notes.html` into an ACTL3162/COMP6713 selector while preserving `/study-notes/` and existing ACTL3162 deep routes.
- Reused the established Jekyll design and added only narrow notes-specific CSS.
- Added `scripts/check_comp6713_notes.py`, eight focused tests, CI coverage, and README maintenance guidance.
- Kept `site-check.json` at zero exemptions and `_site/` untracked.
- Recorded zero unresolved normalized 12-word prose overlaps and passing structure, technical, mathematics, code, attribution, privacy, and assessment-integrity reviews.
- Exact-head workflow run `30874223125` passed every step.

## M-003 — Full QA, evidence, and final approval

State: ACCEPTED  
Accepted review: R-0003 at PR #13 head `436bf94c8257cd3e829bb2d7e77d58d58bae34a4`  
Correction and QA commit: `acb8d211c86f4523a4b094f0b023ed09dfc413ee`  
Final approval decision: DEC-002  
Covers: AC-010, AC-011, AC-013, AC-014 and all final quality gates

### Completed scope

- Corrected the Attention and Transformers wording to explain permutation equivariance and the absence of token-order representation without positional information.
- Added a generic narrow-screen inline-MathJax containment rule after browser QA exposed one overflow.
- Clarified that executable-example isolation is a maintainer policy check, not an adversarial security sandbox.
- Re-ran technical, mathematics, executable-code, structure, source-distance, citation/attribution, privacy, and assessment-integrity checks; all passed for 9/9 modules and unresolved normalized 12-word overlaps remained zero.
- Verified all ten COMP6713 routes at 360 px, 768 px, and 1440 px.
- Completed keyboard/focus, navigation, code/table/math containment, heading/landmark, metadata, favicon, ACTL3162 route, and browser-console QA.
- Added eight immutable screenshots under `docs/review/d0003/`, excluded from the generated site.
- Exact-head `Validate site` run `30875922503`, job `91887243468`, passed every step.
- Bryan explicitly approved final factual content and visual presentation.

## Final state and ownership

All approved milestones, acceptance criteria, and final quality gates are complete. The repository/source project verdict is PASS.

PR #13 remains on a non-default branch. Bryan alone owns final merge and publication. Codex and the Project Director must not merge or deploy.

## Risks and mitigations preserved

- Official, third-party, private, assessment, team-project, exam-preparation, copied-reading, unclear-permission, and raw OneDrive material remains permanently excluded.
- The public edition remains independently authored; private notes are not publishable source text.
- Executable examples remain original, synthetic, deterministic, standard-library-only policy checks with no network, credentials, private files, datasets, models, or saved outputs.
- Existing ACTL3162 routes remain stable.

## Documentation and rollout

README documents the COMP6713 source structure, eligibility boundary, example-testing convention, local validation, and Bryan-owned merge/publication. The implementation remains on `agent/comp6713-notes` until Bryan merges PR #13.
