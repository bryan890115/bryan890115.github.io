# Current Codex Directive

Directive ID: D-0001  
Status: PENDING_APPROVAL  
Milestone ID: M-001  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`  
Issued timestamp: `2026-08-03T17:12:00+10:00`  
Replaced directive ID: None

## Required outcome

Create the shared Jekyll design foundation and a complete, professional home-page vertical slice that clearly positions Bryan as a research-focused computer scientist with an Actuarial Studies background. The site must remain buildable, responsive, accessible, and compatible with existing primary routes.

Codex must not begin this directive until Bryan approves the specification and plan and the Project Director changes this directive to `ACTIVE`.

## In-scope work

1. Add a shared Jekyll page shell with reusable metadata, header/navigation, and footer includes.
2. Establish a restrained CSS design system with reusable variables, typography, spacing, layout, buttons, cards, focus states, reduced-motion support, and responsive behaviour.
3. Implement an accessible mobile navigation pattern without a framework.
4. Redesign the home page using the exact positioning and content approved in `.project-loop/SPEC.md`.
5. Remove `SITE UNDER CONSTRUCTION` from the home page.
6. Add semantic landmarks, a skip link, descriptive headings, visible focus states, and correct link/button semantics on the home page and shared shell.
7. Add reusable title, description, canonical, Open Graph, and verified Person JSON-LD metadata support.
8. Add or update repository build instructions needed for this milestone.
9. Add `scripts/check_site.py` using the Python standard library to check built HTML for broken internal links and configured forbidden placeholder phrases.
10. Keep existing primary routes functional while introducing the shared shell. Make only the minimum compatibility edits required outside the home page.
11. Update `.project-loop/STATUS.md` with exact evidence, commands, outputs, changed files, deviations, risks, and blockers.

## Explicitly out of scope

- Final rewriting of research, projects, about, contact, books, or study-note content.
- Publishing unverified project descriptions, metrics, credentials, employment, or research results.
- Adding a CMS, backend, contact form, analytics, tracking, advertisements, or authentication.
- Migrating to React, Next.js, a CSS framework, or a JavaScript framework.
- Adding stock imagery, external icon libraries, external fonts, or unnecessary third-party scripts.
- Removing tracked `_site/` output before the new source build is verified; that cleanup belongs to M-004.
- Merging to `main` or deploying the site.

## Mapped acceptance criteria

- AC-001
- AC-003
- AC-008
- AC-009
- AC-010
- AC-013
- AC-015
- AC-016

## Required evidence

- A concise changed-file inventory.
- A statement of the exact starting SHA and final implementation SHA.
- Successful output for every required validation command.
- Built-route evidence for `/`, `/pages/about.html`, `/pages/projects.html`, `/pages/research.html`, `/pages/contact.html`, and `/study-notes/`.
- Home-page visual evidence at 360 px, 768 px, and 1440 px.
- Keyboard-navigation evidence covering the skip link, navigation, and primary calls to action.
- A list of all factual home-page claims and the approved source for each claim.
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

Until Bryan explicitly approves the specification, plan, and publication permission, Codex may work locally only. Codex must not commit, push, open or update a pull request, merge, or deploy under this pending directive.

When this directive is activated, the Project Director must explicitly restate whether Codex may commit and push a non-default branch and open or update a draft pull request.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when any of the following occurs:

- The approved positioning or home-page factual copy is ambiguous or conflicts with repository/user evidence.
- A proposed change would break an existing public route without an approved redirect.
- The Jekyll build cannot be reproduced from the repository and resolving it requires a material dependency or architecture change.
- A requested asset, profile image, project link, credential, or claim cannot be verified.
- The implementation requires a framework, backend, tracking, or other explicitly excluded capability.
- The working tree contains unrelated user changes that cannot be safely separated.
- The target branch has moved so the directive's base SHA no longer represents the inspected starting point.

## Next Project Director review focus

- Whether the home page immediately communicates a truthful and distinctive professional identity.
- Whether the design looks credible without relying on generic corporate language or decoration.
- Whether shared Jekyll structure reduces duplication without breaking existing routes.
- Whether accessibility and responsive behaviour are implemented, not merely claimed.
- Whether all factual content is traceable to Bryan's approval.
- Whether the implementation remains the smallest safe route to the approved outcome.
