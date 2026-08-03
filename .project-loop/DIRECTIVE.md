# Current Codex Directive

Directive ID: D-0001  
Status: ACTIVE  
Milestone ID: M-001  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`  
Issued timestamp: `2026-08-03T17:12:00+10:00`  
Activated timestamp: `2026-08-03T17:33:00+10:00`  
Replaced directive ID: None

## Approval

Bryan explicitly approved the specification and plan without corrections on 2026-08-03. D-0001 is active.

## Required outcome

Create the shared Jekyll design foundation and a complete, professional home-page vertical slice that presents Bryan as a research-focused computer scientist with an Actuarial Studies background. The site must remain buildable, responsive, accessible, and compatible with existing primary routes.

## In-scope work

1. Add a shared Jekyll page shell with reusable metadata, header/navigation, and footer includes.
2. Establish a restrained CSS design system with reusable variables, typography, spacing, layout, buttons, cards, focus states, reduced-motion support, and responsive behaviour.
3. Implement an accessible mobile navigation pattern without a framework.
4. Redesign the home page using the approved positioning in `.project-loop/SPEC.md`.
5. Remove `SITE UNDER CONSTRUCTION` from the home page.
6. Add semantic landmarks, a skip link, descriptive headings, visible focus states, and correct link/button semantics.
7. Add reusable title, description, canonical, Open Graph, and verified Person JSON-LD metadata support.
8. Add or update repository build instructions needed for this milestone.
9. Add `scripts/check_site.py` using the Python standard library to check built HTML for broken internal links and forbidden placeholder phrases.
10. Keep existing primary routes functional. Make only minimum compatibility edits outside the home page.
11. Update `.project-loop/STATUS.md` with exact evidence, commands, outputs, changed files, deviations, risks, and blockers.

## Explicitly out of scope

- Final rewriting of research, projects, about, contact, books, or study-note content.
- Publishing unverified project descriptions, metrics, credentials, employment, or research results.
- Adding a CMS, backend, contact form, analytics, tracking, advertisements, authentication, stock imagery, external fonts, or unnecessary third-party scripts.
- Migrating to React, Next.js, a CSS framework, or a JavaScript framework.
- Removing tracked `_site/` output before the source build is verified; that belongs to M-004.
- Merging to `main` or deploying the site.

## Mapped acceptance criteria

AC-001, AC-003, AC-008, AC-009, AC-010, AC-013, AC-015, and AC-016.

## Required evidence

- Exact starting and final implementation SHAs and a concise changed-file inventory.
- Successful output for every required validation command.
- Built-route evidence for `/`, `/pages/about.html`, `/pages/projects.html`, `/pages/research.html`, `/pages/contact.html`, and `/study-notes/`.
- Home-page visual evidence at 360 px, 768 px, and 1440 px.
- Keyboard-navigation evidence covering the skip link, navigation, and primary calls to action.
- A list of factual home-page claims and the approved source for each.
- Any deviation from the approved specification, with no silent scope expansion.

## Exact validation commands

```bash
bundle install
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
git diff --check
git status --short
```

## Publication permission

Codex may create `agent/professional-portfolio-redesign` from the current `main` after the approval commit is merged. The original base SHA remains valid because subsequent commits changed only project-loop metadata.

Codex may commit and push changes to that non-default branch and may open or update a draft pull request targeting `main`. Codex must not merge the pull request, push website implementation directly to `main`, or deploy the site.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- Approved positioning or factual copy is ambiguous or conflicts with evidence.
- A change would break an existing public route without an approved redirect.
- The Jekyll build cannot be reproduced without a material dependency or architecture change.
- A requested asset, link, credential, or claim cannot be verified.
- Work requires an explicitly excluded capability.
- Unrelated working-tree changes cannot be safely separated.
- The implementation code base has materially changed since the directive was issued.

## Next Project Director review focus

- Truthful and distinctive home-page positioning.
- Credible design without generic corporate decoration or claims.
- Shared Jekyll structure with preserved routes.
- Implemented accessibility and responsive behaviour.
- Traceable factual content.
- The smallest safe route to the approved outcome.
