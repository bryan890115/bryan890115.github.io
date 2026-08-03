# Website Professional Redesign Plan

State: DRAFT  
Specification state: DRAFT  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`

## Delivery strategy

Use four reviewable milestones. Each milestone must leave a buildable site and must be reviewed before the next milestone begins. Keep the existing Jekyll/GitHub Pages stack, introduce only small reusable components, and prefer deletion of generic or placeholder material over adding unverified copy.

## M-001 — Shared foundation and professional home page

State: PENDING  
Dependencies: User approval of this specification and plan  
Covers: AC-001, AC-003, AC-008, AC-009, AC-010, AC-013, AC-015, AC-016

### Scope

- Add a shared Jekyll page shell with reusable metadata, header/navigation, and footer includes.
- Establish a restrained design system using CSS custom properties, a responsive content grid, consistent type scale, spacing, buttons, cards, focus states, and reduced-motion support.
- Implement an accessible mobile navigation pattern with no framework dependency.
- Redesign the home page as the first complete vertical slice using the approved research-first positioning.
- Add a skip link and semantic landmarks.
- Add minimal reusable metadata support for title, description, canonical URL, Open Graph fields, and verified Person structured data.
- Add or update local build instructions.
- Add `scripts/check_site.py`, using Python's standard library, to check built HTML for broken internal links and configurable forbidden placeholder phrases.
- Keep the other primary pages working while the shared shell is introduced; do not perform their final content rewrite in this milestone.

### Explicitly excluded

- Final research, project, about, or contact copy.
- New project screenshots or publication assets.
- A contact form, analytics, or third-party UI framework.
- Removing tracked `_site/` output before the new build has been verified.

### Validation

```bash
bundle install
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
ruby -e 'require "yaml"; YAML.load_file("_config.yml"); puts "config ok"'
git diff --check
```

### Exit evidence

- Built home page and working navigation in `_site/`.
- Validation command output recorded in `.project-loop/STATUS.md`.
- Screenshots or equivalent visual evidence at 360 px, 768 px, and 1440 px for the home page.
- Keyboard-navigation notes covering skip link, navigation, and primary calls to action.
- Diff showing the shared shell and home-page vertical slice without unrelated content changes.

## M-002 — Evidence-backed research and project pages

State: PENDING  
Dependencies: M-001 accepted; Bryan confirms the public project/research facts and links  
Covers: AC-002, AC-004, AC-005, AC-011, AC-012, AC-014

### Scope

- Replace the current research cards and placeholder modal copy with a clear research narrative: problem, motivation, approach, current status, and approved outputs.
- Replace generic or invented project descriptions with three to five verified project case studies.
- For each project, include Bryan's role, the problem, methods or technology, evidence-backed outcome or learning, and a verified public link when available.
- Replace click-only cards and weak modal interactions with semantic links, accessible disclosures, or dedicated case-study sections.
- Use locally stored, optimized images only when they add evidence; otherwise use a strong text-first layout.
- Preserve the existing `/pages/research.html` and `/pages/projects.html` routes.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
! grep -RniE 'SITE UNDER CONSTRUCTION|Placeholder|More details coming soon|future deep dives|documented later' index.html pages _layouts _includes
ruby -e 'Dir["_site/**/*.html"].each { |f| abort("empty page: #{f}") if File.size(f) == 0 }; puts "html files non-empty"'
git diff --check
```

### Exit evidence

- Source list for every factual project/research claim, recorded in `STATUS.md` or the relevant page data file.
- Working research and project pages with no placeholder or duplicated filler content.
- Verified links for every public repository, paper, demo, or study-note reference.
- Keyboard and mobile checks for all interactive project/research elements.

## M-003 — About, contact, and study-note integration

State: PENDING  
Dependencies: M-002 accepted; Bryan confirms preferred public contact and profile details  
Covers: AC-002, AC-006, AC-007, AC-008, AC-009, AC-010, AC-014

### Scope

- Rewrite the about page around current education, MPhil research, relevant teaching, and concise technical/quantitative capability.
- Remove generic self-praise and unverified expertise claims.
- Rewrite the contact page with only approved channels and a simple, professional invitation to connect.
- Remove hard-coded response-time and consulting-availability promises unless Bryan explicitly approves them.
- Integrate study notes into the main navigation or a clearly labelled resources path while preserving existing URLs and content.
- Confirm the profile image decision; optimize and use it accessibly, or remove it without leaving a visual gap.
- Ensure the footer year and identity information are current and centrally managed.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
! grep -RniE 'Typically within 24-48 hours|Consulting Available|SITE UNDER CONSTRUCTION|Placeholder|© 2024' index.html pages _layouts _includes
python3 -m compileall scripts
git diff --check
```

### Exit evidence

- Approved final biography and contact details recorded in `STATUS.md`.
- About, contact, and study-note routes verified from the built site.
- Mobile and keyboard checks for all primary pages.
- No unapproved personal data added.

## M-004 — Repository cleanup, automated quality checks, and release candidate

State: PENDING  
Dependencies: M-003 accepted  
Covers: AC-009, AC-010, AC-012, AC-014, AC-015, AC-016, AC-017, AC-018

### Scope

- Remove tracked generated `_site/` files after confirming the source build reproduces the site.
- Confirm `.gitignore` excludes Jekyll output, caches, local gems, and operating-system files.
- Add a lightweight GitHub Actions workflow that builds the Jekyll site and runs the site checker on pull requests.
- Complete responsive, accessibility, metadata, performance, and browser-console QA.
- Update README documentation with local build, validation, content-editing, and deployment instructions.
- Prepare a release-candidate summary and evidence for final Project Director review.

### Validation

```bash
bundle install
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
test -z "$(git ls-files _site)"
git diff --check
git status --short
```

Where browser tooling is available, also run a Lighthouse audit against the locally served built home page and record the report path and scores in `STATUS.md`.

### Exit evidence

- Successful local build and site-check output.
- Successful GitHub Actions run on the implementation pull request.
- Evidence that `_site/` is no longer tracked.
- Responsive screenshots for home, research, projects, about, and contact.
- Keyboard-navigation and browser-console results.
- Lighthouse scores or a documented environment blocker.
- Final factual-content approval from Bryan.

## Risks and mitigations

### RISK-001 — Unverified public claims

Mitigation: Treat all current placeholder or generic claims as untrusted. Publish only facts and links confirmed by Bryan or verifiable from approved public sources. Prefer omission over approximation.

### RISK-002 — Breaking study-note URLs

Mitigation: Preserve existing paths, include them in the internal-link checker, and verify representative deep links after every milestone.

### RISK-003 — Large rewrite becomes difficult to review

Mitigation: Use milestone-sized vertical slices and keep the site buildable at every accepted commit.

### RISK-004 — Shared-layout migration changes old pages unexpectedly

Mitigation: Introduce the page shell incrementally, compare built routes before and after, and defer final page-content changes to their assigned milestones.

### RISK-005 — Portrait or project images weaken the professional result

Mitigation: Use a text-first layout that does not depend on images. Include images only when current, relevant, optimized, and approved.

### RISK-006 — Jekyll/GitHub Pages version mismatch

Mitigation: Keep dependencies minimal, document the supported Ruby/Bundler workflow, and validate both locally and in GitHub Actions before release.

## Dependency policy

- No JavaScript framework or CSS framework.
- No runtime package dependency for basic navigation or content display.
- Ruby/Jekyll dependencies must be limited to what is required for the GitHub Pages build.
- Python validation must use the standard library unless a new dependency is separately justified and approved.
- External fonts, icon libraries, embeds, and analytics are excluded by default.

## Documentation, migration, and rollout

- README must explain the site structure, local build, validation commands, and how to edit profile/project content.
- Existing URLs must remain stable or receive explicit redirects.
- The implementation remains on a non-default branch and draft pull request until final review.
- Neither Codex nor the Project Director may merge or deploy. Bryan owns final merge and publication.
