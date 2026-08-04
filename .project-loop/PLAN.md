# COMP6713 Course Notes Publication Plan

State: APPROVED  
Specification state: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Planning branch: `agent/comp6713-notes-plan`  
Implementation branch: `agent/comp6713-notes`  
Base SHA: `a19fe81dadcc03e7de85f2268bc0b5666d20d031`  
Draft date: 2026-08-04  
Approval date: 2026-08-04

## Delivery strategy

Deliver three reviewable milestones. First separate publication eligibility from implementation so private OneDrive material, assessment content, and third-party course material cannot leak into the public repository. Then independently author the exact public edition Bryan approves. Finish with full route, accessibility, responsive, CI, similarity/integrity, and final-content review.

## M-001 — Private discovery and publication eligibility

State: ACCEPTED  
Dependencies: Specification and plan approved by Bryan on 2026-08-04  
Accepted review: R-0001 at PR #13 head `249ab50c7f8d89f397e41f3e80f01bcf8da5ad86`  
Approval decision: DEC-001  
Covers: AC-001, AC-002, AC-003, AC-004

### Completed scope

- Inspected 255 COMP6713-associated files read-only, including 133 Markdown note bodies.
- Classified 0 files as directly publishable, 97 as potentially usable after authorship confirmation and independent rewriting, 53 as official/third-party or permission-sensitive, and 105 as restricted, assessment-related, duplicate, private-metadata, or otherwise excluded.
- Delivered the detailed publication packet privately to Bryan.
- Bryan confirmed authorship of the 97 candidate notes as his own synthesis and approved their use only as private conceptual input for an independently authored public edition.
- Bryan approved all nine proposed modules, the proposed public title and disclaimer, exact module order and routes, text/math-first treatment, newly authored synthetic code examples, and permanent exclusions.
- Changed only `.project-loop/STATUS.md`; no private evidence or public website source entered GitHub.
- Exact-head CI passed through run `30872531021`.

## M-002 — Approved COMP6713 clean public edition

State: ACCEPTED  
Dependencies: M-001 accepted through R-0001; exact publication scope approved through DEC-001  
Accepted review: R-0002 at PR #13 head `3681324c37d2876190c4fcc01cf2564ac422151e`  
Covers: AC-005, AC-006, AC-007, AC-008, AC-009, AC-012

### Completed public structure

Course index:

- `/study-notes/comp6713/`

Approved title:

- `COMP6713 Natural Language Processing — Personal Study Notes`

Approved modules, in order:

1. Foundations of NLP — `/study-notes/comp6713/notes/foundations-of-nlp.html`
2. Representation Learning — `/study-notes/comp6713/notes/representation-learning.html`
3. Attention and Transformers — `/study-notes/comp6713/notes/attention-and-transformers.html`
4. Modern Language Models — `/study-notes/comp6713/notes/modern-language-models.html`
5. Sentiment Analysis — `/study-notes/comp6713/notes/sentiment-analysis.html`
6. Sequence Tagging — `/study-notes/comp6713/notes/sequence-tagging.html`
7. Machine Translation — `/study-notes/comp6713/notes/machine-translation.html`
8. Summarisation and Question Answering — `/study-notes/comp6713/notes/summarisation-and-question-answering.html`
9. NLP Applications and Responsible Deployment — `/study-notes/comp6713/notes/nlp-applications-and-responsible-deployment.html`

Approved disclaimer:

> These are Bryan Jen’s personal study notes for COMP6713 Natural Language Processing. They are not official UNSW course materials and are not endorsed by UNSW. Assessment questions, solutions, marking guidance, restricted course content, and copied teaching materials are intentionally excluded. Any errors are my own.

### Completed scope

- Independently authored the approved index and all nine module pages using the private notes only as a post-draft concept-coverage checklist.
- Added semantic headings, concise explanations, independently re-derived mathematics, and original worked examples.
- Added one newly authored, deterministic, standard-library Python example using tiny synthetic data in every module; all nine are automatically executed by the COMP6713 checker.
- Added no external link, image, diagram, PDF, notebook, dataset, trained model, downloadable raw asset, external script, or external stylesheet.
- Updated `/pages/study-notes.html` into an ACTL3162/COMP6713 selector while preserving `/study-notes/` and representative ACTL3162 deep routes.
- Reused the established Jekyll layout, metadata, favicon, navigation, focus system, responsive styles, and MathJax support.
- Added narrow shared CSS for the collection index, note callouts, concepts, code, equations, tables, and module navigation.
- Added `scripts/check_comp6713_notes.py`, eight focused tests, workflow coverage, and README maintenance guidance.
- Kept `site-check.json` at zero exemptions and `_site/` untracked.
- Completed public-safe source-distance, structure, technical, mathematics, code, attribution, privacy, and assessment-integrity reviews. Recorded unresolved normalized 12-word prose overlaps: zero.

### Permanent exclusions preserved

- Official slides, tutorials, handouts, notebooks, attachments, and solutions.
- Assignment specifications, assessment questions, rubrics, answers, project code, examination preparation, and the entire team-assessment collection.
- Textbooks, copied readings, third-party diagrams/tables/code, and unclear-permission material.
- The mixed examination/course-recap note.
- Archived duplicates, hidden artifacts, private metadata, private communications, and student data.
- Private OneDrive paths, links, comments, revision history, screenshots, raw documents, and evidence files.

### Accepted validation evidence

- Starting SHA `d7f754dc9b36e4edb372bf59383dbdcdebd438af`.
- Implementation commit `5dac1aa679e057ec0f58c0a8b8d1036da1497da5`.
- Reviewed head `3681324c37d2876190c4fcc01cf2564ac422151e`.
- Jekyll build produced 25 HTML pages.
- Generated-site checker validated 428 references with zero exemptions.
- COMP6713 checker validated nine modules and nine executable examples across nine modules.
- Seventeen tests passed.
- JavaScript syntax, Python compilation, YAML, source-only `_site`, exact routes, privacy syntax, external-link/asset, and diff checks passed.
- Exact-head workflow run `30874223125` passed every step.
- 360 px smoke checks passed for the index, code-heavy Sequence Tagging page, and mathematics-heavy Attention page.

## M-003 — Full QA, evidence, and final approval

State: ACTIVE  
Dependencies: M-002 accepted through R-0002  
Active directive: D-0003  
Covers: AC-010, AC-011, AC-013, AC-014 and all final quality gates

### Active scope

- Correct the bounded terminology issue in Attention and Transformers: explain that self-attention without positional information is permutation-equivariant/order-unaware, rather than simply “insensitive to permutation.”
- Confirm no other important technical or mathematical defect across all nine modules.
- Re-run the public-safe source-distance, structure, technical, mathematics, code, attribution, privacy, and assessment-integrity reviews after any final correction; unresolved normalized 12-word prose overlaps must remain zero.
- Verify every COMP6713 index/module navigation path and the ACTL3162 selector/representative deep routes.
- Check the COMP6713 index and every module at 360 px, 768 px, and 1440 px, with focused worst-case evidence for code, tables, long headings, and mathematics.
- Test keyboard navigation, visible focus, skip link, desktop and compact navigation, module cards, previous/index/next links, code scrolling, table containment, MathJax containment, heading hierarchy, landmarks, and accessible names.
- Verify browser-console state and title, description, canonical URL, Open Graph fields, favicon, and one-H1 structure on the index and every module.
- Attach immutable screenshots for the index and representative text-, code-, table-, and mathematics-heavy pages at mobile and desktop widths.
- Confirm documentation describes example execution as an isolated interpreter/temporary working-directory policy check, not an adversarial security sandbox.
- Run the complete local suite and exact-head PR workflow.
- Request Bryan's explicit final factual-content and visual-presentation approval.
- Keep PR #13 draft and perform no merge or deployment.

### Validation

Run the full M-002 local suite plus the existing `Validate site` workflow at the exact final head. Record the workflow run ID, job ID, step conclusions, responsive/keyboard/console/metadata results, screenshots, integrity evidence, and any environment limitation.

### Exit evidence

- Exact starting, correction/QA, and final review SHAs.
- Exact-head successful CI.
- Reviewable immutable screenshots.
- Responsive evidence at 360 px, 768 px, and 1440 px across all ten COMP6713 routes.
- Keyboard, code/table/math-overflow, heading/landmark, metadata, and browser-console evidence.
- Zero unexplained source overlap, zero broken links, zero checker exemptions, no tracked `_site`, and all required routes present.
- Confirmation that every executable example remains original, synthetic, deterministic, standard-library-only, and passing.
- Bryan's explicit factual-content and visual-presentation approval.
- Final Project Director review with no unresolved critical or important defect.

## Risks and mitigations

- **RISK-001 — Restricted assessment material is published:** permanent exclusion of specifications, questions, solutions, rubrics, project code, exam preparation, and team-assessment material; dedicated private integrity review.
- **RISK-002 — Official or third-party course wording is closely paraphrased:** clean independent authorship, 12-word contiguous-prose overlap audit, and manual source-distance review.
- **RISK-003 — OneDrive details leak through a public PR:** keep paths, links, raw files, candidate notes, screenshots, excerpts, and private audit data outside GitHub; record aggregate results only.
- **RISK-004 — The all-nine-module scope encourages shortcuts:** stop rather than export or lightly transform source notes; require per-module technical and integrity evidence.
- **RISK-005 — Code examples reproduce private notebooks or require unsafe resources:** allow only newly authored, deterministic, synthetic, tested examples with no network, credentials, private files, datasets, models, or saved outputs.
- **RISK-006 — Note conversion changes meaning or introduces technical errors:** independently re-derive explanations and mathematics; run per-module technical, equation, code, and terminology review.
- **RISK-007 — Code, tables, or mathematics overflow on mobile:** reuse the responsive/MathJax system and test all modules plus representative worst cases at required widths.
- **RISK-008 — Existing ACTL3162 links break:** retain `/study-notes/` and `/study-notes/notes/`; validate representative deep links locally and in CI.
- **RISK-009 — The notes become an unofficial answer bank:** publish learning explanations and synthetic examples only; preserve the approved disclaimer and permanent assessment exclusions.

## Dependency policy

- Keep the current Jekyll, Liquid, HTML, CSS, MathJax, and minimal vanilla JavaScript stack.
- Use no new framework, CMS, backend, database, analytics, external font, or deployment action.
- Executable examples use Python's standard library.
- The COMP6713 checker and tests use the Python standard library.
- Prefer static source files and existing validation tooling.

## Documentation, migration, and rollout

- Preserve the completed redesign archive under `.project-loop/archive/2026-08-04-professional-portfolio-redesign/`.
- README or nearby maintenance documentation explains COMP6713 source paths, module creation, code-example testing, supported formatting, eligibility restrictions, integrity review, local validation, and Bryan-owned merge/publication.
- Existing ACTL3162 URLs remain stable; no migration or redirect is planned for them.
- Implementation remains on `agent/comp6713-notes` and draft PR #13 until final review.
- Codex and the Project Director must not merge or deploy; Bryan owns final publication.
