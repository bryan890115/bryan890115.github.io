# Current Codex Directive

Directive ID: D-0005  
Status: ACTIVE  
Milestone ID: M-004  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `e9a4dbba3ec2a06beffb49237e67f3f920226ae1`  
Issued timestamp: `2026-08-04T00:32:00+10:00`  
Replaced directive ID: D-0004

## Context and approvals

R-0004 accepted M-003 at the exact reviewed head above. M-001, M-002, and M-003 are accepted. DEC-001 governs the approved research/project publication set and privacy boundary. DEC-002 confirms the approved Contact channels:

- `mailto:bryan890115@gmail.com`
- `https://github.com/bryan890115`
- `https://www.linkedin.com/in/bryan-c-jen-0604a311b/`

No LinkedIn-derived biography or profile fact is approved. Public content is now frozen except for a necessary quality, accessibility, metadata, route, or documentation fix discovered during release-candidate validation.

## Required outcome

Produce a reviewable release candidate for the complete professional portfolio. Remove tracked generated output, add validation-only pull-request CI, complete full-site responsive/accessibility/metadata/performance QA, update maintenance and deployment documentation, attach reviewable evidence, and request Bryan's final factual and visual approval. Keep PR #11 draft and perform no merge or deployment.

## In-scope work

1. Pull the current `agent/professional-portfolio-redesign` branch and record its exact pre-work head as `Starting SHA` in `.project-loop/STATUS.md`.
2. Verify that D-0005's base SHA is an ancestor of the starting head and that intervening changes are limited to Director-owned `.project-loop/DECISIONS.md`, `.project-loop/REVIEW.md`, `.project-loop/PLAN.md`, and `.project-loop/DIRECTIVE.md`.
3. Prove the committed source builds successfully before deleting generated output.
4. Remove every tracked file under `_site/` from Git while keeping `_site/` ignored. Do not hand-edit generated output.
5. Confirm `.gitignore` excludes `_site/`, local bundle/gem directories, Python caches, test/browser outputs, OS files, and other generated artifacts without excluding required source.
6. Review source assets and remove only obsolete generated/legacy assets that are demonstrably unreferenced. Do not broaden this into a redesign or delete a source asset still used by the canonical study-note pages.
7. Add a lightweight validation-only GitHub Actions workflow under `.github/workflows/` triggered by `pull_request` and optionally manual dispatch. It must:
   - use supported official checkout and Ruby setup actions;
   - install dependencies from `Gemfile.lock` with Bundler caching when supported;
   - build Jekyll;
   - run `scripts/check_site.py`;
   - run the nine unit tests;
   - check JavaScript syntax;
   - compile Python scripts;
   - validate `_config.yml`;
   - assert zero checker exemptions;
   - assert no tracked `_site/` files;
   - scan for all forbidden placeholder, stale-footer, consulting, availability, and response-time phrases; and
   - have read-only repository permissions unless a strictly necessary permission is documented.
8. The workflow must not deploy, upload to GitHub Pages, push, comment automatically, mutate the repository, use secrets, or run on a schedule.
9. Update README with:
   - source layout and shared Jekyll structure;
   - supported local Ruby/Bundler setup and the known macOS system-Ruby incompatibility;
   - install, build, serve, checker, tests, and complete validation commands;
   - content-editing guidance for home, research, projects, about, contact, and study notes;
   - generated `_site/` policy;
   - PR validation workflow behavior;
   - metadata/configuration editing guidance; and
   - explicit statement that Bryan owns merge and GitHub Pages publication.
10. Build from a clean source state after `_site/` is untracked and confirm all required routes are non-empty:
    - `/`
    - `/pages/research.html`
    - `/pages/projects.html`
    - `/pages/about.html`
    - `/pages/contact.html`
    - `/pages/study-notes.html`
    - `/study-notes/`
    - `/study-notes/notes/mod0.html`
11. Verify public external links used by the site, including GitHub project links and the approved LinkedIn URL, without copying external profile content into the repository. Record unavailable/blocking responses honestly.
12. Complete responsive visual QA at 360, 768, and 1440 CSS pixels for Home, Research, Projects, About, Contact, and the study-note landing page. Check overflow, clipping, overlap, heading hierarchy, navigation state, focus visibility, and readability.
13. Attach or otherwise make reviewable actual screenshots for at least:
    - Home at 360 and 1440 px;
    - Research at one mobile and one desktop width;
    - Projects at one mobile and one desktop width;
    - About and Contact at one representative width each.
    Do not merely reference inaccessible local paths in `STATUS.md`.
14. Complete keyboard-only QA covering the skip link, desktop navigation, compact menu open/close/Escape/focus restoration, all home calls to action, all Research/Projects/About/Contact links, Resources compatibility link, and representative study-note navigation.
15. Inspect primary pages for one H1, semantic landmarks, sensible heading order, descriptive accessible names, visible focus, and no uncaught browser-console warning or error.
16. Verify each primary page's title, description, canonical URL, Open Graph fields, and shared Person JSON-LD. Confirm that approved email, GitHub, and LinkedIn URLs are consistent where used; do not add LinkedIn to JSON-LD unless Bryan explicitly approves that separate metadata change.
17. Run Lighthouse using available browser tooling for at least the home page at a production-like local build. Target:
    - Performance >= 90
    - Accessibility >= 95
    - Best Practices >= 95
    - SEO >= 95
    If a target cannot be met or tooling is unavailable, record exact scores or the precise environment blocker and do not silently waive the gate.
18. Fix only release-blocking defects discovered by these checks. Any factual-copy, project-selection, research-status, contact-channel, or strategic design change requires escalation.
19. Update `.project-loop/STATUS.md` with exact SHAs, changed files, commands, local outputs, CI run/check identity and conclusion, route/link results, screenshots/evidence locations, responsive/keyboard/console/metadata/Lighthouse results, deviations, risks, and blockers.
20. Update draft PR #11 to a release-candidate description, attach reviewable evidence, and post `CODEX_READY D-0005 at <FULL_SHA>` only after local checks pass and the PR validation workflow has completed successfully. If the workflow is pending or failing, do not post ready.
21. Explicitly request Bryan's final factual-content and visual approval in the private Codex response. Do not infer that prior milestone approvals constitute final release approval.

## Explicitly out of scope

- New or rewritten public biography, research, project, education, employment, teaching, metric, credential, availability, or private-source content.
- Changing the approved email, GitHub, or LinkedIn link.
- Adding LinkedIn or any new social URL to JSON-LD without separate explicit approval.
- Analytics, tracking, advertising, contact forms, scheduling, backend services, CMS, authentication, external fonts, stock imagery, framework migration, or new visual concept.
- A GitHub Pages deployment workflow, push-to-main automation, release creation, branch protection change, repository settings change, or secret use.
- Merging PR #11, marking it ready for review, deleting the implementation branch, or deploying the site.

## Mapped acceptance criteria

- AC-009
- AC-010
- AC-012
- AC-014
- AC-015
- AC-016
- AC-017
- AC-018
- All approved final quality gates

## Required evidence

- Exact starting SHA, implementation commit SHA, and final review head SHA.
- Focused changed-file inventory separating generated-output deletion, CI, documentation, tests/policy, and any release fix.
- Source build success before and after `_site/` removal.
- `test -z "$(git ls-files _site)"` success.
- Complete local validation output.
- PR validation workflow name, run ID/URL, head SHA, job/check names, and successful conclusion.
- Zero checker exemptions and zero forbidden-content scan matches.
- Built-route and representative deep-link results.
- Public external-link results with any access limitation stated.
- Reviewable screenshot evidence.
- Full keyboard, responsive, heading/landmark, focus, console, and metadata results.
- Lighthouse scores or precise blocker.
- Confirmation that approved content and privacy boundaries did not change.
- Bryan's final factual and visual approval status; initially `PENDING` until he responds.

## Exact local validation commands

Record `STARTING_SHA`, then run the authority checks before work:

```bash
git merge-base --is-ancestor e9a4dbba3ec2a06beffb49237e67f3f920226ae1 "$STARTING_SHA"
git diff --name-only e9a4dbba3ec2a06beffb49237e67f3f920226ae1..."$STARTING_SHA"
```

After implementation, run:

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
ruby -e 'required=%w[_site/index.html _site/pages/research.html _site/pages/projects.html _site/pages/about.html _site/pages/contact.html _site/pages/study-notes.html _site/study-notes/index.html _site/study-notes/notes/mod0.html]; required.each { |f| abort("missing or empty: #{f}") unless File.file?(f) && File.size(f) > 0 }; puts "release routes non-empty"'
git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

If the default system Ruby cannot load the pinned Bundler, use the existing compatible Ruby/Bundler launcher and record the exact deviation. Do not change dependencies merely to accommodate the system Ruby.

The pre-work diff from D-0005's base to `STARTING_SHA` must contain only `.project-loop/DECISIONS.md`, `.project-loop/REVIEW.md`, `.project-loop/PLAN.md`, and `.project-loop/DIRECTIVE.md`. Any other intervening change requires escalation.

## Publication permission

Codex may continue on `agent/professional-portfolio-redesign`, commit and push the bounded M-004 release-candidate work, update existing draft PR #11, and post the generic ready notification after all required conditions are satisfied.

Codex must not merge, deploy, push directly to `main`, mark the PR ready for review, alter repository settings, expose private material, or change frozen public content beyond a necessary release-blocking fix.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- The source does not reproduce after tracked `_site/` removal.
- A required public route or accepted link breaks.
- CI requires secrets, write permissions, deployment, or an unapproved third-party action.
- The PR workflow fails and cannot be fixed within the bounded validation scope.
- A Lighthouse gate fails and a meaningful fix would require content/design expansion rather than a small performance/accessibility correction.
- A screenshot or browser test exposes an important visual/accessibility regression that cannot be fixed generically.
- A factual or privacy discrepancy is discovered in accepted content.
- The starting branch contains unexpected changes after D-0005's base SHA.
- Bryan's final factual and visual approval is unavailable; in that case deliver the release candidate but keep final verdict blocked on approval.

## Next Project Director review focus

- Whether `_site/` is fully untracked and source reproduction is proven.
- Whether PR-only CI is safe, minimal, supported, passing, and non-deploying.
- Whether all primary routes, links, accessibility semantics, keyboard paths, metadata, console state, responsive layouts, and Lighthouse gates are evidenced.
- Whether screenshots are actually reviewable.
- Whether README and rollout ownership are complete.
- Whether accepted content and privacy boundaries remain unchanged.
- Whether Bryan has explicitly approved the final factual content and visual presentation.
- Whether the project is genuinely ready for PASS without merge or deployment by the Project Director.
