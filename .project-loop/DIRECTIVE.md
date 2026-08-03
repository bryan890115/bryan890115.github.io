# Current Codex Directive

Directive ID: D-0004  
Status: ACTIVE  
Milestone ID: M-003  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157`  
Issued timestamp: `2026-08-03T23:50:00+10:00`  
Replaced directive ID: D-0003

## Context and approval basis

R-0003 accepted M-002 at the exact reviewed head above. The approved specification already confirms:

- Bryan's positioning as an MPhil researcher working on natural-language interfaces for semantic building data, with a Computer Science and Actuarial Studies background;
- public email `bryan890115@gmail.com`;
- public GitHub account `bryan890115`;
- existing study-note URLs must remain functional; and
- the design must work without a portrait, with image reuse allowed only when the image is current and explicitly approved.

The current portrait has not been explicitly reconfirmed as current and approved. D-0004 therefore requires a complete text-first About and Contact implementation with no portrait. M-003 can satisfy AC-006 through current research and relevant experience; it must not invent education details, teaching appointments, employment, dates, marks, credentials, or other biography facts.

## Required outcome

Complete the About, Contact, and study-note integration milestone using only already approved specification facts and already accepted public project/research evidence. Remove generic self-praise, unsupported expertise, consulting/availability claims, response-time promises, inline legacy styling, and unapproved portrait references while preserving routes, accessibility, responsive behaviour, metadata, and the established design system.

## In-scope work

1. Pull the current `agent/professional-portfolio-redesign` branch and record its exact pre-work head as `Starting SHA` in `.project-loop/STATUS.md`.
2. Verify that D-0004's base SHA is an ancestor of the starting head and that intervening changes are limited to Director-owned `.project-loop/REVIEW.md`, `.project-loop/PLAN.md`, and `.project-loop/DIRECTIVE.md`.
3. Rewrite `pages/about.html` as a concise text-first profile using only:
   - the approved MPhil research positioning;
   - the approved Computer Science and Actuarial Studies background;
   - the accepted Research and Projects page evidence;
   - relevant experience evidenced by the five accepted project articles; and
   - concise skills directly evidenced by accepted public pages or repository source, such as Python, Brick, SPARQL, machine-learning/data workflows, Markdown, Jekyll, and MathJax.
4. Structure About around clear sections such as current work, background, selected experience, and evidenced capabilities. Use neutral factual language and semantic headings/articles/lists.
5. Do not add an institution name, degree title beyond the approved positioning/background, dates, marks, scholarships, accreditation, employment, tutoring/teaching appointment, award, location, age, collaborator name, publication, or credential unless that exact fact is already explicitly approved in the repository handoff. Omit rather than infer.
6. Remove the portrait and all portrait references from `pages/about.html`. The page must remain visually complete without an image.
7. Rewrite `pages/contact.html` as a neutral, concise contact page using only:
   - email `bryan890115@gmail.com`; and
   - GitHub `https://github.com/bryan890115`.
8. Use wording limited to contacting Bryan about the research or work presented on the site. Do not claim consulting availability, collaboration availability, response times, networking/mentorship availability, or guaranteed replies.
9. Remove prefilled marketing-style email subject/body parameters unless a simple subject is necessary and neutral; a plain `mailto:` link is preferred.
10. Remove the portrait and all portrait references from `pages/contact.html`.
11. Preserve the canonical `/study-notes/` route, `/pages/study-notes.html` compatibility page, existing navigation label, and representative note paths. Make only small integration/wording improvements; do not substantively rewrite study-note content.
12. Replace page-specific inline styles in the scoped pages with existing or narrowly added shared CSS. Keep the restrained design system and avoid unrelated visual expansion.
13. Remove the final `pages/contact.html` exemption from `site-check.json` after all forbidden phrases are absent. The final configuration must contain zero exemptions.
14. Update `tests/test_check_site.py` so the repository-policy test requires zero exemptions and prevents silent reintroduction of page-specific exceptions.
15. Preserve all accepted M-001 and M-002 content, routes, links, privacy boundaries, and conservative publication decisions.
16. Update `.project-loop/STATUS.md` with exact implementation evidence, a public-safe claim mapping, validation results, deviations, risks, and blockers.
17. Push changes to the existing branch, update draft PR #11 with a generic M-003 summary, and post `CODEX_READY D-0004 at <FULL_SHA>` when ready for Project Director review.

## Explicitly out of scope

- OneDrive access, private-source discovery, or reuse of private candidate notes.
- Adding unapproved institution names, program dates, graduation dates, marks, rankings, scholarships, accreditation, employment, tutoring/teaching claims, awards, locations, phone numbers, social accounts, credentials, or other personal data.
- Adding or retaining portrait imagery on About or Contact.
- Consulting offers, availability statements, response-time promises, networking/mentorship claims, or sales-oriented calls to action.
- Contact forms, scheduling tools, backend services, analytics, tracking, advertising, external fonts, icon libraries, stock imagery, or framework migration.
- Substantive rewriting of study-note content.
- Changing approved Research or Projects copy except for a necessary shared-style compatibility fix.
- Removing tracked `_site/`; that belongs to M-004.
- Merging PR #11 or deploying the site.

## Mapped acceptance criteria

- AC-002
- AC-006
- AC-007
- AC-008
- AC-009
- AC-010
- AC-014

## Required evidence

- Exact starting SHA, implementation commit SHA, and final review head SHA.
- A focused changed-file inventory.
- A public-safe mapping for every new factual About/Contact statement to the approved specification or accepted Research/Projects content.
- Confirmation that no unapproved profile fact, personal information, private evidence, or portrait was added.
- Confirmation that About uses neutral, evidence-backed language without generic self-praise.
- Confirmation that Contact exposes only the approved email and GitHub channels and contains no availability or response-time claim.
- Exact `site-check.json` change showing zero exemptions and a regression test requiring that state.
- Built-route evidence for `/pages/about.html`, `/pages/contact.html`, `/pages/study-notes.html`, `/study-notes/`, and a representative note page.
- Responsive evidence at 360 px, 768 px, and 1440 px for About and Contact.
- Keyboard-focus evidence for all links and compact navigation on the scoped pages.
- Browser-console results for About and Contact.
- Successful output for every required validation command.

## Exact validation commands

Record the exact pre-work branch head in `STARTING_SHA`, then run:

```bash
git merge-base --is-ancestor c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157 "$STARTING_SHA"
git diff --name-only c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157..."$STARTING_SHA"
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
git diff --name-only "$STARTING_SHA"...HEAD
```

If the default system Ruby cannot load the repository's pinned Bundler, Codex may use the already installed compatible Ruby/Bundler launcher with otherwise identical Jekyll arguments and must record that deviation precisely.

The pre-work diff from D-0004's base to `STARTING_SHA` must contain only `.project-loop/REVIEW.md`, `.project-loop/PLAN.md`, and `.project-loop/DIRECTIVE.md`. Any other intervening change requires escalation before implementation.

## Publication permission

Codex may continue on `agent/professional-portfolio-redesign`, commit and push the bounded M-003 implementation, update existing draft PR #11, and post a generic ready-for-review notification.

Codex must not merge, deploy, push implementation directly to `main`, expose private material, or expand public profile facts beyond this directive.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- An About or Contact statement cannot be supported by the approved specification or accepted public page evidence.
- Completing the page would require an unapproved institution, date, mark, employment, teaching, credential, location, portrait, or personal-detail claim.
- The existing portrait must be retained to make the design work.
- A route or study-note path would break without an unapproved migration.
- Removing the final checker exemption reveals forbidden text outside the bounded scope that cannot be safely deleted.
- The starting branch contains unexpected changes after D-0004's base SHA.
- The implementation requires an excluded dependency, backend, external service, or material design change.

## Next Project Director review focus

- Whether About is current, specific, and evidence-backed without generic praise or invented biography details.
- Whether Contact exposes only approved channels without promises or availability claims.
- Whether the text-first layout is complete and the unapproved portrait is absent.
- Whether study-note routes and navigation remain intact.
- Whether checker exemptions are reduced to zero with a durable regression test.
- Whether responsive, keyboard, metadata, and browser-console behaviour remain sound.
- Whether the implementation remains the smallest safe route to M-004.
