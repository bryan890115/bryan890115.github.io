# Codex Implementation Status

Protocol version: 1
Directive ID: D-0004
Milestone ID: M-003
State: READY_FOR_REVIEW
Branch: `agent/professional-portfolio-redesign`
Starting SHA: `6b13762deb86e5184538740a673a51cd6ac00417`
Implementation commit SHA: `812c41dcd836b67a626b69677d2a67088b1ed651`
Updated at: `2026-08-03T14:17:29Z`

## Completed work

- Replaced the unsupported About biography, expertise, financial-services
  positioning, generic self-praise, inline styles, and portrait with a complete
  text-first profile.
- Structured About as four semantic articles covering current research, the
  approved Computer Science and Actuarial Studies background, the five accepted
  project areas, and capabilities directly evidenced by accepted public pages and
  repository source.
- Replaced Contact's consulting offers, collaboration and availability statements,
  response-time promise, networking and mentorship claims, marketing-style mailto,
  inline styles, and portrait with a neutral text-first channel list.
- Contact now exposes exactly the approved email, GitHub account, and the LinkedIn
  URL Bryan explicitly added in his current instruction. No LinkedIn profile content
  was inspected, copied, or inferred.
- Normalized the `/pages/study-notes.html` compatibility page to the shared semantic
  hero and button system while preserving its link to the canonical `/study-notes/`
  route. Canonical note content was not rewritten.
- Removed the final Contact exemption from `site-check.json` and changed the
  repository-policy regression test to require zero exemptions.
- Preserved the accepted Research and Projects pages, the existing design system,
  all privacy boundaries, and tracked generated `_site/` files.

## Files changed

- `.project-loop/STATUS.md`
- `pages/about.html`
- `pages/contact.html`
- `pages/study-notes.html`
- `site-check.json`
- `tests/test_check_site.py`

No CSS, JavaScript, Research, Projects, canonical study-note, portrait asset, or
generated-site source was changed. The portrait asset and shared legacy portrait CSS
remain because the canonical study-note landing page still uses them; About and
Contact contain no portrait reference.

## Acceptance and claim evidence

- **AC-002:** The exact forbidden-copy scan returned no match across `index.html`,
  `pages`, `_layouts`, and `_includes`. About and Contact contain no placeholder,
  consulting, availability, response-time, networking, mentorship, or generic
  marketing copy.
- **AC-006:** The About hero uses the positioning approved in `SPEC.md`. The current
  research statement maps to the accepted `pages/research.html`. The five named
  experience areas and their methods map to the accepted `pages/projects.html`.
  Python, Brick, SPARQL, machine-learning/data workflows, Markdown, Jekyll, and
  MathJax are expressly permitted by D-0004 and evidenced by accepted pages or
  repository source. No institution, date, mark, employment, teaching appointment,
  credential, location, collaborator, publication, or award was added.
- **AC-007:** Email `bryan890115@gmail.com` and GitHub
  `https://github.com/bryan890115` map to the approved specification and D-0004.
  LinkedIn `https://www.linkedin.com/in/bryan-c-jen-0604a311b/` maps only to Bryan's
  explicit instruction during implementation. The page makes no response or
  availability promise and contains no form or prefilled inquiry.
- **AC-008:** Both pages reuse the established hero, section-heading, cards-grid,
  card-item, and card-link system. No page-specific style or new CSS was needed.
- **AC-009:** About and Contact were checked at 360, 768, and 1440 CSS pixels. Each
  viewport had `scrollWidth == clientWidth`, zero overflowing elements, zero
  overlapping cards, and non-empty main content.
- **AC-010:** Each scoped page has labelled regions and hierarchical headings. Every
  content interaction is a visible native anchor with `tabIndex=0`, no disabled
  state, and automatic shared focus styling. At 360 and 768 pixels the compact Menu
  changed `aria-expanded` and navigation state to `true`, closed with Escape, restored
  focus to `#nav-toggle`, and showed a solid three-pixel focus outline. Desktop
  navigation was visible and the Menu hidden at 1440 pixels.
- **AC-014:** The build and browser checks confirmed non-empty
  `/pages/about.html`, `/pages/contact.html`, `/pages/study-notes.html`,
  `/study-notes/`, and `/study-notes/notes/mod0.html` routes. The checker validated
  all 15 built HTML files and 227 references.

## Authority checks

```text
git merge-base --is-ancestor c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157 "$STARTING_SHA"
Exit 0; no output.

git diff --name-only c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157..."$STARTING_SHA"
.project-loop/DIRECTIVE.md
.project-loop/PLAN.md
.project-loop/REVIEW.md
```

The starting branch therefore contained only the three Director-owned changes
permitted by D-0004 after its base SHA.

## Validation

```text
bundle exec jekyll build --trace
Exit 1 under the default macOS Ruby 2.6 launcher: Bundler 2.5.23 was unavailable.

/opt/homebrew/Cellar/ruby@3.4/3.4.10/bin/bundle _2.5.23_ exec jekyll build --trace
Exit 0 using the directive-permitted Ruby 3.4 launcher and the existing ignored
local gem cache; generated successfully in 0.369 seconds. No network installation or
dependency change was made.

python3 scripts/check_site.py _site
Exit 0; 15 HTML files, 227 references, and 0 exemptions applied.

python3 -m unittest discover -s tests -v
Exit 0; 9 tests passed in 0.163 seconds, including
`test_repository_config_has_no_exemptions`.

node --check assets/js/script.js
Exit 0; no output.

python3 -m compileall scripts
Exit 0; both Python modules compiled.

D-0004 exact forbidden-copy negative grep
Exit 0; no matches.

D-0004 exact About/Contact portrait-reference negative grep
Exit 0; no matches.

ruby -e 'required=%w[_site/pages/about.html _site/pages/contact.html _site/pages/study-notes.html _site/study-notes/index.html _site/study-notes/notes/mod0.html]; required.each { |f| abort("missing or empty: #{f}") unless File.file?(f) && File.size(f) > 0 }; puts "required routes non-empty"'
Exit 0; `required routes non-empty`.

git diff --check
The first post-build run detected trailing whitespace in generated `_site/index.html`.
After the required validation and browser checks, tracked `_site/` was restored rather
than edited or committed. The final run exited 0 with no output.
```

The built About and Contact pages produced no browser-console warnings or errors at
any required width. DOM and visual checks found no portrait, inline style, clipping,
overlap, or horizontal overflow. Contact's three main-content links exactly matched
the email, GitHub, and user-approved LinkedIn destinations. The compatibility,
canonical, and representative note routes each loaded with their expected title and
heading and no console warning or error.

## Checker scope

`site-check.json` now contains `"exemptions": []`. The repository-policy test asserts
`config.exemptions == ()`, so any future page-specific exception fails the test. The
generic checker tests for exact, auditable exemptions remain intact.

## Deviations and risks

- Bryan's latest instruction explicitly added
  `https://www.linkedin.com/in/bryan-c-jen-0604a311b/` after D-0004 had limited
  Contact to email and GitHub. This is the only content-scope deviation. It is
  confined to one neutral Contact link, is recorded for Director review, and does
  not introduce any inferred LinkedIn fact or broader social/profile integration.
- The default Ruby/Bundler launcher remains incompatible with the pinned Bundler
  version. The already installed Ruby 3.4 launcher and existing ignored local gem
  cache produced the successful build.
- Browser evidence is local rather than attached CI evidence; CI remains assigned to
  M-004.

## Blockers

None.

## Review focus

- Factual restraint and source mapping across all four About articles.
- Acceptance of Bryan's explicit LinkedIn addition as the only deviation from the
  originally issued two-channel Contact list.
- Complete removal of About/Contact portrait and marketing content.
- Exact three-link Contact boundary, zero checker exemptions, and route preservation.
- Responsive layout, compact-navigation focus restoration, and absence of console
  errors.
