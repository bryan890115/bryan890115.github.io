# Project Reviews

## R-0001 — M-001 shared foundation and home page

Timestamp: `2026-08-03T18:49:00+10:00`  
Directive ID: D-0001  
Milestone ID: M-001  
Pull request: `#11` (`agent/professional-portfolio-redesign`)  
Exact reviewed head SHA: `0f7408e0fbe1fba5ac76f373711f7eef1e89e4c6`  
Verdict: CONTINUE

### Evidence inspected

- PR #11 metadata, description, exact head, changed-file list, and `CODEX_READY` comment.
- Full PR diff and the exact-head versions of `.project-loop/STATUS.md`, `.project-loop/PLAN.md`, `.project-loop/DIRECTIVE.md`, shared Jekyll layout/includes, `_config.yml`, home page, CSS, JavaScript, site-check configuration, checker implementation, and checker tests.
- Codex-reported local validation: bundle installation, Jekyll build, site checker, nine unit tests, YAML load, JavaScript syntax check, responsive/browser checks, and `git diff --check`.
- GitHub status and workflow queries for the reviewed head; no Actions workflow runs or status checks were attached.
- An independent local checkout/rerun was attempted by the Project Director but could not proceed because the review environment could not resolve `github.com`.

### Acceptance-criteria results

- **AC-001 — PASS:** The home page uses the approved MPhil research positioning and removes `SITE UNDER CONSTRUCTION`.
- **AC-003 — PASS:** The home page contains a concise introduction, current focus, selected work, capabilities, and direct contact action.
- **AC-008 — PASS for M-001:** The primary routes share one coherent design system and page shell.
- **AC-009 — PASS on reported evidence:** Codex recorded responsive checks at 360 px, 768 px, and 1440 px with no horizontal overflow.
- **AC-010 — PASS for M-001:** Semantic landmarks, skip link, visible focus styling, native links/buttons, reduced-motion support, and compact-navigation Escape/focus restoration are implemented. A final human keyboard pass remains appropriate.
- **AC-013 — PASS:** Shared Jekyll layouts/includes replace duplicated metadata, header, navigation, and footer structure.
- **AC-015 — PASS:** Central title, description, canonical, Open Graph, and Person JSON-LD support is present.
- **AC-016 — PASS on reported evidence:** Local build instructions, the standard-library site checker, narrow exemptions, and unit tests are present.

### Findings

No critical or important implementation defect was found.

Minor follow-up items:

1. The visual-evidence files named in `STATUS.md` were not attached to the pull request, so their contents were not independently inspected through GitHub.
2. No GitHub Actions/status checks exist yet for this head. This is acceptable for M-001 because CI is planned in M-004, but Codex's command results remain reported local evidence rather than CI evidence.
3. The skip-link and primary-CTA Tab/Enter path should receive a human keyboard pass before final release.
4. Legacy project/research modal accessibility and placeholder content remain visible debt, but their replacement is explicitly assigned to M-002 and is not a defect in the bounded M-001 slice.

### Strategic approach assessment

The implementation remains the smallest safe route to the approved outcome. The shared Jekyll foundation is suitable for staged content replacement, avoids a framework migration, preserves routes, and makes deferred placeholder debt explicit through exact-path checker exemptions.

After this review, Bryan authorized Codex to inspect accessible OneDrive project material to prepare candidate content. Because the repository and PR are public, OneDrive material must remain read-only discovery input until Bryan approves exact publishable summaries, assets, and links. Bryan's requested extra placeholder is therefore recorded as a private TODO reminder only, not a public website card.

### Single next action

Codex must execute active D-0002: inspect accessible OneDrive and repository evidence, return a private research/project approval packet with three to five candidates plus one non-public future-upload TODO, and make no public content changes until Bryan approves the exact material.
