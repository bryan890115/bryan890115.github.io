# Website Professional Redesign Plan

State: COMPLETE  
Specification state: APPROVED  
Final project verdict: PASS  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`  
Approval date: 2026-08-03  
Completion date: 2026-08-04

## Delivery strategy

Four buildable, independently reviewed milestones were completed. The implementation keeps Jekyll/GitHub Pages, uses reusable components, preserves important routes, publishes only approved evidence-backed content, and remains unmerged and undeployed by Codex or the Project Director.

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

State: ACCEPTED  
Accepted review: R-0005  
Reviewed implementation head: `6d312b079d4baa69e05a8fe24779f9194bd12a16`  
Final approval: DEC-003  
Covers: AC-009, AC-010, AC-012, AC-014, AC-015, AC-016, AC-017, AC-018 and all final quality gates

### Completed scope

- Proved source reproduction and removed every tracked `_site/` file while keeping generated output ignored.
- Added read-only, validation-only PR CI with no deployment, secret, write, comment, or scheduled behavior.
- Updated README with supported setup, source layout, full checks, content editing, generated-output policy, CI behavior, and Bryan-owned merge/publication instructions.
- Completed responsive, keyboard, accessibility, route, link, metadata, console, and Lighthouse checks.
- Added eight immutable release-review screenshots excluded from the generated public site.
- Converted legacy click-only study-module cards to links, contained narrow-screen MathJax, improved focus treatment, sized the retained note portrait, and added a local favicon.
- Removed only demonstrably unreferenced legacy assets.
- Preserved accepted content, Contact boundaries, and all privacy constraints.

### Accepted validation evidence

- Exact-head workflow run `30827825395` succeeded at `6d312b079d4baa69e05a8fe24779f9194bd12a16`; every validation step passed.
- Local build passed with the supported Ruby 3.4/Bundler 2.5.23 launcher.
- Site checker: 15 HTML files, 242 references, zero exemptions.
- Nine tests passed; JavaScript, Python, YAML, route, generated-output, and forbidden-copy checks passed.
- `_site/` has zero tracked files and rebuilds from source.
- All required primary and representative study-note routes are non-empty.
- Responsive/keyboard/console/metadata checks passed.
- Lighthouse Performance is at least 94; Accessibility, Best Practices, and SEO are 100 for all recorded routes.
- Bryan explicitly approved final factual content and visual presentation.

## Final state and ownership

All milestones and approved acceptance criteria are complete. The repository/source project verdict is PASS.

PR #11 remains on a non-default branch. Bryan alone owns the final merge, GitHub Pages publication, and custom-domain configuration. The Project Director and Codex must not merge or deploy.

Bryan reports that the custom-domain issue may now be fixed. Because the Project Director environment could not independently resolve the domain during finalization, Bryan should confirm a valid browser certificate for `https://bryan-c-jen.au` before or immediately after merging.
