# COMP6713 Course Notes Publication Plan

State: APPROVED  
Specification state: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Planning branch: `agent/comp6713-notes-plan`  
Intended implementation branch: `agent/comp6713-notes`  
Base SHA: `a19fe81dadcc03e7de85f2268bc0b5666d20d031`  
Draft date: 2026-08-04  
Approval date: 2026-08-04

## Delivery strategy

Deliver three reviewable milestones. First separate publication eligibility from implementation so private OneDrive material, assessment content, and third-party course material cannot leak into the public repository. Then implement only the exact module set Bryan approves. Finish with full route, accessibility, responsive, CI, and final-content review.

## M-001 — Private discovery and publication eligibility

State: ACTIVE  
Dependencies: Specification and plan approved by Bryan on 2026-08-04  
Active directive: D-0001  
Covers: AC-001, AC-002, AC-003, AC-004

### Scope

- Inspect only the OneDrive material clearly associated with Bryan's COMP6713 notes.
- Inventory file formats and note bodies without copying private source material into GitHub.
- Classify every candidate file, section, and asset as:
  - Bryan-authored and publishable;
  - publishable after redaction or conversion into Bryan's own words;
  - official/third-party material requiring permission; or
  - restricted/assessment material that must be excluded.
- Identify assignment specifications, questions, solutions, marking rubrics, current assessment material, official slides/handouts, copied readings, private communications, student data, and unclear-ownership material for exclusion.
- Prepare a private approval packet with:
  - proposed public course title and disclaimer;
  - proposed module titles, order, and one-sentence summaries;
  - proposed handling for code, mathematics, tables, diagrams, and citations;
  - ownership and assessment-risk classification;
  - exact proposed public links/assets or no-link/no-asset treatment;
  - excluded or uncertain material and the reason; and
  - any decision Bryan must make before publication.
- Commit only a public-safe `.project-loop/STATUS.md` update and post a generic approval-required PR notification.
- Make no public website or note-content change.

### Validation

```bash
git merge-base --is-ancestor <D-0001_BASE_SHA> "$STARTING_SHA"
git diff --name-only <D-0001_BASE_SHA>..."$STARTING_SHA"
git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

The post-work diff must contain only `.project-loop/STATUS.md`. Any public note, page, asset, OneDrive-derived path, title, excerpt, or candidate detail in GitHub is a blocker.

### Exit evidence

- Exact starting and final branch SHAs.
- Number of private source files or note bodies inspected and number proposed for publication.
- Private approval packet delivered directly to Bryan.
- Confirmation that assessment, official, third-party, private, and uncertain material remains excluded.
- Confirmation that no OneDrive path, raw file, private URL, excerpt, image, candidate title, or public note content entered GitHub.
- Public-safe `STATUS.md` and generic `CODEX_APPROVAL_REQUIRED D-0001` notification.

## M-002 — Approved COMP6713 notes implementation

State: PENDING  
Dependencies: M-001 accepted; Bryan approves the exact module set, copy, assets, links, exclusions, and transformations  
Covers: AC-005, AC-006, AC-007, AC-008, AC-009, AC-012

### Scope

- Create `/study-notes/comp6713/` as the COMP6713 course-notes index.
- Add only the approved module pages beneath `/study-notes/comp6713/notes/`.
- Use the approved course title and a clear personal-notes/not-official-course-material disclaimer.
- Preserve the approved note substance and order; perform formatting and light editorial cleanup only where it does not change meaning.
- Use semantic headings, module navigation, code blocks, MathJax, tables, citations, and approved diagrams as required by the source material.
- Do not invent missing content, fill perceived gaps, add assignment answers, or publish excluded evidence.
- Update `/pages/study-notes.html` into a clear course selector for existing ACTL3162 and new COMP6713 notes.
- Keep `/study-notes/` as the existing ACTL3162 landing page and preserve all ACTL3162 module URLs.
- Add only narrow shared CSS or layout support needed for technical notes, code, tables, diagrams, or module navigation.
- Update maintenance documentation with the new COMP6713 source structure and publication boundary.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
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
ruby -e 'required=%w[_site/pages/study-notes.html _site/study-notes/index.html _site/study-notes/notes/mod0.html _site/study-notes/comp6713/index.html]; required.each { |f| abort("missing or empty: #{f}") unless File.file?(f) && File.size(f) > 0 }; puts "notes routes non-empty"'
git diff --check
git status --short --branch
```

The required-route command must be expanded to include every approved COMP6713 module page.

### Exit evidence

- Exact implementation starting SHA, implementation commit SHA, and final review head.
- Approved module list and public-safe source/approval mapping.
- Working COMP6713 index and all approved modules.
- Resources page linking both courses.
- Preserved ACTL3162 landing and representative deep links.
- Confirmation that no excluded, private, assessment, official, or unclear-ownership material entered the repository or build.
- Successful local validation and a generic `CODEX_READY` notification.

## M-003 — Full QA, CI, and final approval

State: PENDING  
Dependencies: M-002 accepted  
Covers: AC-010, AC-011, AC-013, AC-014 and all final quality gates

### Scope

- Run exact-head pull-request CI and resolve only bounded integration, accessibility, route, or formatting defects.
- Verify every COMP6713 module and navigation path.
- Check COMP6713 index and representative modules at 360 px, 768 px, and 1440 px.
- Test keyboard navigation, focus visibility, code scrolling, table containment, MathJax containment, heading structure, landmarks, accessible names, and browser-console state.
- Verify title, description, canonical URL, Open Graph metadata, and favicon for the COMP6713 index and representative module pages.
- Attach immutable screenshots for the COMP6713 index and representative text/code/math-heavy modules.
- Confirm site checker, tests, zero exemptions, source-only `_site`, required routes, and exact-head workflow success.
- Obtain Bryan's final factual-content and visual approval.
- Keep the PR draft and perform no merge or deployment.

### Validation

Run the full M-002 local suite plus the existing `Validate site` workflow at the exact final head. Record the workflow run ID, job ID, step conclusions, responsive/keyboard/console/metadata results, screenshots, and any external-link limitation.

### Exit evidence

- Exact-head successful CI.
- Reviewable immutable screenshots.
- Responsive, keyboard, code/table/math-overflow, heading/landmark, metadata, and browser-console evidence.
- Zero broken links, zero checker exemptions, no tracked `_site`, and all required routes present.
- Bryan's explicit factual-content and visual-presentation approval.
- Final Project Director review with no unresolved critical or important defect.

## Risks and mitigations

- **RISK-001 — Restricted assessment material is published:** use a private eligibility gate; exclude assignment specifications, questions, solutions, rubrics, current assessment material, and unclear items by default.
- **RISK-002 — Official or third-party course content is copied:** classify authorship and permission section by section; publish only Bryan-authored content or clearly permitted material.
- **RISK-003 — OneDrive details leak through a public PR:** keep private paths, links, raw files, candidate notes, screenshots, and discovery details outside GitHub; use only public-safe counts and approval states.
- **RISK-004 — Note conversion changes meaning:** preserve approved ordering and substance; limit edits to formatting and light clarity improvements; require Bryan's content approval.
- **RISK-005 — Code, tables, or mathematics overflow on mobile:** reuse the existing responsive/MathJax system and test representative worst-case modules at required widths.
- **RISK-006 — Existing ACTL3162 links break:** retain `/study-notes/` and `/study-notes/notes/`; validate representative deep links locally and in CI.
- **RISK-007 — The notes become an unofficial answer bank:** publish learning notes only, include a personal-notes disclaimer, and omit restricted or assessment-answer material.
- **RISK-008 — Source format is difficult to convert:** record the format and blocker in the private packet; do not upload raw documents merely to make conversion easier.

## Dependency policy

- Keep the current Jekyll, Liquid, HTML, CSS, MathJax, and minimal vanilla JavaScript stack.
- Use no new framework, CMS, backend, database, analytics, external font, or deployment action.
- Add no new runtime dependency unless the approved notes cannot be represented safely with the existing stack and Bryan approves the material change.
- Prefer static source files and the existing standard-library validation tooling.

## Documentation, migration, and rollout

- Preserve the completed redesign archive under `.project-loop/archive/2026-08-04-professional-portfolio-redesign/`.
- README or nearby maintenance documentation must explain COMP6713 source paths, module creation, supported formatting, eligibility restrictions, local validation, and Bryan-owned merge/publication.
- Existing ACTL3162 URLs remain stable; no migration or redirect is planned for them.
- Implementation remains on `agent/comp6713-notes` and a draft PR until final review.
- Codex and the Project Director must not merge or deploy; Bryan owns final publication.
