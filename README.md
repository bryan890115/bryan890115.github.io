# Bryan Jen portfolio

This repository contains the source for Bryan Jen's Jekyll-based portfolio at
[bryan-c-jen.au](https://bryan-c-jen.au). The site uses shared Liquid layouts and
includes, local CSS, and minimal vanilla JavaScript.

## Prerequisites

- Ruby 3.1 or newer
- Bundler 2.5.23, as pinned in `Gemfile.lock`
- Python 3.10 or newer
- Node.js for the JavaScript syntax check

The macOS system Ruby at `/usr/bin/ruby` is version 2.6 on many installations and
cannot load the pinned Bundler. Use a supported Ruby from a version manager or
Homebrew, then confirm that `ruby`, `gem`, and `bundle` resolve from the same
toolchain and that `ruby --version` reports 3.1 or newer before installing Bundler
2.5.23. Do not update `Gemfile.lock` merely to accommodate system Ruby.

## Install, build, and preview

Install the locked Ruby dependencies and build the static site:

```bash
gem install bundler -v 2.5.23
bundle install
bundle exec jekyll build --trace
```

To preview the source locally:

```bash
bundle exec jekyll serve
```

Open `http://127.0.0.1:4000`. The generated site is written to `_site/`.

## Complete validation

Run these checks from the repository root after installing dependencies:

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
! grep -RniE 'SITE UNDER CONSTRUCTION|Placeholder|More details coming soon|Coming Soon|future deep dives|documented later|Typically within 24-48 hours|Consulting Available|Open to consulting opportunities|Available for consulting opportunities|Available for consulting engagements|consulting services|Open to professional inquiries and collaboration discussions|© 2024' index.html pages _layouts _includes
ruby -e 'required=%w[_site/index.html _site/pages/research.html _site/pages/projects.html _site/pages/about.html _site/pages/contact.html _site/pages/study-notes.html _site/study-notes/index.html _site/study-notes/notes/mod0.html]; required.each { |f| abort("missing or empty: #{f}") unless File.file?(f) && File.size(f) > 0 }; puts "release routes non-empty"'
git diff --check
```

`scripts/check_site.py` validates generated internal page, asset, and fragment links
and scans HTML for the phrases configured in `site-check.json`. Repository policy
requires zero page-specific exemptions.

## Source layout

- `_layouts/default.html` provides the shared document and main-content shell.
- `_includes/` contains shared metadata, navigation, and footer markup.
- `_config.yml` stores site-wide identity, URL, author, and Markdown settings.
- `index.html` is the home-page source.
- `pages/` contains Research, Projects, About, Contact, and compatibility pages.
- `study-notes/` contains the canonical study-note landing page and note sources.
- `assets/css/` and `assets/js/` contain the shared visual system and navigation code.
- `scripts/check_site.py`, `site-check.json`, and `tests/` provide validation.

## Editing content and metadata

Edit public content only in its source file:

- Home: `index.html`
- Research: `pages/research.html`
- Projects: `pages/projects.html`
- About: `pages/about.html`
- Contact: `pages/contact.html`
- Study-note compatibility page: `pages/study-notes.html`
- Canonical study notes: `study-notes/index.html` and `study-notes/notes/`

Each primary page's front matter supplies its title and description. Shared
canonical, Open Graph, and Person JSON-LD markup lives in `_includes/head.html` and
uses values from `_config.yml`. Change verified identity, contact, or profile data
only with Bryan's explicit approval. In particular, the approved LinkedIn contact
link is not approved for inclusion in JSON-LD.

Preserve existing public routes and use Jekyll's `relative_url` or `absolute_url`
filters for internal and canonical links. Rebuild and run the complete validation
suite after every content, layout, asset, or metadata change.

## Generated-output policy

`_site/` is reproducible build output, not source. It is ignored by Git, must contain
no tracked files, and must never be hand-edited or committed. Local gem directories,
caches, coverage, browser-test reports, and Lighthouse scratch output are also
ignored. Curated release screenshots belong under `docs/review/`; Jekyll excludes
that directory from the public build while GitHub keeps the evidence reviewable in
the pull request.

## Pull-request validation

`.github/workflows/validate.yml` runs on pull requests and optional manual dispatch.
It checks out the exact validation head with persisted credentials disabled,
installs the
locked Ruby dependencies, builds the site, and runs the checker, tests, syntax,
configuration, generated-output, zero-exemption, and forbidden-copy policies.

The workflow has read-only repository permission. It does not use secrets, push
commits, comment, deploy to GitHub Pages, or modify repository settings.

## Merge and publication ownership

Bryan owns final factual and visual approval, merging, and publication. This
repository deliberately contains no deployment workflow. After approving a release
candidate, Bryan may merge it and publish through the repository's configured GitHub
Pages source. Contributors and validation automation must not merge, deploy, push to
`main`, or alter Pages settings on Bryan's behalf.
