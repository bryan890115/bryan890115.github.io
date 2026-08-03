# Website Professional Redesign Specification

Protocol version: 1  
State: DRAFT  
Repository: `bryan890115/bryan890115.github.io`  
Default branch: `main`  
Planning branch: `agent/professional-portfolio-redesign-plan`  
Approval state: PENDING USER APPROVAL  
Draft date: 2026-08-03  
Base SHA: `c18d372f2e0dad67a03eba0016ae2ea1f4ac4651`

## Goal

Transform the current GitHub Pages site into a credible, modern, and maintainable professional portfolio that presents Bryan Jen as a research-focused computer scientist with an Actuarial Studies background. The site should make Bryan's current work, technical capability, and contact path understandable within one minute, without placeholder content or unsupported professional claims.

## Intended audience

1. Academic supervisors, research collaborators, and prospective research partners.
2. Technical recruiters and employers evaluating software, data, AI, and quantitative experience.
3. Students and peers looking for research, project, or study-note material.

## Recommended positioning

The site should lead with Bryan's current research identity rather than broad consulting language:

> MPhil researcher working on natural-language interfaces for semantic building data, with a background in Computer Science and Actuarial Studies.

This wording is an approval-time assumption. It must be corrected before implementation if Bryan's preferred title, program wording, institution wording, or research description differs.

## Goals

- Present a clear and current professional identity on the home page.
- Replace generic and placeholder content with concise, evidence-backed material.
- Highlight current research, selected technical projects, education, teaching, and core skills.
- Use a restrained visual system suitable for an academic and technical portfolio.
- Preserve the existing GitHub Pages deployment model and important public URLs.
- Improve accessibility, responsive behaviour, metadata, performance, and maintainability.

## Non-goals

- Building a CMS, database, authentication system, or backend service.
- Adding a contact form that stores or transmits user data.
- Adding analytics, advertising, tracking pixels, or marketing automation.
- Inventing publications, project outcomes, client work, employment, metrics, or credentials.
- Publishing private coursework, private repositories, confidential research, or assessment material without explicit approval.
- Rewriting the substantive contents of the existing study notes in this redesign.
- Migrating to React, Next.js, or another application framework.
- Merging to `main` or deploying without Bryan's final approval.

## Constraints

- Remain compatible with GitHub Pages and Jekyll.
- Prefer HTML, Liquid, CSS, and minimal vanilla JavaScript.
- Preserve or redirect existing routes including `/`, `/pages/about.html`, `/pages/projects.html`, `/pages/research.html`, `/pages/contact.html`, and `/study-notes/`.
- Use only verified, user-approved claims and links.
- Keep personal information limited to details Bryan explicitly chooses to publish.
- The design must work at 360 px, 768 px, and 1440 px viewport widths.
- Interactive elements must be keyboard operable and visibly focusable.
- Generated Jekyll output must not be edited as source or committed as part of normal development.

## Assumptions

- Bryan's current public email remains `bryan890115@gmail.com` unless corrected during approval.
- The GitHub account `bryan890115` may be linked publicly.
- The existing profile image may be reused only if Bryan considers it current and professional; otherwise the design must work without a portrait.
- The primary design direction is research-first and evidence-led, not consultant-style sales copy.
- Candidate portfolio material includes Bryan's MPhil research on natural-language interfaces for semantic building data and selected approved software, AI, data, or actuarial projects. Final project selection and public links must be verified before publication.
- Existing study-note URLs should remain functional even if their visual treatment is only lightly updated.

## Acceptance criteria

### Positioning and content

- **AC-001:** The home-page hero states Bryan's current role, research focus, and Computer Science/Actuarial Studies background in clear, specific language; `SITE UNDER CONSTRUCTION` is removed.
- **AC-002:** No public portfolio page contains placeholder paragraphs, duplicated filler, fake availability statements, stale response-time promises, or unsupported consulting claims.
- **AC-003:** The home page includes a concise introduction, current focus, selected work, key capabilities, and one clear contact action.
- **AC-004:** The research page accurately explains Bryan's current research problem, motivation, approach, present status, and approved outputs or links without overstating results.
- **AC-005:** The projects page contains three to five approved, evidence-backed project entries. Each entry states the problem, Bryan's role, methods or stack, and a concrete outcome or learning; links appear only when the target is public and verified.
- **AC-006:** The about page contains current education, research, teaching or relevant experience, and a concise technical-skills summary without generic self-praise.
- **AC-007:** The contact page provides only approved channels and removes claims such as guaranteed response times or open consulting availability unless Bryan explicitly confirms them.

### Design and experience

- **AC-008:** All primary pages use one coherent visual system with consistent typography, spacing, navigation, cards, buttons, and footer treatment.
- **AC-009:** Navigation and page layouts remain usable without horizontal scrolling at 360 px, 768 px, and 1440 px widths.
- **AC-010:** Pages use semantic landmarks, a skip link, descriptive headings, descriptive alternative text, visible keyboard focus, sufficient contrast, and keyboard-operable interactions.
- **AC-011:** Clickable content is implemented with links, buttons, or accessible disclosure elements rather than click-only `<div>` elements. Any retained dialog has correct focus management and escape behaviour.
- **AC-012:** Images are appropriately sized, have explicit dimensions where practical, and are lazy-loaded below the fold. Unnecessary third-party assets and scripts are removed.

### Maintainability and deployment

- **AC-013:** Shared Jekyll layouts/includes or equivalent reusable partials replace duplicated headers, navigation, metadata, and footers across the primary portfolio pages.
- **AC-014:** Existing public routes and study-note links continue to resolve, or an explicit redirect is supplied.
- **AC-015:** Page titles, descriptions, canonical metadata, Open Graph metadata, and a minimal verified Person JSON-LD block are present on primary pages.
- **AC-016:** The repository has reproducible local build instructions and an automated check that catches broken internal links and obvious placeholder text.
- **AC-017:** Tracked generated `_site/` content is removed from source control while `.gitignore` continues to exclude future build output.
- **AC-018:** The final implementation is delivered on a non-default branch through a draft pull request and is not merged or deployed by Codex.

## Final quality gates

1. `bundle exec jekyll build --trace` completes successfully.
2. The repository's site-validation command completes with zero broken internal links and zero forbidden placeholder phrases.
3. Primary navigation, call-to-action links, email links, project links, and study-note links are manually checked from the built site.
4. Keyboard-only navigation reaches all interactive elements in a logical order with visible focus.
5. Home, research, projects, about, and contact pages are visually checked at 360 px, 768 px, and 1440 px.
6. There are no uncaught browser console errors on the primary pages.
7. Lighthouse targets on the built home page are at least 90 Performance and 95 Accessibility, Best Practices, and SEO, or any environment-caused exception is documented with evidence and approved.
8. No public page contains `SITE UNDER CONSTRUCTION`, `Placeholder`, repeated filler copy, an outdated hard-coded 2024 footer, or an unverified professional claim.
9. All changed content is reviewed by Bryan before merge.
