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

State: ACCEPTED  
Dependencies: Approved specification and plan; satisfied 2026-08-03  
Accepted review: R-0001 at PR #11 head `0f7408e0fbe1fba5ac76f373711f7eef1e89e4c6`  
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

State: ACCEPTED  
Dependencies: M-001 accepted; private discovery packet delivered and approved through DEC-001 and R-0002  
Accepted review: R-0003 at PR #11 head `c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157`  
Covers: AC-002, AC-004, AC-005, AC-011, AC-012, AC-014

### Completed scope

- Replaced research placeholders with the approved problem, motivation, staged approach, current status, and no-public-output treatment.
- Replaced generic and invented projects with exactly five approved general-project articles.
- Published only approved public titles, contribution statements, methods, outcomes or learnings, and verified link or no-link treatments.
- Preserved conservative exclusions, team attribution, clinical and academic caveats, ownership constraints, omitted metrics, and text-first asset decisions.
- Removed click-only cards, hidden placeholder details, weak modal behavior, obsolete scripts, and scoped modal CSS.
- Removed research and project placeholder exemptions while retaining only the deferred contact-page exemption.
- Preserved `/pages/research.html`, `/pages/projects.html`, home-page navigation, and representative study-note routes.
- Kept all OneDrive evidence, private paths, raw files, private links, candidate notes, rejected candidates, uncertainty notes, and reminders outside GitHub.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
python3 -m unittest discover -s tests -v
node --check assets/js/script.js
! grep -RniE 'SITE UNDER CONSTRUCTION|Placeholder|More details coming soon|future deep dives|documented later' index.html pages _layouts _includes
! grep -RniE 'Future project|upload supporting material to OneDrive|private approval packet|OneDrive' index.html pages _layouts _includes assets
ruby -e 'Dir["_site/**/*.html"].each { |f| abort("empty page: #{f}") if File.size(f) == 0 }; puts "html files non-empty"'
git diff --check
git status --short
```

### Accepted evidence

- Exact implementation and review SHAs.
- Public-safe approval mapping for all research/project claims.
- Five semantic project articles in approved order.
- Two verified public links and three intentional no-link treatments.
- Responsive and keyboard evidence reported for Research and Projects.
- No private evidence, unapproved asset, metric, placeholder, or future-project card in GitHub or built output.
- Narrow checker scope with only the deferred Contact exemption remaining.

## M-003 — About, contact, and study-note integration

State: ACTIVE  
Dependencies: M-002 accepted through R-0003; approved specification confirms public email `bryan890115@gmail.com`, public GitHub account `bryan890115`, approved positioning, and a layout that must work without a portrait  
Active implementation directive: D-0004  
Covers: AC-002, AC-006, AC-007, AC-008, AC-009, AC-010, AC-014

### Active scope

- Rewrite About around the approved MPhil research positioning, Computer Science and Actuarial Studies background, selected public project evidence, and concise evidenced technical/quantitative capabilities.
- Satisfy AC-006 through current research and relevant experience; do not invent institution names, degree dates, marks, employment, teaching appointments, credentials, or other profile details.
- Remove generic self-praise, unsupported expertise, financial-services positioning, and broad consulting language.
- Rewrite Contact as a neutral page using only the approved public email and GitHub account.
- Remove consulting offers, availability promises, mentorship/networking claims, response-time guarantees, and prefilled marketing-style inquiry copy.
- Use a complete text-first layout. Remove portrait references from About and Contact because the current image has not been explicitly confirmed as current and approved.
- Preserve the canonical `/study-notes/` route, the `/pages/study-notes.html` compatibility page, representative note routes, and the existing Resources navigation.
- Remove the final Contact exemption from `site-check.json` after the forbidden phrases are absent; update the regression test to require zero exemptions.
- Update shared CSS only as needed to replace inline styles and support the bounded About/Contact presentation.

### Explicit exclusions

- No OneDrive access or private-source content.
- No unapproved institution, date, mark, employment, tutoring, teaching, award, accreditation, location, phone, social profile, or credential claim.
- No portrait or new personal image.
- No contact form, scheduling link, response-time promise, consulting offer, availability claim, analytics, tracking, external font, icon library, or unrelated redesign.
- No substantive rewrite of study-note content.
- No `_site/` removal; that remains M-004.

### Validation

```bash
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
python3 -m unittest discover -s tests -v
node --check assets/js/script.js
python3 -m compileall scripts
! grep -RniE 'Typically within 24-48 hours|Consulting Available|Open to consulting opportunities|Available for consulting opportunities|Available for consulting engagements|consulting services|Open to professional inquiries and collaboration discussions|SITE UNDER CONSTRUCTION|Placeholder|© 2024' index.html pages _layouts _includes
! grep -RniE 'profile-professional\.jpg' pages/about.html pages/contact.html
ruby -e 'required=%w[_site/pages/about.html _site/pages/contact.html _site/pages/study-notes.html _site/study-notes/index.html _site/study-notes/notes/mod0.html]; required.each { |f| abort("missing or empty: #{f}") unless File.file?(f) && File.size(f) > 0 }; puts "required routes non-empty"'
git diff --check
git status --short --branch
```

### Exit evidence

- Exact starting, implementation, and final review SHAs.
- A public-safe mapping from every new About/Contact claim to the approved specification or already accepted public page evidence.
- About and Contact with no generic self-praise, unapproved profile claim, consulting offer, response-time promise, or portrait reference.
- Zero site-check exemptions and passing checker tests.
- Verified email, GitHub, study-note compatibility, canonical study-note, and representative note links.
- Responsive checks at 360 px, 768 px, and 1440 px for About and Contact.
- Keyboard-focus and browser-console results for all About/Contact interactions.
- Confirmation that no private or unapproved personal information was added.

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

- **RISK-001 — Unverified claims:** publish only facts and links Bryan approved; omit uncertainty.
- **RISK-002 — Broken study-note URLs:** preserve paths and test representative deep links each milestone.
- **RISK-003 — Unreviewable rewrite:** use buildable milestone-sized vertical slices.
- **RISK-004 — Layout migration regressions:** migrate incrementally and compare built routes.
- **RISK-005 — Weak imagery:** use a text-first design and only current, relevant, optimized, approved images.
- **RISK-006 — Jekyll version mismatch:** minimize dependencies and validate locally and in GitHub Actions.
- **RISK-007 — Private discovery material exposed through a public PR:** implement only the privately approved public-facing set, keep evidence and notes outside GitHub, use public-safe approval mappings, and stop on ambiguity.
- **RISK-008 — Private packet unavailable after context loss:** Codex must stop and request Bryan to re-supply or reconfirm the public-facing copy privately rather than reconstructing it from OneDrive or guessing.
- **RISK-009 — Generic profile copy replaced with new unsupported claims:** M-003 must use only approved specification facts and accepted public project evidence, omit uncertain biography details, and use no portrait.

## Dependency policy

No JavaScript or CSS framework; no runtime dependency for basic navigation/content; minimal Ruby/Jekyll dependencies; standard-library Python validation unless separately justified and approved; external fonts, icon libraries, embeds, and analytics excluded by default.

## Documentation, migration, and rollout

README must explain site structure, local build, validation, and content editing. Existing URLs remain stable or receive explicit redirects. Implementation stays on a non-default branch and draft pull request until final review. Codex and the Project Director must not merge or deploy; Bryan owns final merge and publication.
