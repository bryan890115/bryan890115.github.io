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

## R-0002 — M-002 private content-discovery gate

Timestamp: `2026-08-03T20:55:00+10:00`  
Directive ID: D-0002  
Milestone ID: M-002  
Pull request: `#11` (`agent/professional-portfolio-redesign`)  
Exact reviewed head SHA: `3675b996628ff738ce9002b5c41a074a9cf5bc47`  
Verdict: CONTINUE

### Evidence inspected

- Exact branch and PR head metadata.
- `.project-loop/STATUS.md` at the reviewed head.
- The comparison from D-0002's starting head `51644f5492c538cbc5f3d6c539138368d5a12daa` to the reviewed head, showing one commit and only `.project-loop/STATUS.md` changed.
- The generic `CODEX_APPROVAL_REQUIRED D-0002` PR notification.
- Bryan's explicit approval of the private D-0002 candidate packet and Codex's conservative publication decisions.

The Project Director did not copy, request, or publish the private packet contents. Bryan reviewed and approved that private material directly.

### Acceptance-criteria results

- **M-002 discovery gate — PASS:** Codex reports fifteen candidates evaluated, five shortlisted, and a private approval packet delivered.
- **Privacy boundary — PASS:** Repository comparison shows only the non-sensitive status file changed during D-0002; no public page, asset, candidate detail, private path, raw file, or reminder was committed.
- **Content approval dependency — PASS:** Bryan approved the private research summary, selected general-project candidates, and conservative publication decisions.
- **AC-002, AC-004, AC-005, AC-011, AC-012, AC-014 — NOT YET IMPLEMENTED:** These remain assigned to the public implementation slice in D-0003.

### Findings

No critical or important defect was found in the discovery and approval gate.

The durable public handoff intentionally does not contain private evidence or candidate notes. D-0003 therefore authorizes only the exact public-facing content marked approved in the private D-0002 packet. If Codex cannot unambiguously recover that approved set, it must stop rather than reconstruct it from private evidence or guess.

### Strategic approach assessment

Separating private evidence discovery from public implementation remains the safest and smallest route. It allows evidence-backed project selection without exposing OneDrive material in the public repository. The approved conservative publication set can now replace the site's generic and placeholder research/project content.

### Single next action

Codex must execute active D-0003 on the existing branch and draft PR: implement only the approved research summary and selected general-project cards, remove the corresponding placeholders and weak modal behavior, validate the result, and keep all private discovery evidence outside GitHub.
