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

State: ACTIVE  
Dependencies: M-001 accepted through R-0001; exact publication scope approved through DEC-001  
Active directive: D-0002  
Covers: AC-005, AC-006, AC-007, AC-008, AC-009, AC-012

### Approved public structure

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

### Active scope

- Independently author the index and all nine module pages. The private notes may guide conceptual coverage only; they must not be exported, copied, line-edited, sentence-transformed, or closely paraphrased.
- Preserve the approved module order and broad scope while using an original explanatory structure within each page.
- Use semantic headings, concise explanations, independently re-derived mathematics, original examples, accessible code blocks, and source-independent comparison lists or tables only when they materially aid understanding.
- Include newly authored code examples where pedagogically useful. Every executable example must:
  - use synthetic data;
  - be minimal and deterministic;
  - require no credentials, network access, private files, downloaded models, or saved outputs;
  - be independently written rather than adapted from course notebooks, assignments, solutions, team projects, or private code; and
  - be automatically tested using standard-library validation or the repository test suite.
- Clearly label non-executable pseudocode and do not present it as tested code.
- Do not reuse existing code, outputs, datasets, trained models, tables, screenshots, PDFs, diagrams, course attachments, or raw assets from the private material.
- Do not add external links or assets in this milestone. Shared existing site assets and MathJax remain permitted.
- Remove all private embeds, local links, vault syntax, course logistics, assessment references outside the approved disclaimer, and source-specific metadata.
- Update `/pages/study-notes.html` into a clear selector for ACTL3162 and COMP6713.
- Preserve `/study-notes/` as the existing ACTL3162 landing page and preserve all existing `/study-notes/notes/*.html` routes.
- Reuse the established Jekyll layout, metadata, favicon, navigation, focus styles, and responsive system.
- Add only narrow shared CSS or static source support needed for note typography, code, tables, mathematics, and module navigation.
- Add a standard-library COMP6713 validation script and tests that verify the exact module set, approved disclaimer, relative navigation, absence of private/local/embed syntax, absence of unapproved external links/assets, and execution of marked Python examples.
- Update README or nearby maintenance documentation with the COMP6713 structure, example-testing method, and publication-eligibility boundary.
- Perform a local private-source integrity review before requesting evaluation:
  - compare public prose against the private candidate corpus for unexplained normalized contiguous prose overlap of 12 or more words, excluding titles, the approved disclaimer, code, equations, standard named terms, and explicitly permitted quotations;
  - resolve all unexplained overlap through independent rewriting;
  - review every module for technical accuracy, equation correctness, code correctness, privacy, attribution needs, and assessment integrity; and
  - record only public-safe aggregate results and affected public paths, never private excerpts or source identities.

### Permanent exclusions

- Official slides, tutorials, handouts, notebooks, attachments, and solutions.
- Assignment specifications, assessment questions, rubrics, answers, project code, examination preparation, and the entire team-assessment collection.
- Textbooks, copied readings, third-party diagrams/tables/code, and unclear-permission material.
- The mixed examination/course-recap note.
- Archived duplicates, hidden artifacts, private metadata, private communications, and student data.
- Private OneDrive paths, links, comments, revision history, screenshots, raw documents, and evidence files.

### Validation

```bash
git merge-base --is-ancestor 249ab50c7f8d89f397e41f3e80f01bcf8da5ad86 "$STARTING_SHA"
git diff --name-only 249ab50c7f8d89f397e41f3e80f01bcf8da5ad86..."$STARTING_SHA"
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
python3 scripts/check_comp6713_notes.py study-notes/comp6713
python3 -m unittest discover -s tests -v
node --check assets/js/script.js
python3 -m compileall scripts
ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
test -z "$(git ls-files _site)"
python3 - <<'PY'
import json
from pathlib import Path
config = json.loads(Path("site-check.json").read_text())
assert config.get("exemptions") == [], config.get("exemptions")
print("zero exemptions")
PY
ruby -e 'required=%w[_site/pages/study-notes.html _site/study-notes/index.html _site/study-notes/notes/mod0.html _site/study-notes/comp6713/index.html _site/study-notes/comp6713/notes/foundations-of-nlp.html _site/study-notes/comp6713/notes/representation-learning.html _site/study-notes/comp6713/notes/attention-and-transformers.html _site/study-notes/comp6713/notes/modern-language-models.html _site/study-notes/comp6713/notes/sentiment-analysis.html _site/study-notes/comp6713/notes/sequence-tagging.html _site/study-notes/comp6713/notes/machine-translation.html _site/study-notes/comp6713/notes/summarisation-and-question-answering.html _site/study-notes/comp6713/notes/nlp-applications-and-responsible-deployment.html]; required.each { |f| abort("missing or empty: #{f}") unless File.file?(f) && File.size(f) > 0 }; puts "notes routes non-empty"'
! grep -RniE 'onedrive|sharepoint|file://|obsidian://|/Users/|[A-Za-z]:\\|!\[\[|\[\[[^]]+\]\]' study-notes/comp6713 pages/study-notes.html
git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

If the default system Ruby cannot load the pinned Bundler, use the existing supported Ruby/Bundler launcher and record the exact deviation. The COMP6713 checker may define safe exceptions for ordinary Markdown links only when they are relative public-site links; it must not weaken the no-private-link or no-external-link boundary.

### Exit evidence

- Exact implementation starting SHA, implementation commit SHA, and final review head.
- Public-safe module and approval mapping for all nine pages.
- Working index and all nine approved module routes.
- Resources page linking ACTL3162 and COMP6713.
- Preserved ACTL3162 landing and representative deep links.
- Inventory of newly authored executable and pseudocode examples, with test outcomes and synthetic-data confirmation.
- Public-safe source-similarity results, including method, exclusions, count of unresolved overlaps, and public paths rewritten.
- Technical, mathematics, code, attribution, privacy, and assessment-integrity review results for every module.
- Confirmation that no excluded, private, assessment, official, third-party, raw, or unclear-ownership material entered the repository or build.
- Successful local validation and exact-head PR workflow result.
- Generic `CODEX_READY D-0002 at <FULL_SHA>` notification.

## M-003 — Full QA, evidence, and final approval

State: PENDING  
Dependencies: M-002 accepted  
Covers: AC-010, AC-011, AC-013, AC-014 and all final quality gates

### Scope

- Review all M-002 implementation and integrity evidence at the exact head.
- Resolve only bounded integration, accessibility, route, technical-accuracy, source-distance, code, mathematics, or formatting defects.
- Verify every COMP6713 module and navigation path.
- Check COMP6713 index and representative modules at 360 px, 768 px, and 1440 px.
- Test keyboard navigation, focus visibility, code scrolling, table containment, MathJax containment, heading structure, landmarks, accessible names, and browser-console state.
- Verify title, description, canonical URL, Open Graph metadata, and favicon for the COMP6713 index and representative module pages.
- Attach immutable screenshots for the COMP6713 index and representative text-, code-, table-, and mathematics-heavy modules.
- Confirm site checker, COMP6713 checker, tests, zero exemptions, source-only `_site`, required routes, and exact-head workflow success.
- Obtain Bryan's final factual-content and visual approval.
- Keep the PR draft and perform no merge or deployment.

### Validation

Run the full M-002 local suite plus the existing `Validate site` workflow at the exact final head. Record the workflow run ID, job ID, step conclusions, responsive/keyboard/console/metadata results, screenshots, integrity evidence, and any external limitation.

### Exit evidence

- Exact-head successful CI.
- Reviewable immutable screenshots.
- Responsive, keyboard, code/table/math-overflow, heading/landmark, metadata, and browser-console evidence.
- Zero unexplained source overlap, zero broken links, zero checker exemptions, no tracked `_site`, and all required routes present.
- Bryan's explicit factual-content and visual-presentation approval.
- Final Project Director review with no unresolved critical or important defect.

## Risks and mitigations

- **RISK-001 — Restricted assessment material is published:** permanent exclusion of specifications, questions, solutions, rubrics, project code, exam preparation, and team-assessment material; dedicated private integrity review.
- **RISK-002 — Official or third-party course wording is closely paraphrased:** clean independent authorship, 12-word contiguous-prose overlap audit, and manual source-distance review.
- **RISK-003 — OneDrive details leak through a public PR:** keep paths, links, raw files, candidate notes, screenshots, excerpts, and private audit data outside GitHub; record aggregate results only.
- **RISK-004 — The all-nine-module scope encourages shortcuts:** stop rather than export or lightly transform source notes; require per-module technical and integrity evidence.
- **RISK-005 — Code examples reproduce private notebooks or require unsafe resources:** allow only newly authored, deterministic, synthetic, tested examples with no network, credentials, private files, datasets, models, or saved outputs.
- **RISK-006 — Note conversion changes meaning or introduces technical errors:** independently re-derive explanations and mathematics; run per-module technical, equation, code, and terminology review.
- **RISK-007 — Code, tables, or mathematics overflow on mobile:** reuse the responsive/MathJax system and test representative worst-case modules at required widths.
- **RISK-008 — Existing ACTL3162 links break:** retain `/study-notes/` and `/study-notes/notes/`; validate representative deep links locally and in CI.
- **RISK-009 — The notes become an unofficial answer bank:** publish learning explanations and synthetic examples only; preserve the approved disclaimer and permanent assessment exclusions.

## Dependency policy

- Keep the current Jekyll, Liquid, HTML, CSS, MathJax, and minimal vanilla JavaScript stack.
- Use no new framework, CMS, backend, database, analytics, external font, or deployment action.
- Executable examples should use Python's standard library unless a material dependency is separately proposed and approved.
- The COMP6713 checker and tests must use the Python standard library.
- Prefer static source files and existing validation tooling.

## Documentation, migration, and rollout

- Preserve the completed redesign archive under `.project-loop/archive/2026-08-04-professional-portfolio-redesign/`.
- README or nearby maintenance documentation must explain COMP6713 source paths, module creation, code-example testing, supported formatting, eligibility restrictions, integrity review, local validation, and Bryan-owned merge/publication.
- Existing ACTL3162 URLs remain stable; no migration or redirect is planned for them.
- Implementation remains on `agent/comp6713-notes` and draft PR #13 until final review.
- Codex and the Project Director must not merge or deploy; Bryan owns final publication.
