# Website Professional Redesign Plan

State: APPROVED  
Specification state: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`  
Approval date: 2026-08-03

## Delivery strategy

Deliver four buildable, independently reviewed milestones. Keep Jekyll/GitHub Pages, use small reusable components, preserve important routes, publish only approved evidence-backed content, and do not merge or deploy through Codex or the Project Director.

## M-001 — Shared foundation and professional home page

State: ACCEPTED  
Accepted review: R-0001 at `0f7408e0fbe1fba5ac76f373711f7eef1e89e4c6`  
Covers: AC-001, AC-003, AC-008, AC-009, AC-010, AC-013, AC-015, AC-016

### Completed scope

- Shared Jekyll layout, metadata, navigation, footer, skip link, responsive design system, compact navigation, and reduced-motion/focus support.
- Research-first home page using the approved positioning.
- Local build documentation, standard-library site checker, policy configuration, and unit tests.
- Required primary routes preserved during staged migration.

## M-002 — Evidence-backed research and project pages

State: ACCEPTED  
Accepted review: R-0003 at `c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157`  
Content approval: DEC-001 and R-0002  
Covers: AC-002, AC-004, AC-005, AC-011, AC-012, AC-014

### Completed scope

- Approved MPhil research summary with conservative current-status and no-public-output treatment.
- Exactly five approved project articles with contribution, methods, and outcome or learning.
- Two verified public links and three intentional no-link treatments.
- Legacy click-only cards, hidden placeholders, modal behavior, invented outcomes, and scoped exemptions removed.
- Text-first asset decision and all private discovery boundaries preserved.

## M-003 — About, contact, and study-note integration

State: ACCEPTED  
Accepted review: R-0004 at `e9a4dbba3ec2a06beffb49237e67f3f920226ae1`  
Contact approval: DEC-002 confirms email, GitHub, and exact LinkedIn URL  
Covers: AC-002, AC-006, AC-007, AC-008, AC-009, AC-010, AC-014

### Completed scope

- About rewritten as a text-first, evidence-backed profile using approved positioning and accepted public research/project evidence.
- Contact rewritten with only approved email, GitHub, and LinkedIn channels.
- Generic praise, unsupported biography claims, portrait references, consulting/availability language, response-time promises, and marketing inquiry copy removed.
- Study-note compatibility and canonical routes preserved.
- Checker exemptions reduced to zero with regression coverage.

## M-004 — Cleanup, automated quality checks, and release candidate

State: ACTIVE  
Dependencies: M-003 accepted through R-0004  
Active implementation directive: D-0005  
Covers: AC-009, AC-010, AC-012, AC-014, AC-015, AC-016, AC-017, AC-018 and all final quality gates

### Active scope

- Confirm source-only reproduction, then remove all tracked `_site/` generated output and ensure `_site/` remains ignored.
- Remove stale generated or obsolete assets only when their source usage is absent and deletion is safe; do not broaden into content redesign.
- Confirm `.gitignore` covers `_site/`, local gems, caches, OS files, test/browser artifacts, and other generated output without hiding source.
- Add a lightweight **validation-only** GitHub Actions workflow for pull requests. It must build Jekyll and run the site checker, unit tests, JavaScript syntax, Python compilation, zero-exemption policy, placeholder/privacy scans, and tracked-`_site` assertion. It must not deploy or write to the repository.
- Use supported official GitHub actions and a reproducible Ruby/Bundler setup derived from the repository lockfile. Avoid unnecessary third-party actions.
- Update README with source layout, local setup, build, preview, checks, content editing, generated-output policy, CI behavior, and user-owned merge/deployment steps.
- Complete full-site responsive QA at 360, 768, and 1440 px for Home, Research, Projects, About, Contact, and Resources/study notes.
- Complete keyboard-only QA for skip link, primary navigation, compact navigation, all calls to action, and all public links.
- Verify titles, descriptions, canonical URLs, Open Graph fields, Person JSON-LD, headings, landmarks, link targets, and browser-console results on primary pages.
- Run Lighthouse on the home page and primary pages where practical. Record scores and satisfy the approved home targets—Performance at least 90 and Accessibility, Best Practices, and SEO at least 95—or provide a precise environment blocker for Project Director approval.
- Produce reviewable release-candidate evidence. Attach or link screenshots for the home page and scoped primary pages at representative desktop/mobile widths rather than merely naming local files.
- Update PR #11 to a release-candidate description while keeping it draft.
- Request Bryan's final factual-content and visual approval; do not mark the project PASS or merge before that approval is returned.

### Explicit exclusions

- No new biography, project, research, education, employment, teaching, metric, credential, private-source, or availability claim.
- No change to approved email, GitHub, or LinkedIn channels without new approval.
- No content redesign, framework migration, analytics, tracking, contact form, backend, CMS, external font, stock imagery, advertising, or deployment workflow.
- No GitHub Pages deployment action or push-to-main automation.
- No merge, release, or deployment by Codex or the Project Director.

### Required validation

```bash
bundle install
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
git diff --check
git status --short --branch
```

The new pull-request workflow must run the applicable non-browser checks successfully at the release-candidate head. Codex must inspect the workflow result and record its run/check identity and conclusion.

### Exit evidence

- Exact starting SHA, implementation commit SHA, final review head, and changed-file inventory.
- `_site/` absent from tracked files and reproducible from source.
- Passing local checks and passing PR validation workflow.
- Zero checker exemptions, zero forbidden placeholder/marketing phrases, and no privacy-boundary regression.
- Verified primary routes and representative deep study-note route.
- Reviewable responsive screenshots and keyboard/console results.
- Metadata and Lighthouse results or a precise approved environment exception.
- Updated README and clear deployment ownership.
- Bryan's explicit final factual-content and visual approval.

## Risks and mitigations

- **Unverified content:** freeze accepted public copy; omit rather than infer.
- **Private evidence exposure:** keep all OneDrive/private discovery material outside GitHub.
- **Broken note URLs:** build and test compatibility, canonical, and representative deep links.
- **Generated-output confusion:** remove tracked `_site/`, validate source reproduction locally and in CI, and document the policy.
- **CI dependency drift:** use supported official actions and lockfile-driven Ruby/Bundler setup; keep workflow validation-only.
- **Unreviewable visual claims:** attach actual screenshots or other reviewable evidence to PR #11.
- **Premature publication:** PR remains draft; Bryan owns final approval, merge, and deployment.

## Dependency policy

No JavaScript or CSS framework; no runtime dependency for basic content/navigation; minimal Ruby/Jekyll dependencies; standard-library Python validation; external fonts, icon libraries, embeds, analytics, and deployment actions excluded by default.

## Documentation, migration, and rollout

README must explain site structure, local build, validation, content editing, generated output, CI, and deployment ownership. Existing URLs remain stable or receive explicit redirects. Implementation remains on a non-default branch and draft PR until final Project Director review and Bryan's final approval. Bryan alone owns merge and publication.
