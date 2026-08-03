# Bryan Jen portfolio

This repository contains the source for Bryan Jen's Jekyll-based portfolio at
[bryan-c-jen.au](https://bryan-c-jen.au). The site uses shared Liquid layouts and
includes, local CSS, and minimal vanilla JavaScript.

## Prerequisites

- Ruby 3.1 or newer
- Bundler 2.5.23
- Python 3.10 or newer for site validation

## Install and build

```bash
bundle install
bundle exec jekyll build --trace
```

The generated site is written to `_site/`. Generated files are validation output,
not source, and should not be edited directly.

To preview locally:

```bash
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000`.

## Validate

After building, run:

```bash
python3 scripts/check_site.py _site
python3 -m unittest discover -s tests -v
ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
git diff --check
```

The checker validates internal page, asset, and fragment links and scans generated
HTML for configured forbidden phrases. Its phrase policy is stored in
`site-check.json`; any temporary milestone exemption must name an exact generated
path and phrase so deferred content remains visible in validation output.

## Site structure

- `_layouts/` and `_includes/` contain the shared page shell and metadata.
- `index.html` is the home-page source.
- `pages/` contains the public portfolio pages.
- `study-notes/` contains the study-note index and Markdown notes.
- `assets/` contains local styles, scripts, and images.
- `scripts/check_site.py` validates the generated site.

Edit source files, rebuild, and run the validation commands before proposing a
change. Existing public URLs should remain stable.
