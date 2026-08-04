# Codex Implementation Status

Protocol version: 1
Directive ID: D-0003
Milestone ID: M-003
State: READY_FOR_REVIEW
Branch: `agent/comp6713-notes`
Starting SHA: `350d87a8613977c80c7d895a777f3a56267d3edd`
Correction and QA commit SHA: `acb8d211c86f4523a4b094f0b023ed09dfc413ee`
Updated at: `2026-08-04T03:49:28Z`

## Authority and scope

- The accepted D-0003 base `3681324c37d2876190c4fcc01cf2564ac422151e`
  is an ancestor of the starting SHA.
- Intervening files were limited to Director-owned `.project-loop/DIRECTIVE.md`,
  `.project-loop/PLAN.md`, and `.project-loop/REVIEW.md`.
- The approved title, disclaimer, nine-module set and order, routes, examples,
  factual scope, permanent exclusions, and design direction remain unchanged.
- Public changes are limited to the required attention terminology correction, a
  generic narrow-screen MathJax containment fix, and the required maintainer-policy
  wording clarification.

## Bounded correction and technical review

- Attention and Transformers now explains that self-attention without positional
  information is permutation-equivariant: reordering input tokens reorders the
  output vectors in the same way, so self-attention has no representation of token
  order by itself.
- The wording remains beginner-friendly and preserves the accepted surrounding
  explanation of fixed, learned, and relative position schemes.
- Per-module technical and mathematics reread: Foundations PASS; Representation
  Learning PASS; Attention and Transformers PASS after the required terminology
  fix; Modern Language Models PASS; Sentiment Analysis PASS; Sequence Tagging PASS;
  Machine Translation PASS; Summarisation and Question Answering PASS; NLP
  Applications and Responsible Deployment PASS.
- All nine executable examples remain accurately described, newly authored,
  standard-library-only, synthetic, deterministic, file/network/credential
  independent, and terminating within the checker timeout. The checker executed
  all nine examples twice successfully from fresh temporary working directories
  with Python's isolated-interpreter flag.
- README now describes that mechanism as a maintainership policy check, not an
  adversarial security sandbox.

## Private integrity review

- The final frozen public prose was compared with the 97 eligible candidate notes
  for normalized contiguous overlap of 12 or more words. Found: 0; resolved: 0;
  unresolved: 0.
- The broader conservative screen covered 133 Markdown files, 66 notebooks, and 21
  PDFs comprising 1,658 extracted pages. Found: 0 overlap runs of 12 or more words;
  extraction errors: 0; unresolved: 0.
- Structure review passed; the maximum consecutive exact heading match was one.
- Technical, mathematics, executable-code, citation/attribution, privacy, and
  assessment-integrity reviews all passed for 9/9 modules.
- No private source identity, path, link, excerpt, comparison, or audit artifact was
  added to Git or the generated site. No official, third-party, assessment,
  restricted, excluded, or source-similar material entered the public edition.

## Route, responsive, and interaction QA

- All ten COMP6713 routes rendered with exactly one H1, sensible heading order,
  shared header/navigation/main/footer landmarks, a non-empty title and description,
  matching canonical and Open Graph URLs, the shared favicon, valid JSON-LD, and no
  COMP6713-specific identity claim.
- All 30 COMP6713 route/viewport combinations passed at 360, 768, and 1440 px. Page,
  code, table, module-navigation, and MathJax containment passed with no clipping,
  overlap, or page-level horizontal overflow; compact and desktop navigation states
  were correct.
- One release-blocking 360 px overflow from a long inline equation was found and
  resolved with a generic scroll-contained inline MathJax rule. The complete
  30-case matrix passed after the correction.
- Keyboard and focus QA covered the shared skip link; all six desktop navigation
  links; compact Menu open, Escape close, and focus restoration; both course cards;
  all nine module cards; both index navigation links; all 25 module
  previous/index/next links; navigation after long code, table, and MathJax content;
  and all 75 focusable MathJax outputs. Required targets exposed a visible 3 px focus
  outline and every destination resolved correctly.
- `/pages/study-notes.html`, `/study-notes/`, `/study-notes/notes/mod0.html`, and
  `/study-notes/notes/mod5.html` remained present and usable; ACTL3162 source was not
  rewritten.
- Fresh browser-console checks covered the ten COMP6713 routes plus the four
  preserved selector/ACTL routes: 14/14 passed with zero warnings or errors.

## Review evidence

- Eight immutable screenshot files are committed under `docs/review/d0003/`: index
  at 360 and 1440 px; Foundations at 768 px; Attention at 360 and 1440 px; Sequence
  Tagging at 360 and 1440 px; and Responsible Deployment at 1440 px.
- The Attention evidence shows the corrected position-information explanation. The
  Foundations evidence shows narrow inline-math containment; Sequence evidence shows
  table and code containment.
- Screenshots contain only public page content and no local URL, private source,
  path, browser storage, developer tool, credential, or hidden audit material.
- `_config.yml` excludes `docs/review`, and a clean build confirmed that none of the
  review evidence is present in `_site`.

## Validation

- D-0003 ancestry and Director-handoff inventory: passed.
- Jekyll build: passed with 25 generated HTML pages.
- Generated-site checker: passed with 428 references and zero exemptions.
- COMP6713 checker: passed with 9 modules and 9 executable examples across 9
  modules.
- Unit tests: 17 passed.
- JavaScript syntax, Python compilation, YAML configuration, tracked-output,
  zero-exemption, exact-route, privacy syntax, external-link/asset, diff, and
  worktree checks: passed.
- The default system Bundler entrypoint could not load pinned Bundler 2.5.23. As
  permitted by D-0003, the build used
  `/opt/homebrew/Cellar/ruby@3.4/3.4.10/bin/bundle _2.5.23_` with the existing local
  dependency bundle whose lockfile matches this worktree. No dependency or lockfile
  changed.

## Pull request, exact-head CI, approval, and blockers

- Draft PR #13 remains the implementation pull request and must remain draft.
- The final status-bearing head and its exact `Validate site` workflow run/job IDs
  are recorded in the immutable PR update and readiness notification after this
  status commit is pushed; a commit cannot contain its own SHA or future workflow
  identity without changing that identity.
- Bryan factual-content approval: PENDING.
- Bryan visual-presentation approval: PENDING.
- Final project verdict remains blocked on Bryan explicitly providing both required
  approval lines. There are no known implementation blockers or residual technical
  risks within D-0003 scope.

## Review focus

- Precision and clarity of the permutation-equivariance correction.
- Visual review of the eight commit-pinned screenshots.
- Confirmation of the public-safe aggregate integrity, route, responsive,
  interaction, metadata, example, and exact-head CI evidence.
- Bryan's explicit factual-content and visual-presentation approval.
