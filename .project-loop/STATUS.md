# Codex Implementation Status

Protocol version: 1
Directive ID: D-0001
Milestone ID: M-001
State: READY_FOR_REVIEW
Branch: `agent/professional-portfolio-redesign`
Starting SHA: `ad5b3549917699ff225e94ff2d83aa8e7f9282b8`
Final implementation SHA: `e147a2a744556f08ce65c347b9bca0ccfd4170c6`
Updated at: `2026-08-03T08:27:09Z`

## Implemented work

- Added a shared Jekyll shell with reusable head metadata, header/navigation, footer,
  skip link, semantic main landmark, current-page navigation state, and versioned local
  CSS/JavaScript assets.
- Rebuilt the home page around the approved MPhil research positioning, with a concise
  introduction, current focus, selected work, capabilities, and a direct email action.
- Added a restrained responsive design system with local system fonts, reusable tokens,
  cards, buttons, focus states, a compact navigation breakpoint, print rules, and
  `prefers-reduced-motion` support.
- Added a progressively enhanced mobile navigation controller. With JavaScript disabled,
  the navigation remains visible; with JavaScript enabled, the menu exposes
  `aria-expanded`, closes on link selection or Escape, and restores focus after Escape.
- Migrated the primary and compatibility pages to the shared layout while preserving
  their existing source content and URLs. Final rewrites of those pages remain assigned
  to M-002 and M-003.
- Added canonical, Open Graph, and verified Person JSON-LD metadata from central site
  configuration.
- Added reproducible build instructions, a Python-standard-library site checker, a narrow
  checker policy file, and nine checker unit tests.
- Removed the unused Minima theme dependency, added Ruby former-standard-library
  compatibility gems, and locked both macOS and Linux gem platforms.
- Left tracked `_site/` output unchanged, as required by the M-001 scope.

## Files changed

Implementation commit changes 23 files:

- Build and documentation: `.gitignore`, `Gemfile`, `Gemfile.lock`, `README.md`,
  `_config.yml`.
- Shared shell: `_layouts/default.html`, `_includes/head.html`,
  `_includes/header.html`, `_includes/footer.html`.
- Design and behaviour: `assets/css/professional.css`, `assets/js/script.js`.
- Home and compatibility sources: `index.html`, `pages/about.html`, `pages/books.html`,
  `pages/contact.html`, `pages/projects.html`, `pages/research.html`,
  `pages/study-notes.html`, `study-notes/index.html`.
- Validation: `scripts/__init__.py`, `scripts/check_site.py`, `site-check.json`,
  `tests/test_check_site.py`.

No Director-owned file other than this Codex-owned `STATUS.md` was changed. No generated
`_site/` file is present in the implementation diff.

## Acceptance evidence

- **AC-001:** `index.html` has one H1 stating the approved current role, research focus,
  and Computer Science/Actuarial Studies background. `SITE UNDER CONSTRUCTION` is absent
  from built public HTML.
- **AC-003:** The built home page contains the introduction, current-focus, selected-work,
  capability, and contact sections; the primary email and selected-work actions are
  native links.
- **AC-008 / AC-013:** All required primary routes render the same header, navigation,
  main landmark, footer, metadata include, CSS, and JavaScript through
  `_layouts/default.html` and `_includes/`.
- **AC-009:** Browser measurements reported `scrollWidth == innerWidth` at 360, 768, and
  1440 px. The 360 and 768 px states use the compact menu; 1440 px uses the desktop nav.
- **AC-010:** The built route tree exposes one H1 and one header/main/footer on every
  required route. The skip link is the first interactive element, targets
  `#main-content`, and the main landmark has `tabindex="-1"`. Shared CSS supplies visible
  `:focus-visible` and skip-link focus states. The mobile menu opened with
  `aria-expanded="true"`; Escape closed it, hid the nav, and returned focus to
  `#nav-toggle`. Primary calls to action are native `<a>` elements with real `mailto:`
  and checked fragment targets. Reduced-motion rules disable animation and smooth scroll.
- **AC-015:** The built home page has the title
  `MPhil researcher in semantic building data | Bryan Jen`, the approved description,
  `https://bryan-c-jen.au/` canonical URL, Open Graph fields, and Person JSON-LD.
- **AC-016:** `README.md` documents install, build, preview, validation, and source layout.
  `scripts/check_site.py` checks case-sensitive internal page, asset, directory-index,
  same-origin, `data-href`, and fragment targets plus forbidden text.

### Built routes

The isolated final build produced non-empty files for every required route:

| Route | Built file | Bytes |
| --- | --- | ---: |
| `/` | `_site/index.html` | 8,469 |
| `/pages/about.html` | `_site/pages/about.html` | 7,470 |
| `/pages/projects.html` | `_site/pages/projects.html` | 19,796 |
| `/pages/research.html` | `_site/pages/research.html` | 10,713 |
| `/pages/contact.html` | `_site/pages/contact.html` | 6,774 |
| `/study-notes/` | `_site/study-notes/index.html` | 9,301 |

At 360 px, browser inspection of all six routes found one H1, one header, one main, one
footer, the skip-link target, and no horizontal overflow on every route. The browser
console contained no warnings or errors.

### Visual evidence

- 360 px: `outputs/home-360.jpg` — compact header, stacked hero/actions, no overflow.
- 768 px: `outputs/home-768.jpg` — compact menu at the boundary, stacked research card,
  no overflow.
- 1440 px: `outputs/home-1440.jpg` — desktop navigation and two-column editorial hero,
  no overflow.

### Factual claims and approved sources

| Home-page claim | Approved source |
| --- | --- |
| Bryan is an MPhil researcher working on natural-language interfaces for semantic building data, with a Computer Science and Actuarial Studies background. | Approved positioning in `.project-loop/SPEC.md`, lines 23-27. |
| Public email is `bryan890115@gmail.com`. | `.project-loop/SPEC.md`, line 57. |
| Public GitHub account is `bryan890115`. | `.project-loop/SPEC.md`, line 58, plus the repository named in D-0001. |
| Public ACTL3162 General Insurance Techniques notes exist. | Existing `study-notes/` source and the successfully checked `/study-notes/` route. |
| Canonical site host is `bryan-c-jen.au`. | Existing repository `CNAME`. |

No project outcome, employment, publication, availability, response-time, or research-result
claim was added to the home page.

## Validation

Required commands and final outcomes:

```text
/opt/homebrew/opt/ruby@3.4/bin/bundle _2.5.23_ install
Bundle complete! 5 Gemfile dependencies, 35 gems now installed.

/opt/homebrew/opt/ruby@3.4/bin/bundle _2.5.23_ exec jekyll build --trace
Generating... done in 0.138 seconds. Exit 0.

python3 scripts/check_site.py _site
Site check passed: 15 HTML file(s), 234 reference(s), 30 exemption(s) applied.

ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
config ok

git diff --check
Exit 0; no output.

git status --short
Clean after implementation commit; this STATUS-only evidence update is the sole subsequent change.
```

The build and site-check commands ran from an isolated copy at
`/tmp/bryan-site-validation.hgpdBH` with the committed source and installed bundle. This
protects the tracked legacy `_site/` tree while executing the exact build/checker workflow.

Additional checks:

```text
python3 -m unittest discover -s tests -v
Ran 9 tests in 0.042s — OK.

node --check assets/js/script.js
Exit 0; no output.

Browser console warnings/errors
[]
```

## Deviations

- The required Ruby commands used the absolute Ruby 3.4/Bundler 2.5.23 executable because
  the host default Ruby 2.6 cannot run the locked Jekyll toolchain. Command semantics and
  arguments are otherwise identical to D-0001.
- The build ran in an isolated source copy instead of the repository root so M-001 could
  validate source reproduction without modifying tracked `_site/`; D-0001 explicitly
  defers removal of tracked generated output to M-004.
- `site-check.json` contains exact-path, exact-phrase exemptions only for legacy projects
  and research copy deferred to M-002 and contact availability copy deferred to M-003.
  Every applied exemption is printed; the home page has none.
- A cache-busting asset revision was added after the 768 px breakpoint fix exposed a stale
  browser stylesheet during QA.

## Risks

- Legacy about, projects, research, contact, books, and study-note copy and imagery remain
  pending their approved M-002/M-003 rewrites. The checker makes the known placeholder and
  availability debt visible rather than silently accepting it.
- End-to-end Lighthouse thresholds are a final project quality gate and were not part of
  the acceptance criteria mapped to D-0001.
- The browser automation runtime did not reliably synthesize the initial Tab/Enter sequence
  after a page reload. Skip-link and CTA keyboard support is evidenced by native semantics,
  focus styling, verified targets, and built DOM; the menu Escape path was exercised
  end-to-end. A human keyboard pass remains appropriate during Pro review.
- Bryan must review all changed public content before merge. No merge or deployment has
  been performed.

## Blockers

None.

## Review focus

- Truthfulness and distinctiveness of the approved home-page positioning.
- Editorial visual system and compact navigation at the 768 px boundary.
- Shared Jekyll shell, metadata consistency, and route preservation.
- Accessibility semantics, visible focus, and the human keyboard pass noted above.
- Whether the narrow M-002/M-003 checker exemptions clearly expose deferred content debt.
