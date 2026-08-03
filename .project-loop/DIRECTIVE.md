# Current Codex Directive

Directive ID: D-0003  
Status: ACTIVE  
Milestone ID: M-002  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `3675b996628ff738ce9002b5c41a074a9cf5bc47`  
Issued timestamp: `2026-08-03T20:55:00+10:00`  
Replaced directive ID: D-0002

## Context and approval

R-0002 accepted the D-0002 private discovery gate at the exact reviewed head above. Bryan explicitly approved the private D-0002 research summary, selected general-project candidates, and Codex's conservative publication decisions. DEC-001 records this approval without reproducing private evidence or candidate notes.

The private D-0002 packet is the authority for which public-facing research and project content is approved. OneDrive evidence, private paths, raw files, private links, rejected candidates, internal notes, uncertainty notes, and the future-upload reminder are not approved for GitHub disclosure.

## Required outcome

Implement the exact approved research summary and selected general-project cards from the private D-0002 packet on the existing Jekyll site. Replace the current generic, invented, repeated, or placeholder research/project content with concise evidence-backed public content while preserving routes, accessibility, responsive behaviour, and the privacy boundary.

## In-scope work

1. Pull the current `agent/professional-portfolio-redesign` branch and record its exact pre-work head as `Starting SHA` in `.project-loop/STATUS.md`.
2. Verify that D-0003's base SHA is an ancestor of the starting head and that intervening changes are limited to Director-owned `.project-loop/DECISIONS.md`, `.project-loop/REVIEW.md`, `.project-loop/PLAN.md`, and `.project-loop/DIRECTIVE.md`.
3. Rewrite `pages/research.html` using only the exact public-facing research summary approved in the private D-0002 packet:
   - research problem;
   - motivation;
   - approach;
   - current status;
   - genuinely public outputs or links approved for display.
4. Rewrite `pages/projects.html` using only the selected general-project candidates and conservative public-facing copy approved in the private D-0002 packet.
5. For each approved project, present only the approved title, purpose/problem, Bryan's role or contribution, methods/technologies, result or main learning, and approved public link or no-link treatment.
6. Preserve conservative exclusions, redactions, attribution limits, ownership restrictions, assessment-integrity decisions, and link decisions from the approved packet.
7. Replace click-only `<div>` cards and the weak legacy modal pattern with semantic `<article>`, `<a>`, `<button>`, or accessible disclosure structures appropriate to the amount of content. Do not retain a dialog unless focus entry, focus trapping, Escape, close, and focus restoration are correctly implemented and tested.
8. Remove repeated filler, fake consulting language, invented business outcomes, placeholder paragraphs, hidden placeholder detail blocks, and obsolete inline modal scripts from the research and projects pages.
9. Update the shared CSS only as needed to support the approved research/project presentation. Keep the existing restrained design system and avoid framework or decorative scope expansion.
10. Use a local image or other asset only when the private packet explicitly marked it publishable and ownership/licensing is clear. Otherwise use the existing text-first design. Do not copy a raw OneDrive file into the repository merely because it was evidence.
11. Preserve `/pages/research.html`, `/pages/projects.html`, home-page links, primary navigation, and representative study-note routes.
12. Remove research/project exemptions from `site-check.json` once the corresponding forbidden phrases are absent. Retain unrelated contact-page exemptions until M-003.
13. Update tests when needed so the checker prevents reintroduction of public placeholders and does not silently broaden exemptions.
14. Update `.project-loop/STATUS.md` with exact implementation evidence, public-safe claim/approval mappings, validation results, deviations, risks, and blockers.
15. Push changes to the existing branch and update draft PR #11 with a generic M-002 implementation summary. Post `CODEX_READY D-0003 at <FULL_SHA>` when ready for Project Director review.

## Explicitly out of scope

- Adding any candidate, wording, result, metric, collaborator, link, or asset not marked approved in the private D-0002 packet.
- Re-inspecting OneDrive to broaden the approved set or reconstructing missing packet content.
- Committing or posting OneDrive paths, raw files, private URLs, private screenshots, candidate notes, rejected candidates, assessment material, evidence excerpts, uncertainty notes, credentials, secrets, or third-party personal data.
- Publishing the private reminder `Future project — upload supporting material to OneDrive` or any placeholder/future-project card.
- Final rewriting of About, Contact, books, or study-note content; these remain assigned to later milestones.
- Adding analytics, a contact form, a backend, a CMS, a JavaScript/CSS framework, external fonts, stock imagery, or unrelated redesign work.
- Removing tracked `_site/` output; that remains assigned to M-004.
- Merging PR #11 or deploying the site.

## Mapped acceptance criteria

- AC-002
- AC-004
- AC-005
- AC-011
- AC-012
- AC-014

## Required evidence

- Exact starting SHA, implementation commit SHA, and final review head SHA.
- A focused changed-file inventory.
- A public-safe mapping for every published factual claim to `Bryan-approved D-0002 private packet`, plus any independently public repository or URL evidence, without naming private source paths.
- Confirmation that the implemented project set exactly matches the candidates marked approved and selected in the private packet.
- Confirmation that all conservative exclusions and no-link decisions were preserved.
- Confirmation that no OneDrive evidence, private path, raw file, private URL, internal note, rejected candidate, reminder, or unapproved asset was committed or posted.
- Successful output for every validation command.
- Built-route evidence for `/pages/research.html`, `/pages/projects.html`, `/`, and representative study-note routes.
- Responsive evidence at 360 px, 768 px, and 1440 px for research and projects pages.
- Keyboard evidence for every project/research interaction and link.
- Browser-console results for research and projects pages.
- Exact exemption changes in `site-check.json` and evidence that project/research placeholder exemptions are no longer required.

## Exact validation commands

Record the exact pre-work branch head in `STARTING_SHA`, then run:

```bash
git merge-base --is-ancestor 3675b996628ff738ce9002b5c41a074a9cf5bc47 "$STARTING_SHA"
git diff --name-only 3675b996628ff738ce9002b5c41a074a9cf5bc47..."$STARTING_SHA"
bundle exec jekyll build --trace
python3 scripts/check_site.py _site
python3 -m unittest discover -s tests -v
node --check assets/js/script.js
! grep -RniE 'SITE UNDER CONSTRUCTION|Placeholder|More details coming soon|future deep dives|documented later' index.html pages _layouts _includes
! grep -RniE 'Future project|upload supporting material to OneDrive|private approval packet|OneDrive' index.html pages _layouts _includes assets
ruby -e 'Dir["_site/**/*.html"].each { |f| abort("empty page: #{f}") if File.size(f) == 0 }; puts "html files non-empty"'
git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

The pre-work diff from the directive base to `STARTING_SHA` must contain only Director-owned project-loop files. Any other intervening change requires escalation before implementation.

## Publication permission

Codex may continue on `agent/professional-portfolio-redesign`, commit and push the approved M-002 implementation, update existing draft PR #11, and post a generic ready-for-review notification.

Codex must not merge, deploy, push implementation directly to `main`, expose private evidence, or expand beyond the approved private publication set.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- The private D-0002 packet or its approved/selected markings are unavailable, incomplete, or ambiguous in the active Codex context.
- It is unclear whether a particular title, sentence, contribution, result, link, image, or asset was approved for public use.
- Implementing a candidate would require returning to private evidence to infer or broaden the approved copy.
- Ownership, licensing, assessment integrity, collaborator attribution, privacy, or permission to publish is unresolved.
- An approved public link is unavailable, redirects unexpectedly, exposes private access, or does not support the stated content.
- The branch contains unexpected non-Director changes after the base SHA.
- A route cannot be preserved without an unapproved redirect or material architecture change.
- Passing validation would require weakening the checker, adding broad exemptions, or hiding placeholder/private text.

On ambiguity, omit nothing silently and guess nothing. Report the exact public-facing decision needed without posting private source details to GitHub.

## Next Project Director review focus

- Exact fidelity to Bryan's approved conservative publication set.
- Accuracy and modesty of the research summary.
- Whether selected projects clearly state the problem, Bryan's contribution, methods, and evidence-backed outcome or learning.
- Removal of fake, generic, repeated, and placeholder content.
- Semantic and keyboard-accessible project/research presentation.
- Preservation of routes and the M-001 design system.
- Narrow checker configuration with project/research exemptions removed.
- Absence of OneDrive evidence, private paths, raw files, notes, reminders, and unapproved assets from GitHub.
- Whether the implementation remains the smallest safe route to M-002 acceptance.
