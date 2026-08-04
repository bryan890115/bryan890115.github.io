# Codex Implementation Status

Protocol version: 1
Directive ID: D-0005
Milestone ID: M-004
State: READY_FOR_REVIEW
Release verdict: BLOCKED_PENDING_BRYAN_APPROVAL
Branch: `agent/professional-portfolio-redesign`
Starting SHA: `462a886edafdb73ef340ff8eefce5a24127ded0d`
Implementation commit SHA: `8977621acf31c457c94989ba7353e3bf13ba82a3`
Final review head SHA: PENDING_EVIDENCE_COMMIT
Bryan factual-content approval: PENDING
Bryan visual approval: PENDING
Updated at: `2026-08-03T15:29:18Z`

## Completed work

- Proved that the accepted source reproduced before removing generated output,
  then removed all 17 tracked `_site/` files. `_site/` remains ignored and is
  rebuilt only from source.
- Added the PR-only, read-only `Validate site` workflow. It installs the locked
  Ruby dependencies, builds Jekyll, and enforces the checker, nine tests, source
  syntax, configuration, route, zero-exemption, generated-output, and forbidden-copy
  gates. It has no push, deployment, secret, comment, schedule, or
  repository-write capability.
- Expanded README maintenance, validation, metadata, generated-output, CI, merge,
  and publication guidance. Curated review screenshots are stored under
  `docs/review/` and excluded from the public Jekyll build.
- Removed three demonstrably unreferenced legacy source assets while preserving the
  profile image still used by the canonical study-note landing page.
- Added a local SVG favicon, converted the six click-only study-module cards to
  native links, sized and lazy-loaded the canonical study-note portrait, contained
  narrow-screen display mathematics, and gave keyboard-focusable MathJax output the
  shared three-pixel focus treatment.
- Preserved all accepted public Research, Projects, About, Contact, home, and note
  copy. Contact still contains exactly the approved email, GitHub, and LinkedIn
  channels. LinkedIn remains absent from Person JSON-LD, and no LinkedIn-derived
  information was added.

## Changed-file inventory

### Generated output removed

- All 17 previously tracked paths under `_site/`

### Validation and policy

- `.github/workflows/validate.yml`
- `.gitignore`

### Documentation and review evidence

- `README.md`
- `_config.yml`
- `docs/review/d0005/about-1440.jpg`
- `docs/review/d0005/contact-360.jpg`
- `docs/review/d0005/home-360.jpg`
- `docs/review/d0005/home-1440.jpg`
- `docs/review/d0005/projects-360.jpg`
- `docs/review/d0005/projects-1440.jpg`
- `docs/review/d0005/research-360.jpg`
- `docs/review/d0005/research-1440.jpg`

### Bounded release fixes

- `_includes/head.html`
- `assets/css/professional.css`
- `assets/images/favicon.svg`
- `study-notes/index.html`

### Unreferenced legacy assets removed

- `assets/images/love-picture.jpg`
- `assets/images/modal-project.svg`
- `assets/images/modal-research.svg`

## Authority checks

```text
git merge-base --is-ancestor e9a4dbba3ec2a06beffb49237e67f3f920226ae1 "$STARTING_SHA"
Exit 0; no output.

git diff --name-only e9a4dbba3ec2a06beffb49237e67f3f920226ae1..."$STARTING_SHA"
.project-loop/DECISIONS.md
.project-loop/DIRECTIVE.md
.project-loop/PLAN.md
.project-loop/REVIEW.md
```

The starting branch therefore contained only the four Director-owned changes
permitted by D-0005 after its base SHA.

## Source reproduction and generated-output evidence

Before untracking `_site/`, the supported Ruby 3.4/Bundler 2.5.23 launcher ran
`jekyll build --trace` successfully. The checker then passed 15 HTML files and 227
references with zero exemptions, and every required route was non-empty.

After untracking `_site/`, a clean Jekyll build reproduced the site. The final build
contains 15 HTML files and 242 validated references; the additional 15 references
are the shared favicon on each generated page. `git ls-files _site` returns no path,
and `_site/docs/review` is absent because review evidence is excluded from Jekyll.

## Final local validation

The literal `bundle install` command exited 1 because `/usr/bin/bundle` invokes the
macOS Ruby 2.6 RubyGems environment and cannot load the lockfile's Bundler 2.5.23.
No dependency was changed. The directive-permitted compatible launcher was used:

```text
/opt/homebrew/Cellar/ruby@3.4/3.4.10/bin/bundle _2.5.23_ install
Exit 0; 5 Gemfile dependencies and 35 gems installed in ignored vendor/bundle.

/opt/homebrew/Cellar/ruby@3.4/3.4.10/bin/bundle _2.5.23_ exec jekyll build --trace
Exit 0; generated successfully in 0.054 seconds.

python3 scripts/check_site.py _site
Exit 0; 15 HTML files, 242 references, 0 exemptions.

python3 -m unittest discover -s tests -v
Exit 0; all 9 tests passed in 0.031 seconds.

node --check assets/js/script.js
Exit 0; no output.

python3 -m compileall scripts
Exit 0; scripts compiled.

ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
Exit 0; config ok.

test -z "$(git ls-files _site)"
Exit 0; no tracked generated output.

D-0005 zero-exemption assertion
Exit 0; zero exemptions.

D-0005 exact forbidden-copy negative grep
Exit 0; zero matches.

D-0005 exact required-route assertion
Exit 0; release routes non-empty.

git diff --check
Exit 0; no output.
```

## Route, link, and metadata results

- `/`, all five `/pages/*.html` portfolio routes, `/study-notes/`, the compatibility
  route, and `/study-notes/notes/mod0.html` returned non-empty local content.
- The checker validated all internal pages, assets, fragments, same-origin absolute
  URLs, and representative deep links.
- GitHub profile, portfolio study-note tree, and COMP9417 links returned HTTP 200.
- The MathJax CDN asset returned HTTP 200.
- Scripted LinkedIn access returned HTTP 999 at the exact approved URL. This is an
  anti-automation response rather than a substituted URL; no LinkedIn content was
  copied, inferred, or saved.
- The configured production domain serves content only when TLS certificate
  verification is bypassed; normal HTTPS verification currently reports a hostname
  mismatch. The source canonical value was frozen and was not changed. This is a
  pre-existing custom-domain/Pages publication risk that Bryan must resolve outside
  this no-settings, no-deployment directive.
- Each primary page has one H1, header/nav/main/footer landmarks, no heading-level
  jump, a non-empty title and description, matching canonical and Open Graph URL,
  and shared Person JSON-LD containing only the approved name, email, and GitHub
  identity. LinkedIn is not present in JSON-LD.
- Contact main content exposes exactly:
  `mailto:bryan890115@gmail.com`, `https://github.com/bryan890115`, and
  `https://www.linkedin.com/in/bryan-c-jen-0604a311b/`. It contains no portrait.

## Responsive, console, and keyboard QA

- Home, Research, Projects, About, Contact, and the study-note landing page were
  checked at 360, 768, and 1440 CSS pixels. All 18 combinations had no horizontal
  page overflow, clipped or overlapping cards, heading jumps, missing landmarks,
  or unreadable navigation state.
- The representative note was separately checked at 360 pixels after the generic
  MathJax containment fix: `scrollWidth == innerWidth == 360`, with no overflowing
  display-math container.
- Primary and representative note routes produced no browser-console warning or
  error after the local favicon fix.
- Trusted keyboard input activated the skip link and moved focus to `main`; traversed
  every desktop navigation and scoped page control; opened the compact menu; closed
  it with Escape; restored focus to the Menu button; activated the home fragment CTA,
  Resources compatibility link, and representative module link; and traversed the
  keyboard-focusable MathJax expressions. Every tested focus target displayed the
  shared three-pixel solid outline.

## Lighthouse

Lighthouse 12.8.2 ran against the final local build in Chrome 151. Scores are
Performance / Accessibility / Best Practices / SEO:

| Route | Scores |
| --- | --- |
| `/` | 100 / 100 / 100 / 100 |
| `/pages/research.html` | 100 / 100 / 100 / 100 |
| `/pages/projects.html` | 94 / 100 / 100 / 100 |
| `/pages/about.html` | 100 / 100 / 100 / 100 |
| `/pages/contact.html` | 100 / 100 / 100 / 100 |
| `/study-notes/` | 100 / 100 / 100 / 100 |

All six runs passed the D-0005 thresholds. Each final report also recorded passing
`errors-in-console` and `unsized-images` audits.

## Screenshot evidence

The eight versioned JPEG files under `docs/review/d0005/` have their declared CSS
viewport widths embedded in the filenames and matching pixel widths. They were
visually inspected after capture; the full-page Contact image shows all three exact
channels. Draft PR #11 embeds them using immutable raw URLs at implementation commit
`8977621acf31c457c94989ba7353e3bf13ba82a3`. The directory is excluded from the
generated public site.

## Pull-request validation

- Workflow: `Validate site`
- Draft PR: #11
- Successful implementation run: [#30827645460](https://github.com/bryan890115/bryan890115.github.io/actions/runs/30827645460)
- Successful run head: `8977621acf31c457c94989ba7353e3bf13ba82a3`
- Job/check: `Build and validate` (job ID `91733279586`)
- Conclusion: SUCCESS; checkout, Ruby setup, build, checker, nine tests,
  JavaScript, Python, configuration, tracked-output, zero-exemption,
  forbidden-copy, and route steps all succeeded.
- Resolved run [#30827344851](https://github.com/bryan890115/bryan890115.github.io/actions/runs/30827344851)
  failed before build because the original pinned `ruby/setup-ruby` commit did not
  support Ruby 3.4 on Ubuntu 24.04. It was replaced by current official `v1` commit
  `95ef2b042f9d7a56d8268cba8559e2842e2ad01b`.
- Resolved run [#30827493967](https://github.com/bryan890115/bryan890115.github.io/actions/runs/30827493967)
  passed every required D-0005 step but failed an extra base-to-head whitespace check
  on pre-existing Director Markdown hard breaks. The non-required extra step was
  removed; the exact local D-0005 `git diff --check` remained successful.

No ready-for-review transition, merge, deployment, main-branch push, or repository
settings change has been performed.

## Deviations, risks, and blockers

- Local installation and build used the directive-approved Ruby 3.4 launcher because
  the default `/usr/bin/bundle` is coupled to Ruby 2.6 and cannot load Bundler 2.5.23.
- LinkedIn's HTTP 999 response prevents a scripted 200 assertion; the exact approved
  URL is preserved and the limitation is recorded without importing profile content.
- The production custom domain's TLS hostname mismatch is outside this directive's
  source-only, no-settings boundary. Publication should not be approved until Bryan
  confirms or repairs the GitHub Pages/custom-domain configuration.
- The release candidate is complete, but the final project verdict remains blocked
  until Bryan explicitly approves both factual content and visual presentation.

## Self-review

- No D-0005 edit changes accepted factual copy or adds a contact/profile fact.
- The workflow is pull-request/manual only, read-only, credential-minimized, and
  contains no mutation or deployment mechanism.
- All removed source assets have zero source reference; the canonical study-note
  portrait remains present and validated.
- Screenshot files are review evidence, not generated-site content.
- Remaining work is publication evidence only: push this ledger update, wait for its
  exact-head PR validation, update draft PR #11, and request Bryan's two approvals.

## Review focus

- Confirm the exact three-channel Contact boundary and absence of LinkedIn-derived
  facts or LinkedIn JSON-LD.
- Review the eight attached responsive screenshots and the frozen public copy.
- Confirm `_site/` is source-reproducible and fully untracked.
- Confirm the workflow is safe, passing, and non-deploying.
- Decide how to resolve the production-domain TLS mismatch before publication.
- Obtain Bryan's explicit factual-content and visual approval.
