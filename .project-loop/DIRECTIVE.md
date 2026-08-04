# Current Codex Directive

Directive ID: D-0002  
Status: ACTIVE  
Milestone ID: M-002  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/comp6713-notes`  
Base SHA: `249ab50c7f8d89f397e41f3e80f01bcf8da5ad86`  
Issued timestamp: `2026-08-04T12:45:00+10:00`  
Replaced directive ID: D-0001

## Approval basis

R-0001 accepted the D-0001 private eligibility gate at the exact base SHA above. DEC-001 records Bryan's explicit decisions:

- the 97 candidate notes are Bryan's own synthesis and may be used only as private conceptual input for an independently authored public edition;
- all nine proposed modules are approved;
- the exact title, disclaimer, module order, and routes are approved;
- permanent exclusions are approved;
- the edition remains text-and-mathematics first with no private links and no reuse of existing code, outputs, datasets, trained models, tables, screenshots, PDFs, diagrams, course attachments, or raw assets; and
- newly authored, minimal, tested code examples using synthetic data are approved.

The private packet, source files, source identities, paths, excerpts, and detailed audit notes remain outside GitHub.

## Required outcome

Produce a clean, independently authored public COMP6713 study-notes edition using the existing Jekyll site. Add the approved index and all nine approved modules beneath `/study-notes/comp6713/`, update the Resources selector, preserve every ACTL3162 route, add original synthetic code examples, and provide sufficient public-safe evidence that no private, restricted, official, third-party, assessment, or closely copied source material entered the repository.

This directive implements content and source integration. It does not authorize final merge, deployment, final factual approval, or final visual approval.

## Approved public title and disclaimer

Title:

`COMP6713 Natural Language Processing — Personal Study Notes`

Disclaimer, reproduced exactly:

> These are Bryan Jen’s personal study notes for COMP6713 Natural Language Processing. They are not official UNSW course materials and are not endorsed by UNSW. Assessment questions, solutions, marking guidance, restricted course content, and copied teaching materials are intentionally excluded. Any errors are my own.

## Approved modules, order, routes, and broad scope

1. **Foundations of NLP**  
   Route: `/study-notes/comp6713/notes/foundations-of-nlp.html`  
   Scope: NLP tasks, ambiguity, probability, modelling paradigms, tools, and limitations.
2. **Representation Learning**  
   Route: `/study-notes/comp6713/notes/representation-learning.html`  
   Scope: discrete vectors, embeddings, probabilistic language models, and neural language models.
3. **Attention and Transformers**  
   Route: `/study-notes/comp6713/notes/attention-and-transformers.html`  
   Scope: query-key-value attention, Transformer components, tokenisation, positional encoding, and training.
4. **Modern Language Models**  
   Route: `/study-notes/comp6713/notes/modern-language-models.html`  
   Scope: BERT/GPT model families, fine-tuning, parameter-efficient adaptation, prompting, evaluation, and tool augmentation.
5. **Sentiment Analysis**  
   Route: `/study-notes/comp6713/notes/sentiment-analysis.html`  
   Scope: tasks, annotation, evaluation, and rule-based, statistical, neural, Transformer, and prompting approaches.
6. **Sequence Tagging**  
   Route: `/study-notes/comp6713/notes/sequence-tagging.html`  
   Scope: part-of-speech tagging, named-entity recognition, BIO encoding, HMM/Viterbi, CRFs, and neural sequence models.
7. **Machine Translation**  
   Route: `/study-notes/comp6713/notes/machine-translation.html`  
   Scope: translation challenges, metrics, statistical alignment, Transformer translation, and decoding.
8. **Summarisation and Question Answering**  
   Route: `/study-notes/comp6713/notes/summarisation-and-question-answering.html`  
   Scope: extractive and abstractive methods, long-document models, question answering, retrieval, and alignment.
9. **NLP Applications and Responsible Deployment**  
   Route: `/study-notes/comp6713/notes/nlp-applications-and-responsible-deployment.html`  
   Scope: applications, hallucination, fairness, mitigation, commonsense reasoning, and explanation-based reasoning.

## Clean-room authorship workflow

1. Record the exact pre-work branch head as `Starting SHA` in `.project-loop/STATUS.md` before changing public source.
2. Verify this directive's base SHA is an ancestor of the starting head and that changes between the base and starting head are limited to Director-owned `.project-loop/DECISIONS.md`, `.project-loop/REVIEW.md`, `.project-loop/PLAN.md`, and `.project-loop/DIRECTIVE.md`.
3. Create an original page outline from the approved module names and broad scopes above. Do not reuse the private vault's file order, heading order, paragraph order, examples, tables, or phrasing.
4. Draft each public module independently from stable subject knowledge and newly derived examples without sentence-by-sentence access to the private source text.
5. After an independent draft exists, use the 97 candidate notes only as a private concept-coverage checklist. Do not copy missing material into the draft; independently explain or omit it.
6. Review every draft against private and official/permission-sensitive material. Resolve all unexplained source similarity and remove any material whose ownership, permission, assessment status, or independent authorship remains uncertain.
7. Keep every private file, path, link, source identity, source excerpt, comparison excerpt, and audit artifact outside GitHub.

## In-scope implementation

1. Create `study-notes/comp6713/index.html` with:
   - the exact approved title;
   - the exact approved disclaimer;
   - a concise original introduction;
   - semantic navigation to all nine modules in the approved order; and
   - navigation back to the public Resources selector.
2. Create all nine approved module pages beneath `study-notes/comp6713/notes/` at the exact approved routes.
3. Each module must contain:
   - a descriptive page title and metadata description;
   - one H1 and sensible hierarchical headings;
   - a concise original overview;
   - independently authored conceptual explanations;
   - at least one original worked example, mathematical derivation, executable example, or clearly labelled pseudocode example appropriate to the topic;
   - semantic previous/index/next navigation; and
   - no course logistics, assessment guidance, solution content, private references, or unsupported claims.
4. Across the nine modules, include executable Python examples in at least six modules. Use original mathematical or pseudocode examples in modules where executable code would be artificial or misleading.
5. Every executable example must:
   - be newly authored for this public edition;
   - use Python's standard library unless a separately approved dependency is necessary;
   - use tiny synthetic data created inside the example;
   - be deterministic and terminate quickly;
   - require no network, credentials, environment secrets, private file, external dataset, downloaded model, or saved output;
   - avoid code adapted from course notebooks, assignments, solutions, team projects, private repositories, textbooks, or third parties; and
   - be automatically executed by the COMP6713 validation tooling.
6. Mark executable and non-executable examples with a consistent source convention. Non-executable pseudocode must be visibly labelled as pseudocode and excluded from execution claims.
7. Re-derive mathematics independently. Define notation locally, avoid unexplained symbol reuse, verify simple numerical examples, and ensure MathJax renders without narrow-screen overflow.
8. Do not reuse any existing private or official table. New source-independent semantic tables are permitted only when they clarify a comparison and are checked for mobile containment.
9. Add no COMP6713 image, diagram, PDF, screenshot, dataset, model, downloadable notebook, external script, external stylesheet, or external public link under D-0002. Existing shared site assets, internal relative links, favicon, and existing MathJax integration remain permitted.
10. Update `pages/study-notes.html` into an accessible course selector linking to:
    - the existing ACTL3162 notes at `/study-notes/`; and
    - the new COMP6713 notes at `/study-notes/comp6713/`.
11. Preserve all existing ACTL3162 source and routes, including `/study-notes/` and `/study-notes/notes/mod0.html` through the existing module set. Do not rewrite ACTL3162 content except for a strictly necessary shared compatibility fix.
12. Reuse the existing shared layout, navigation, footer, metadata, favicon, focus treatment, responsive grid, note typography, and MathJax support. Add only narrow shared CSS required for code, tables, equations, callouts, and module navigation.
13. Create `scripts/check_comp6713_notes.py` using only the Python standard library. It must validate at minimum:
    - the exact approved index and nine module source files exist;
    - the exact approved disclaimer is present on the index;
    - module order and internal previous/index/next navigation are complete and relative;
    - no OneDrive, SharePoint, local filesystem, Obsidian, vault embed, private-link, or unapproved external-link syntax appears;
    - no `<img>`, downloadable raw-note asset, embedded PDF, notebook, or external media appears in the COMP6713 section;
    - marked executable Python examples are extracted and executed safely with a reasonable timeout; and
    - marked pseudocode is not counted as executed code.
14. Add focused unit tests for the COMP6713 checker, including failures for missing modules, forbidden private syntax, external links/assets, broken navigation, and failing executable examples.
15. Update README or nearby maintenance documentation with:
    - COMP6713 source paths and route structure;
    - how to add or edit modules without changing approved scope;
    - the exact eligibility and permanent-exclusion boundary;
    - executable-example marking and validation;
    - local build/check commands; and
    - Bryan-owned merge and publication.
16. Keep `site-check.json` at zero exemptions and `_site/` fully untracked.
17. Update `.project-loop/STATUS.md` with exact SHAs, changed files, public-safe module mapping, code-example inventory, validation, source-distance/integrity evidence, deviations, risks, blockers, and review focus.
18. Update existing draft PR #13 with a public-safe M-002 summary and post `CODEX_READY D-0002 at <FULL_SHA>` only after the local suite and exact-head PR workflow succeed.

## Required private integrity review

Before posting `CODEX_READY`, complete all of the following locally without committing private input or excerpts:

1. **Source-distance audit:** compare public prose against the private candidate corpus for normalized contiguous prose overlap of 12 or more words. Exclude page/module titles, the exact approved disclaimer, code, equations, standard named technical terms, and clearly marked permitted quotations. Resolve every unexplained overlap through independent rewriting.
2. **Structure audit:** confirm no module substantially mirrors a private/official note's heading sequence, example sequence, or section progression beyond the approved high-level module scope.
3. **Technical review:** inspect each module for conceptual accuracy, terminology, limitations, distinctions between modelling paradigms, and avoidance of misleading simplification.
4. **Mathematics review:** verify notation, equations, dimensions, probabilities, worked calculations, and MathJax source.
5. **Code review:** execute every marked example and confirm synthetic inputs, deterministic output, no network/private dependency, and no copied/adapted source code.
6. **Citation/attribution review:** remove quotations and source-specific claims unless publication and attribution are clearly permitted. Because the approved treatment contains no external links, prefer original explanations and omit uncertain claims.
7. **Privacy review:** scan for private paths, URLs, names, comments, metadata, identifiers, credentials, and local embed syntax.
8. **Assessment-integrity review:** confirm no specification, question, solution, marking guidance, exam preparation, project content, team-assessment material, or answer-bank pattern appears.

Record only public-safe aggregate outcomes in `STATUS.md`: method, number of modules reviewed, number of overlaps found/resolved/unresolved, number of executable examples passed, public paths changed during review, and whether each integrity category passed. Never record private source names or overlap text.

## Permanent exclusions

- Official slides, tutorials, handouts, notebooks, attachments, and solutions.
- Assignment specifications, assessment questions, marking rubrics, answers, project code, examination preparation, and the entire team-assessment collection.
- Textbooks, copied readings, third-party code/tables/diagrams, and unclear-permission material.
- The mixed examination/course-recap note.
- Archived duplicates, hidden artifacts, private metadata, private communications, and student data.
- Existing private code, outputs, datasets, trained models, tables, screenshots, PDFs, diagrams, attachments, and raw assets.
- OneDrive paths, SharePoint URLs, private links, comments, revision history, source identities, source excerpts, screenshots, and audit artifacts.

## Explicitly out of scope

- Directly exporting, converting, copying, line-editing, lightly paraphrasing, or publishing any private vault file.
- Publishing official or third-party material merely because it appears inside Bryan's synthesis notes.
- Reconstructing assignment questions, solutions, rubrics, project code, tutorial answers, or examination material.
- Adding external links, images, diagrams, raw documents, PDFs, notebooks, downloadable datasets/models, or embedded media.
- Introducing a framework, CMS, backend, database, analytics, external font, new runtime dependency, or deployment action.
- Changing approved portfolio biography, research, projects, contact channels, home content, custom-domain configuration, or unrelated pages.
- Merging PR #13, marking it ready, deploying, pushing directly to `main`, or changing repository/Pages/DNS settings.
- Claiming final factual or visual approval; that remains M-003.

## Mapped acceptance criteria

- AC-005
- AC-006
- AC-007
- AC-008
- AC-009
- AC-012

## Required evidence

- Exact starting SHA, implementation commit SHA, and final review head SHA.
- Pre-work comparison proving only Director-owned handoff files changed after the D-0002 base.
- Focused changed-file inventory.
- Public-safe approval mapping for the index and every module.
- Exact course selector and ACTL3162 route-preservation evidence.
- Per-module headings/content/example inventory without private-source references.
- Executable code-example inventory: public path, purpose, synthetic-input description, standard-library confirmation, and pass result.
- COMP6713 checker and focused unit-test evidence.
- Private source-distance audit method and aggregate counts of found, resolved, and unresolved overlaps; unresolved must be zero.
- Aggregate structure, technical, mathematics, code, citation/attribution, privacy, and assessment-integrity results; every category must pass or be explicitly blocked.
- Confirmation that no permanently excluded or private material entered source, GitHub history, PR text, screenshots, or built output.
- Successful local validation and exact-head workflow identity/conclusion.
- Responsive smoke evidence for the index and at least one code-heavy and one mathematics-heavy module at 360 px, sufficient to catch implementation blockers before M-003.

## Exact validation commands

Set `STARTING_SHA` to the exact branch head before implementation edits, then run:

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
! grep -RniE 'https?://|<img\b|\.pdf(["'"'#?]|$)|\.ipynb(["'"'#?]|$)' study-notes/comp6713

git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

If the default system Ruby cannot load the pinned Bundler, use the existing supported Ruby/Bundler launcher and record the exact deviation. The no-URL scan applies to COMP6713 source content; normal YAML front matter and existing shared layout-generated canonical metadata are not violations.

## Publication permission

Codex may continue on `agent/comp6713-notes`, commit and push the bounded M-002 implementation, update existing draft PR #13, and post the ready notification after all required local and CI conditions pass.

Codex must not merge, deploy, mark the PR ready, push directly to `main`, change repository settings, expose private material, or broaden the approved module/content scope.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- Independent drafting of all nine modules cannot be completed without copying, close paraphrase, or structural imitation of private/official material.
- Any unresolved normalized 12-word prose overlap remains after permitted exclusions.
- Authorship, copyright, permission, privacy, or assessment status becomes uncertain for any included explanation, example, code, table, or equation.
- Technical or mathematical accuracy cannot be established without importing excluded source content.
- A useful code example would require a private notebook, assignment/project code, dataset, model, network call, credential, external dependency, or saved output.
- A permanent exclusion would need to be weakened.
- Existing ACTL3162 routes or accepted portfolio content would break without an unapproved migration.
- The starting branch contains unexpected production changes after the D-0002 base.
- The implementation requires an excluded dependency, external asset, framework, backend, or material architecture change.
- Exact-head PR validation fails and cannot be fixed within the bounded scope.

## Next Project Director review focus

- Whether the public edition is genuinely independently authored rather than exported or closely paraphrased.
- Whether all nine approved modules have accurate, useful, coherent, source-independent explanations.
- Whether code examples are original, synthetic, minimal, tested, and safe.
- Whether mathematics, tables, code, and long technical content render correctly and remain understandable.
- Whether the checker and tests provide durable protection against private links, external assets, broken navigation, and untested examples.
- Whether ACTL3162 routes and the established site design remain intact.
- Whether all private, official, third-party, assessment, and permanent-exclusion boundaries are preserved.
- Whether M-002 can be accepted and M-003 activated without a revision pass.
