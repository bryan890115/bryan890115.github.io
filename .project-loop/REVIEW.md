# Project Reviews

## R-0001 — M-001 private eligibility review

Timestamp: `2026-08-04T12:45:00+10:00`  
Directive ID: D-0001  
Milestone ID: M-001  
Pull request: `#13` (`agent/comp6713-notes`)  
Exact reviewed head SHA: `249ab50c7f8d89f397e41f3e80f01bcf8da5ad86`  
Starting SHA: `24bb05e37458d73efa0350396f61894c47e6a2f1`  
Verdict: CONTINUE

### Evidence inspected

- PR #13 metadata, exact head, open/draft/mergeable state, one-file changed scope, and generic `CODEX_APPROVAL_REQUIRED D-0001` notification.
- Exact `.project-loop/STATUS.md` patch at the reviewed head.
- Codex's public-safe counts and private-packet delivery confirmation.
- Exact-head `Validate site` run `30872531021`; job `91877281856` passed every checkout, Ruby setup, Jekyll build, checker, nine-test, JavaScript, Python, YAML, source-only `_site`, zero-exemption, forbidden-copy, and required-route step.
- Bryan's direct answers approving authorship use, all nine modules, the proposed title, disclaimer, module order and routes, permanent exclusions, and newly authored synthetic code examples.

The private packet and source material were intentionally not copied into GitHub or reproduced in this review. Bryan reviewed those materials directly.

### Acceptance results

- **AC-001 — PASS:** Codex reports a private inventory of 255 associated files, including 133 Markdown note bodies, with format/content/authorship/assessment/publication classification and proposed grouping.
- **AC-002 — PASS:** Bryan explicitly approved the exact nine-module public-edition scope, title, disclaimer, routes, transformation boundaries, code-example policy, and permanent exclusions. These approvals are recorded in DEC-001.
- **AC-003 — PASS:** PR #13 changes only `.project-loop/STATUS.md`; no website source, public note, private path, private URL, raw file, excerpt, screenshot, candidate title, module summary, restricted material, or personal data entered GitHub.
- **AC-004 — PASS:** Official, third-party, restricted, assessment, duplicate, private-metadata, and uncertain material remains excluded. Zero files were accepted for direct export, and the public edition must be independently authored.

### Findings

No critical or important defect was found in the discovery gate.

The zero-as-is result is appropriate rather than a failure: the audit could not certify direct publication from filesystem evidence and found substantial source dependence. Bryan's authorship confirmation permits the candidate notes to guide topic coverage, but not to serve as publishable wording or a close paraphrase source.

The approved all-nine-module scope is materially larger than Codex's recommended three-module initial release. This is an explicit user decision and is accepted, but it increases the need for source-distance, technical, mathematics, code, privacy, and assessment-integrity evidence. D-0002 therefore requires independent authorship and a clean public edition rather than conversion of the vault.

### Strategic assessment

The safest route remains a clean static Jekyll edition beneath `/study-notes/comp6713/`, preserving the existing ACTL3162 routes. Newly authored, synthetic, tested examples can improve educational value without reusing restricted notebooks or datasets. No framework, CMS, raw document export, or private-source publication is justified.

### Single next action

Codex must execute active D-0002 on the existing `agent/comp6713-notes` branch and draft PR #13: independently author the approved index and all nine modules, use only newly authored synthetic code examples, preserve permanent exclusions and ACTL3162 routes, perform the required private source-similarity/integrity review, run all validation, and post `CODEX_READY D-0002 at <FULL_SHA>` when ready. Do not merge or deploy.

## R-0002 — M-002 clean public-edition implementation

Timestamp: `2026-08-04T13:17:00+10:00`  
Directive ID: D-0002  
Milestone ID: M-002  
Pull request: `#13` (`agent/comp6713-notes`)  
Exact reviewed head SHA: `3681324c37d2876190c4fcc01cf2564ac422151e`  
Starting SHA: `d7f754dc9b36e4edb372bf59383dbdcdebd438af`  
Implementation commit SHA: `5dac1aa679e057ec0f58c0a8b8d1036da1497da5`  
Exact-head workflow run: `30874223125`  
Verdict: CONTINUE

### Evidence inspected

- PR #13 metadata, exact head, open/draft/mergeable state, release summary, and `CODEX_READY D-0002` notification.
- Complete changed-file inventory and the exact-head versions of `.project-loop/STATUS.md`, the COMP6713 index, Resources selector, all nine module pages, shared CSS additions, `scripts/check_comp6713_notes.py`, its eight focused tests, README changes, and workflow integration.
- All nine executable examples and their surrounding conceptual and mathematical explanations.
- Exact-head `Validate site` run `30874223125`; job `91882278482` passed checkout, Ruby setup, Jekyll build, generated-site checking, COMP6713 note/example checking, seventeen tests, JavaScript syntax, Python compilation, YAML validation, source-only `_site`, zero-exemption, forbidden-copy, and required-route steps.
- Codex's public-safe aggregate source-distance, structure, technical, mathematics, code, attribution, privacy, and assessment-integrity results.

The private candidate corpus, excluded sources, comparison excerpts, and audit artifacts remain intentionally outside GitHub. This review can verify the public implementation, private-audit methodology recorded in the approved directive, aggregate zero-overlap result, and absence of private material in the public diff, but cannot independently reconstruct the private comparisons without defeating the approved privacy boundary.

### Acceptance results

- **AC-005 — PASS:** `/study-notes/comp6713/` contains the exact approved title and disclaimer, an original introduction, and semantic navigation to all nine modules in the approved order.
- **AC-006 — PASS:** All nine exact approved routes exist. Each page has metadata, one H1, hierarchical headings, an original overview, independently written explanations, an original executable worked example, and previous/index/next navigation.
- **AC-007 — PASS:** Mathematics, code, tables, and long technical content use contained source structures. All nine marked examples use standard-library Python, tiny synthetic literals, deterministic assertions, no network or credentials, and passed two isolated executions with timeouts.
- **AC-008 — PASS:** `/pages/study-notes.html` provides semantic ACTL3162 and COMP6713 links. Existing `/study-notes/` and representative ACTL3162 deep routes remain present and validated.
- **AC-009 — PASS:** The implementation reuses the shared Jekyll layout, navigation, metadata, focus system, and responsive design. Added CSS is narrow and specific to the notes, module list, code, equations, tables, callouts, and note navigation.
- **AC-012 — PASS:** README documents the COMP6713 structure, eligibility exclusions, executable-example convention, validation commands, and Bryan-owned merge/publication.

### Findings

No critical or important implementation, privacy, assessment-integrity, route, CI, or maintainability defect was found.

Minor final-QA corrections and limitations:

1. `study-notes/comp6713/notes/attention-and-transformers.html` says pure self-attention is "insensitive to permutation." The more precise beginner-facing statement is that self-attention without positional information is permutation-equivariant and therefore cannot represent token order. Correct this wording during M-003 without changing the module's scope.
2. The source-distance result is private aggregate evidence by design. It is accepted as a documented integrity control combined with Bryan's authorship confirmation, the clean-room workflow, the zero-overlap result, and the public diff inspection; it is not independently reproducible from GitHub alone.
3. The checker executes examples in an isolated interpreter and temporary working directory, but it is a repository policy check rather than a security sandbox. Final documentation and review must not imply adversarial sandbox guarantees.
4. Responsive evidence so far is a 360 px smoke check for the index and two representative modules. Full 360/768/1440 visual and keyboard evidence remains assigned to M-003.

### Strategic assessment

The implementation remains the fastest safe route to the approved result. It is static, source-only, independently authored, uses no external assets or new dependencies, preserves the existing course-note collection, and adds durable automated coverage for routes, navigation, privacy syntax, exact source set, and executable examples. Rewriting or reducing the nine-module edition is not justified by the inspected evidence.

### Single next action

Codex must execute active D-0003 on the existing branch and draft PR #13: make the bounded terminology correction, complete full responsive/keyboard/metadata/console and final integrity QA, attach immutable review screenshots, rerun exact-head CI, and request Bryan's final factual-content and visual-presentation approval. Do not merge or deploy.

The completed professional-portfolio redesign review history remains archived under:

`.project-loop/archive/2026-08-04-professional-portfolio-redesign/REVIEW.md`
