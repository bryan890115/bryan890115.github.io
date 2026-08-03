# Codex Implementation Status

Protocol version: 1
Directive ID: D-0003
Milestone ID: M-002
State: READY_FOR_REVIEW
Branch: `agent/professional-portfolio-redesign`
Starting SHA: `3c63397a86e5f0a2260177650fec96136dc38e41`
Implementation commit SHA: `8b0ce3e35e210c10fd6f6b5096c9662542c0dafe`
Updated at: `2026-08-03T13:45:34Z`

## Completed work

- Replaced the generic research page with Bryan's approved MPhil summary, preserving
  the approved wording, punctuation, sentence order, status language, and no-link
  treatment.
- Replaced invented and placeholder project material with exactly five approved
  general-project cards in the approved order.
- Presented every project as a semantic article with its approved purpose,
  contribution, methods, outcome or learning, and public-link or no-link treatment.
- Preserved team attribution and conservative research, academic, and clinical
  caveats. Numerical metrics remain omitted.
- Removed the legacy click-only card behaviour, hidden placeholder details, modal
  markup, obsolete page scripts, invented business outcomes, and unused modal CSS.
- Retained the text-first asset decision; no project or research image was added.
- Removed only the completed research/project checker exemptions and strengthened
  the regression test so the single deferred contact-page exemption cannot broaden
  silently.
- Preserved the home page, primary navigation, research and project routes, and
  representative study-note routes.

## Files changed

- `.project-loop/STATUS.md`
- `assets/css/professional.css`
- `pages/projects.html`
- `pages/research.html`
- `site-check.json`
- `tests/test_check_site.py`

Tracked generated output in `_site/` was rebuilt for validation and then restored;
it is not part of this directive's change set.

## Acceptance and approval evidence

- **AC-002:** Removed repeated filler, placeholders, fake consulting language,
  invented business outcomes, and hidden future-detail copy from both scoped pages.
- **AC-004:** The research page contains the exact approved public summary. It makes
  no unapproved publication claim and links to no unpublished research material.
- **AC-005:** The project page contains exactly the approved five-card set, in this
  order: Iterative Query Planning for Building Knowledge Graphs; Histopathology Image
  Classification Pipeline; Air Quality Forecasting and Anomaly Detection;
  Fine-Grained Sentiment Analysis Across Product Domains; General Insurance Study
  Notes. Each card includes the approved purpose, contribution, methods, and outcome
  or learning.
- **AC-011:** Project entries are semantic `<article>` elements. The two approved
  project links are native anchors, are keyboard focusable, and show the shared
  three-pixel focus indicator. There are no research-page interactions and no modal.
- **AC-012:** The approved text-first treatment is retained, with no added image,
  copied evidence file, or third-party asset.
- **AC-014:** The built `/`, `/pages/research.html`, `/pages/projects.html`,
  `/study-notes/`, and `/study-notes/notes/mod0.html` outputs are present and
  non-empty. The site checker validated all 15 built HTML files and 225 references.

All factual research and project copy maps to the Bryan-approved D-0002 private
publication set recorded by DEC-001. The Air Quality card's approved repository and
the General Insurance Study Notes card's approved source location were independently
confirmed as public GitHub resources. The other three cards intentionally have no
public link. No numerical metric, source release, course-team code, report figure,
raw asset, or additional candidate was added.

No private source evidence, private path, raw file, private URL, internal or candidate
note, rejected candidate, uncertainty note, credential, third-party personal data, or
unapproved asset was copied, committed, built, or posted. No placeholder or
future-project card was added.

## Authority checks

```text
git merge-base --is-ancestor 3675b996628ff738ce9002b5c41a074a9cf5bc47 "$STARTING_SHA"
Exit 0; no output.

git diff --name-only 3675b996628ff738ce9002b5c41a074a9cf5bc47..."$STARTING_SHA"
.project-loop/DECISIONS.md
.project-loop/DIRECTIVE.md
.project-loop/PLAN.md
.project-loop/REVIEW.md
```

The pre-work diff therefore contains only the four Director-owned files permitted by
D-0003.

## Validation

```text
bundle exec jekyll build --trace
The unqualified system launcher uses Ruby 2.6 and could not load the repository's
Bundler 2.5.23. The final source was therefore built with the installed compatible
Ruby 3.4 launcher:

/opt/homebrew/Cellar/ruby@3.4/3.4.10/bin/bundle _2.5.23_ exec jekyll build --trace
Exit 0; generated successfully in 0.065 seconds.

python3 scripts/check_site.py _site
Exit 0; 15 HTML files, 225 references, and only 5 exact contact-page exemptions.

python3 -m unittest discover -s tests -v
Exit 0; 9 tests passed.

node --check assets/js/script.js
Exit 0; no output.

D-0003 exact placeholder-content negative grep
Exit 0; no matches.

D-0003 exact privacy-boundary negative grep
Exit 0; no matches.

ruby -e 'Dir["_site/**/*.html"].each { |f| abort("empty page: #{f}") if File.size(f) == 0 }; puts "html files non-empty"'
Exit 0; `html files non-empty`.

git diff --check
Exit 0; no output after restoring temporary `_site/` build changes.

git status --short --branch
Only the six intended D-0003 source, policy, test, and status files were present before
the final status commit; no generated or untracked file remained.
```

Responsive browser checks covered both scoped pages at 360, 768, and 1440 CSS pixels.
Neither page had horizontal overflow. Research retained one readable summary article;
projects retained five articles and changed from one column at 360/768 to two columns
at 1440. Both approved links were visible, enabled, correctly targeted, keyboard
focusable, and showed a solid three-pixel focus ring. Research and projects produced
no browser-console warnings or errors. Visual inspection found no clipping or overlap;
the mobile compact-heading spacing was adjusted before the final build.

## Checker scope

`site-check.json` now has exactly one exemption object: the unchanged
`pages/contact.html` exemption with its exact five deferred phrases. The research and
projects exemption objects were removed. The unit test asserts that exact remaining
scope, so future project/research placeholder copy cannot be exempted silently.

## Deviations and risks

- No implementation-scope deviation was required.
- The default macOS Ruby/Bundler launcher is incompatible with the repository's
  pinned Bundler version; the compatible installed Ruby 3.4 launcher produced the
  successful final build recorded above.
- Public copy remains deliberately conservative: metrics and assets are omitted,
  three projects have no link, and unpublished research has no output or source link.
- The final review head is the commit containing this status update and is reported
  in the PR's exact `CODEX_READY` notification, avoiding a self-referential SHA here.

## Blockers

None.

## Review focus

- Exact fidelity to the approved research summary and five-card order.
- Conservative contribution attribution and caveats.
- Intentional two-link/three-no-link treatment and absence of metrics or assets.
- Semantic structure, responsive layout, keyboard focus, and narrow checker scope.
- Absence of private evidence and all excluded material from repository and build.
