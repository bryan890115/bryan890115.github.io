# Website Professional Redesign Specification

Protocol version: 1  
State: APPROVED  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Planning branch: `agent/professional-portfolio-redesign-plan`  
Approval state: APPROVED BY BRYAN JEN  
Draft date: 2026-08-03  
Approval date: 2026-08-03  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`

## Goal

Transform the GitHub Pages site into a credible, modern, maintainable portfolio presenting Bryan Jen as a research-focused computer scientist with an Actuarial Studies background. A visitor should understand his current work, technical capability, selected evidence, and contact path within one minute, without placeholder material or unsupported claims.

## Audience

- Academic supervisors, collaborators, and research partners.
- Technical recruiters and employers in software, data, AI, and quantitative work.
- Students and peers seeking research, project, or study-note material.

## Approved positioning

> MPhil researcher working on natural-language interfaces for semantic building data, with a background in Computer Science and Actuarial Studies.

Bryan approved this positioning without corrections on 2026-08-03.

## Goals

- Lead with Bryan's current research identity rather than generic consulting language.
- Replace filler with concise, evidence-backed research, project, education, teaching, and skills content.
- Use a restrained visual system appropriate for an academic and technical portfolio.
- Preserve GitHub Pages/Jekyll deployment and existing important URLs.
- Improve accessibility, responsiveness, metadata, performance, and maintainability.

## Non-goals

- A CMS, database, authentication system, backend, data-storing contact form, analytics, advertising, or tracking.
- Invented publications, outcomes, client work, employment, metrics, credentials, or availability claims.
- Publishing private coursework, repositories, research, or assessment content without approval.
- Substantive rewriting of existing study notes.
- Migration to React, Next.js, or another application framework.
- Merge or deployment by Codex or the Project Director.

## Constraints

- Remain compatible with GitHub Pages and Jekyll using HTML, Liquid, CSS, and minimal vanilla JavaScript.
- Preserve or redirect `/`, `/pages/about.html`, `/pages/projects.html`, `/pages/research.html`, `/pages/contact.html`, and `/study-notes/`.
- Use only verified, user-approved claims, links, and personal information.
- Work at 360 px, 768 px, and 1440 px without horizontal scrolling.
- Interactive elements must be keyboard operable and visibly focusable.
- Generated `_site/` output is not source and must not be edited or normally committed.

## Approved assumptions

- Public email: `bryan890115@gmail.com` unless Bryan later requests a change.
- Public GitHub account: `bryan890115`.
- The layout must work without a portrait; reuse the current image only if it is still current and approved.
- The primary design is research-first and evidence-led, not consultant-style sales copy.
- Candidate material includes the MPhil research and selected approved software, AI, data, or actuarial projects; final project facts and links require verification.
- Existing study-note URLs remain functional.

## Acceptance criteria

### Positioning and content

- **AC-001:** The home hero clearly states Bryan's current role, research focus, and Computer Science/Actuarial Studies background; `SITE UNDER CONSTRUCTION` is removed.
- **AC-002:** Public pages contain no placeholder paragraphs, repeated filler, fake availability, stale response-time promises, or unsupported consulting claims.
- **AC-003:** The home page includes a concise introduction, current focus, selected work, key capabilities, and one clear contact action.
- **AC-004:** The research page accurately explains the current problem, motivation, approach, status, and approved outputs without overstating results.
- **AC-005:** The projects page contains three to five approved entries stating the problem, Bryan's role, methods or stack, and a concrete outcome or learning; links are public and verified.
- **AC-006:** The about page contains current education, research, teaching or relevant experience, and concise technical skills without generic self-praise.
- **AC-007:** The contact page provides only approved channels and removes guaranteed response times or consulting availability unless explicitly confirmed.

### Design and experience

- **AC-008:** Primary pages share one coherent system for typography, spacing, navigation, cards, buttons, and footer.
- **AC-009:** Navigation and layouts work at 360 px, 768 px, and 1440 px without horizontal scrolling.
- **AC-010:** Pages use semantic landmarks, a skip link, descriptive headings and alt text, visible focus, sufficient contrast, and keyboard-operable interactions.
- **AC-011:** Interactive content uses semantic links, buttons, or disclosures instead of click-only `<div>` elements; retained dialogs manage focus and Escape correctly.
- **AC-012:** Images are appropriately sized, dimensioned where practical, and lazy-loaded below the fold; unnecessary third-party assets and scripts are removed.

### Maintainability and deployment

- **AC-013:** Shared Jekyll layouts/includes or equivalent partials replace duplicated headers, navigation, metadata, and footers on primary pages.
- **AC-014:** Existing public routes and study-note links continue to resolve or have explicit redirects.
- **AC-015:** Primary pages include title, description, canonical, Open Graph, and minimal verified Person JSON-LD metadata.
- **AC-016:** The repository has reproducible local build instructions and an automated broken-link and placeholder-text check.
- **AC-017:** Tracked `_site/` output is removed while `.gitignore` continues to exclude generated output.
- **AC-018:** Implementation is delivered on a non-default branch through a draft pull request and is not merged or deployed by Codex.

## Final quality gates

1. `bundle exec jekyll build --trace` succeeds.
2. Site validation reports zero broken internal links and zero forbidden placeholder phrases.
3. Navigation, calls to action, email, project, and study-note links are manually checked from the built site.
4. Keyboard-only navigation reaches all controls in logical order with visible focus.
5. Home, research, projects, about, and contact are checked at 360 px, 768 px, and 1440 px.
6. Primary pages have no uncaught browser console errors.
7. Home-page Lighthouse targets are at least 90 Performance and 95 Accessibility, Best Practices, and SEO, or an environment exception is evidenced and approved.
8. No public page contains `SITE UNDER CONSTRUCTION`, `Placeholder`, repeated filler, a hard-coded 2024 footer, or an unverified professional claim.
9. Bryan reviews all changed public content before merge.
