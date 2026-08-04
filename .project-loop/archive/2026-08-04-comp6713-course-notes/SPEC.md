# COMP6713 Course Notes Publication Specification

Protocol version: 1  
State: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Planning branch: `agent/comp6713-notes-plan`  
Intended implementation branch: `agent/comp6713-notes`  
Approval state: APPROVED BY BRYAN JEN  
Draft date: 2026-08-04  
Approval date: 2026-08-04  
Base SHA: `a19fe81dadcc03e7de85f2268bc0b5666d20d031`

## Goal

Publish Bryan's eligible, self-authored COMP6713 course notes from OneDrive as a professional, accessible section of the existing Jekyll website without exposing private storage details, restricted assessment material, official course content, or third-party copyrighted material.

## Requested outcome

- Add a COMP6713 notes landing page at `/study-notes/comp6713/`.
- Publish approved note modules beneath `/study-notes/comp6713/notes/` using the existing website design system.
- Update the Resources compatibility page so visitors can reach both the existing ACTL3162 notes and the new COMP6713 notes.
- Preserve every existing ACTL3162 route, including `/study-notes/` and `/study-notes/notes/*.html`.

## Goals

- Use OneDrive as read-only discovery evidence before any public content is committed.
- Publish only content Bryan authored or has clear permission to publish.
- Preserve the substance and ordering of Bryan's approved notes while improving navigation, readability, formatting, and accessibility.
- Support headings, tables, code examples, mathematical notation, citations, and diagrams where present and publishable.
- Clearly label the material as personal study notes rather than official course material.
- Keep the site buildable, responsive, keyboard accessible, source-only, and covered by the existing validation workflow.

## Non-goals

- Publishing official lecture slides, tutorial sheets, readings, textbooks, course handouts, assignment specifications, assessment questions, marking rubrics, answer keys, solutions, current restricted course material, or material copied from third parties without permission.
- Publishing private OneDrive paths, sharing links, raw evidence files, metadata, comments, revision history, credentials, student information, or private course communications.
- Reconstructing missing notes, inventing explanations, or adding unverified course facts merely to make the section appear complete.
- Providing answers or assistance for restricted or current assessments.
- Rewriting the existing ACTL3162 notes or changing their established URLs.
- Changing the portfolio's approved biography, research, projects, contact information, visual direction, custom-domain configuration, analytics, or deployment settings.
- Migrating away from Jekyll or introducing a JavaScript/CSS framework, CMS, backend, or database.
- Merge or deployment by Codex or the Project Director.

## Constraints

- OneDrive material is private evidence until Bryan approves exact public-facing content.
- Public GitHub commits and pull-request text must not contain OneDrive paths, private links, raw files, excluded candidate details, or private review notes.
- Each note or section must be classified before publication as:
  - Bryan-authored and publishable;
  - publishable after redaction or rewriting into Bryan's own words;
  - third-party or official material requiring permission; or
  - restricted/assessment material that must be excluded.
- When ownership, permission, assessment status, or authorship is unclear, omit the material and escalate.
- Preserve `/study-notes/`, `/study-notes/notes/`, `/pages/study-notes.html`, and representative ACTL3162 deep links.
- New pages must use HTML, Liquid, CSS, MathJax where needed, and minimal existing JavaScript only.
- Generated `_site/` output must remain untracked and must not be edited as source.
- The existing `Validate site` workflow must continue to pass with zero checker exemptions.
- Layouts must work at 360 px, 768 px, and 1440 px without horizontal scrolling, including long code and mathematical expressions.
- Interactive elements must be semantic, keyboard operable, and visibly focusable.

## Assumptions

- Bryan wants eligible COMP6713 notes made public after reviewing a private publication packet.
- OneDrive contains at least some notes primarily authored by Bryan.
- The notes may require conversion from Word, PDF, Markdown, notebooks, images, or mixed formats.
- The existing ACTL3162 landing page remains the canonical `/study-notes/` route; COMP6713 will be added as a separate course subtree to minimize migration risk.
- The existing Resources compatibility page can become the public course selector without changing its URL.
- A text-first presentation is acceptable unless an image or diagram is both useful and clearly publishable.

## Acceptance criteria

### Discovery, ownership, and privacy

- **AC-001:** Codex produces a private inventory of the COMP6713 material it inspected, including format, proposed module grouping, authorship/ownership status, assessment risk, and publication recommendation.
- **AC-002:** Every proposed public module and asset is explicitly approved by Bryan before it enters the public repository.
- **AC-003:** No OneDrive path, private URL, raw evidence file, restricted assessment material, official course material, third-party personal data, or unapproved excerpt appears in GitHub, PR comments, screenshots, or built output.
- **AC-004:** Excluded and uncertain material is recorded privately and omitted rather than guessed, paraphrased without authority, or silently published.

### Published notes

- **AC-005:** `/study-notes/comp6713/` provides a clear course-notes introduction, personal-notes disclaimer, and semantic module navigation.
- **AC-006:** Each approved module page preserves the approved substance and ordering, has a descriptive title, sensible heading hierarchy, and navigation back to the COMP6713 index.
- **AC-007:** Code blocks, tables, mathematical notation, citations, diagrams, and long technical content render legibly without page overflow; copied or externally derived material is attributed only when publication is permitted.
- **AC-008:** The Resources compatibility page links clearly to both ACTL3162 and COMP6713, while all existing ACTL3162 routes and representative deep links continue to resolve.

### Quality and maintainability

- **AC-009:** New notes use the existing shared design system, metadata structure, favicon, focus styles, and responsive navigation without a parallel framework or duplicated site shell.
- **AC-010:** New and changed pages work at 360 px, 768 px, and 1440 px; all links and controls are keyboard operable and visibly focusable; representative pages have no browser-console error.
- **AC-011:** Jekyll build, site checker, nine existing tests, syntax/configuration checks, zero-exemption policy, source-only `_site` assertion, required-route checks, and PR validation CI all pass.
- **AC-012:** README or nearby maintenance documentation explains the COMP6713 source structure, how to add or edit modules, the publication-eligibility boundary, and Bryan-owned merge/publication.
- **AC-013:** Bryan explicitly approves the final published COMP6713 content and representative visual evidence before the project receives PASS.
- **AC-014:** Work is delivered on a non-default branch through a draft pull request; Codex and the Project Director do not merge or deploy.

## Final quality gates

1. The private discovery packet is delivered directly to Bryan and does not enter GitHub.
2. Bryan approves the exact module set, public copy, links, and assets before implementation.
3. `bundle exec jekyll build --trace` succeeds with the supported Ruby/Bundler environment.
4. `python3 scripts/check_site.py _site` reports zero broken internal references and zero exemptions.
5. `python3 -m unittest discover -s tests -v` passes.
6. JavaScript syntax, Python compilation, YAML configuration, forbidden-content scans, and `git diff --check` pass.
7. `test -z "$(git ls-files _site)"` passes.
8. `/study-notes/comp6713/`, every approved COMP6713 module, `/pages/study-notes.html`, `/study-notes/`, and representative ACTL3162 deep links build non-empty.
9. COMP6713 index and representative modules pass responsive, keyboard, MathJax/code-overflow, metadata, and browser-console checks.
10. Exact-head pull-request CI passes.
11. Bryan approves the final factual content and visual presentation.
