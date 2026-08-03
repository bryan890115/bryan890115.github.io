# Project Reviews

## R-0001 — M-001 shared foundation and home page

Timestamp: `2026-08-03T18:49:00+10:00`  
Directive ID: D-0001  
Milestone ID: M-001  
Pull request: `#11`  
Exact reviewed head SHA: `0f7408e0fbe1fba5ac76f373711f7eef1e89e4c6`  
Verdict: CONTINUE

### Result

M-001 was accepted. The shared Jekyll shell, research-first home page, responsive design system, compact navigation, metadata, documentation, checker, and unit tests satisfied the bounded milestone. No critical or important defect was found.

### Deferred evidence and work

- GitHub Actions/status checks were not yet present; CI remained assigned to M-004.
- A final human skip-link and primary-CTA keyboard pass remained appropriate.
- Research and project placeholder/modal debt remained assigned to M-002.

### Next action

Execute D-0002 as a private discovery gate for evidence-backed research and project content without exposing OneDrive material.

## R-0002 — M-002 private content-discovery gate

Timestamp: `2026-08-03T20:55:00+10:00`  
Directive ID: D-0002  
Milestone ID: M-002  
Pull request: `#11`  
Exact reviewed head SHA: `3675b996628ff738ce9002b5c41a074a9cf5bc47`  
Verdict: CONTINUE

### Result

The private discovery gate was accepted. Repository comparison showed that D-0002 changed only `.project-loop/STATUS.md`; no private project detail, OneDrive path, raw file, private link, candidate note, or reminder entered GitHub. Bryan approved the private research summary, selected project candidates, and conservative publication decisions.

### Next action

Execute D-0003 to implement only the exact public-facing research and project content approved in the private packet.

## R-0003 — M-002 research and project implementation

Timestamp: `2026-08-03T23:50:00+10:00`  
Directive ID: D-0003  
Milestone ID: M-002  
Pull request: `#11`  
Exact reviewed head SHA: `c4c262c3f431e1a32d40ef11b9e8ea1f05fd9157`  
Implementation commit SHA: `8b0ce3e35e210c10fd6f6b5096c9662542c0dafe`  
Verdict: CONTINUE

### Evidence inspected

- Exact PR head, description, changed files, and `CODEX_READY D-0003` notification.
- Exact-head Research, Projects, shared CSS, status, checker policy, and checker regression test.
- Two public project link targets.
- Codex-reported build, checker, unit-test, privacy/placeholder scan, route, responsive, keyboard-focus, and browser-console evidence.
- GitHub status/workflow queries; no Actions checks existed yet.

### Acceptance results

- **AC-002 — PASS for M-002:** Scoped placeholder, filler, fake consulting, hidden-detail, and invented-outcome content was removed.
- **AC-004 — PASS:** Research accurately presents the problem, motivation, staged approach, current status, and no-public-output treatment.
- **AC-005 — PASS:** Exactly five approved projects include purpose, contribution, methods, and outcome or learning; two links are verified and three no-link treatments are intentional.
- **AC-011 — PASS:** Semantic articles and native links replace click-only cards and the modal.
- **AC-012 — PASS for M-002:** Text-first presentation adds no unapproved image or private evidence asset.
- **AC-014 — PASS on reported evidence:** Required routes built non-empty with no broken internal reference.

No critical or important defect was found. M-002 was accepted.

### Next action

Execute D-0004 to rewrite About and Contact using approved/public evidence, preserve study-note routes, remove the portrait from those pages, and reduce checker exemptions to zero.

## R-0004 — M-003 About, Contact, and study-note integration

Timestamp: `2026-08-04T00:32:00+10:00`  
Directive ID: D-0004  
Milestone ID: M-003  
Pull request: `#11`  
Exact reviewed head SHA: `e9a4dbba3ec2a06beffb49237e67f3f920226ae1`  
Implementation commit SHA: `812c41dcd836b67a626b69677d2a67088b1ed651`  
Verdict: CONTINUE

### Evidence inspected

- PR #11 exact head, open/draft/mergeable state, updated description, and `CODEX_READY D-0004` notification.
- Exact-head `pages/about.html`, `pages/contact.html`, `pages/study-notes.html`, `.project-loop/STATUS.md`, `site-check.json`, and checker regression test.
- D-0004 implementation commit replacing legacy About and Contact content.
- Codex-reported build, checker, nine unit tests, JavaScript syntax, Python compilation, forbidden-copy scan, portrait scan, route checks, responsive/browser checks, keyboard-focus checks, and console results.
- GitHub status and workflow queries for the reviewed head; no Actions workflow or status check was attached.
- Bryan's explicit confirmation during review that he requested and approves the exact LinkedIn URL implemented on Contact; recorded in DEC-002.

### Acceptance results

- **AC-002 — PASS:** About and Contact contain no placeholder, generic self-praise, consulting offer, availability promise, response-time guarantee, mentorship/networking claim, or marketing-style inquiry copy.
- **AC-006 — PASS:** About uses the approved MPhil positioning, Computer Science and Actuarial Studies background, accepted research/projects evidence, and directly evidenced capabilities without adding institution, date, mark, employment, teaching, credential, location, award, or collaborator claims.
- **AC-007 — PASS:** Contact exposes only the explicitly approved email, GitHub, and LinkedIn channels and makes no response or availability promise.
- **AC-008 — PASS:** About, Contact, and the study-note compatibility page use the shared design system without page-specific inline styling.
- **AC-009 — PASS on reported evidence:** About and Contact were checked at 360, 768, and 1440 px without overflow or overlap.
- **AC-010 — PASS on reported evidence:** Semantic headings and native links are keyboard focusable; compact navigation Escape and focus restoration were exercised; no portrait remains on the scoped pages.
- **AC-014 — PASS on reported evidence:** About, Contact, compatibility study notes, canonical study notes, and a representative note route built and loaded non-empty.

### Findings

No critical or important defect was found.

The LinkedIn link initially exceeded D-0004's two-channel wording, but Bryan explicitly confirmed that he requested and approves the exact URL. DEC-002 resolves the deviation without approving any LinkedIn-derived biography or profile claims.

Minor final-release items:

1. Validation and browser evidence remains local rather than attached CI evidence.
2. GitHub Actions/status checks are still absent and must be added and pass under M-004.
3. Full-site release-candidate visual, keyboard, metadata, performance, and final factual approval remain outstanding.

### Strategic assessment

The implementation is restrained and evidence-backed. It removes all remaining checker exemptions and unsupported public profile content while preserving the accepted research, project, and study-note routes. M-003 is accepted.

### Next action

Execute active D-0005 for M-004: remove tracked generated output, add PR-only CI, complete full-site release-candidate QA and documentation, attach reviewable evidence, and request Bryan's final factual and visual approval. Do not merge or deploy.
