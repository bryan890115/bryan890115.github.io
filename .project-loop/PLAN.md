# Website Professional Redesign Plan

State: APPROVED  
Specification state: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`  
Approval date: 2026-08-03

## Delivery strategy

Deliver four reviewable milestones. Each milestone must leave a buildable site and be reviewed before the next begins. Keep Jekyll/GitHub Pages, use small reusable components, and delete generic or placeholder material rather than replacing it with unverified copy.

## M-001 — Shared foundation and professional home page

State: ACTIVE  
Dependencies: Approved specification and plan; satisfied 2026-08-03  
Covers: AC-001, AC-003, AC-008, AC-009, AC-010, AC-013, AC-015, AC-016

### Scope

- Add a shared Jekyll shell for metadata, header/navigation, main content, and footer.
- Establish a restrained CSS system for typography, spacing, grid, buttons, cards, focus, reduced motion, and responsive behaviour.
- Add accessible mobile navigation and a skip link without a framework.
- Redesign the home page using the approved research-first positioning.
- Add reusable title, description, canonical, Open Graph, and verified Person JSON-LD support.
- Add or update local build instructions.
- Add standard-library `scripts/check_site.py` for internal links and forbidden placeholder phrases.
- Keep other primary routes working; defer their final rewrite.

### Excluded

Final research, project, about, contact, books, or study-note rewrites; new screenshots/publications; contact forms; analytics; third-party UI frameworks; and `_site/` removal before the source build is verified.

### Validation

```bash
bundle install
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
git diff --check
```

### Exit evidence

Built primary routes; command output in `STATUS.md`; home-page evidence at 360 px, 768 px, and 1440 px; keyboard notes for skip link, navigation, and calls to action; and a focused diff without unrelated changes.

## M-002 — Evidence-backed research and project pages

State: PENDING  
Dependencies: M-001 accepted; Bryan confirms public facts and links  
Covers: AC-002, AC-004, AC-005, AC-011, AC-012, AC-014

### Scope

- Replace research placeholders with the problem, motivation, approach, current status, and approved outputs.
- Replace generic projects with three to five verified case studies describing Bryan's role, problem, methods, and outcome or learning.
- Use verified public links only.
- Replace click-only cards or weak modals with semantic links, disclosures, or case-study sections.
- Use optimized local images only where they add evidence.
- Preserve `/pages/research.html` and `/pages/projects.html`.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
! grep -RniE 'SITE UNDER CONSTRUCTION|Placeholder|More details coming soon|future deep dives|documented later' index.html pages _layouts _includes
ruby -e 'Dir["_site/**/*.html"].each { |f| abort("empty page: #{f}") if File.size(f) == 0 }; puts "html files non-empty"'
git diff --check
```

### Exit evidence

A source for every factual claim; working pages without filler; verified links; and keyboard/mobile checks for project and research interactions.

## M-003 — About, contact, and study-note integration

State: PENDING  
Dependencies: M-002 accepted; Bryan confirms contact and profile details  
Covers: AC-002, AC-006, AC-007, AC-008, AC-009, AC-010, AC-014

### Scope

- Rewrite About around current education, MPhil research, relevant teaching, and concise technical/quantitative capability.
- Remove generic self-praise and unverified expertise.
- Keep Contact to approved channels and remove unsupported availability or response-time promises.
- Integrate study notes into navigation or a clearly labelled Resources path while preserving URLs.
- Use the portrait only if current and approved; otherwise keep a complete text-first layout.
- Centralize current footer year and identity information.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
! grep -RniE 'Typically within 24-48 hours|Consulting Available|SITE UNDER CONSTRUCTION|Placeholder|© 2024' index.html pages _layouts _includes
python3 -m compileall scripts
git diff --check
```

### Exit evidence

Approved biography/contact details in `STATUS.md`; verified about, contact, and study-note routes; mobile and keyboard checks; and no unapproved personal data.

## M-004 — Cleanup, automated quality checks, and release candidate

State: PENDING  
Dependencies: M-003 accepted  
Covers: AC-009, AC-010, AC-012, AC-014, AC-015, AC-016, AC-017, AC-018

### Scope

- Remove tracked `_site/` after confirming source reproduction.
- Confirm `.gitignore` excludes generated output, caches, local gems, and OS files.
- Add a lightweight pull-request workflow that builds Jekyll and runs the checker.
- Complete responsive, accessibility, metadata, performance, and console QA.
- Update README with build, validation, content-editing, and deployment instructions.
- Prepare release-candidate evidence for final review.

### Validation

```bash
bundle install
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
test -z "$(git ls-files _site)"
git diff --check
git status --short
```

Run Lighthouse where browser tooling is available and record scores or the environment blocker.

### Exit evidence

Successful local and CI checks; `_site/` untracked; responsive evidence for primary pages; keyboard and console results; Lighthouse evidence; and Bryan's final factual-content approval.

## Risks and mitigations

- **RISK-001 — Unverified claims:** publish only facts and links Bryan approves or approved sources verify; omit uncertainty.
- **RISK-002 — Broken study-note URLs:** preserve paths and test representative deep links each milestone.
- **RISK-003 — Unreviewable rewrite:** use buildable milestone-sized vertical slices.
- **RISK-004 — Layout migration regressions:** migrate incrementally and compare built routes.
- **RISK-005 — Weak imagery:** use a text-first design and only current, relevant, optimized, approved images.
- **RISK-006 — Jekyll version mismatch:** minimize dependencies and validate locally and in GitHub Actions.

## Dependency policy

No JavaScript or CSS framework; no runtime dependency for basic navigation/content; minimal Ruby/Jekyll dependencies; standard-library Python validation unless separately justified and approved; external fonts, icon libraries, embeds, and analytics excluded by default.

## Documentation, migration, and rollout

README must explain site structure, local build, validation, and content editing. Existing URLs remain stable or receive explicit redirects. Implementation stays on a non-default branch and draft pull request until final review. Codex and the Project Director must not merge or deploy; Bryan owns final merge and publication.
