# Current Codex Directive

Directive ID: D-0002  
Status: ACTIVE  
Milestone ID: M-002  
Repository: `bryan890115/bryan890115.github.io`  
Intended implementation branch: `agent/professional-portfolio-redesign`  
Base SHA: `22db5223a0ec1c59500b9371aa33960f04711fa6`  
Issued timestamp: `2026-08-03T18:49:00+10:00`  
Replaced directive ID: D-0001

## Context

R-0001 accepted M-001 at PR #11 head `0f7408e0fbe1fba5ac76f373711f7eef1e89e4c6`. Bryan has stated that Codex can access OneDrive material containing some of his projects and has asked for one additional reminder entry so he remembers to upload more projects later.

The GitHub repository, branch, pull request, comments, and commit history are public. OneDrive material is therefore approved for **read-only discovery**, not automatic public disclosure. Bryan must approve the exact summaries, claims, assets, and links before any OneDrive-derived content is committed to the public branch or displayed on the website.

## Required outcome

Inspect the accessible OneDrive project material and existing repository evidence, then return a private approval packet to Bryan containing:

1. A proposed research-page factual summary.
2. Three to five strongest candidate project case studies.
3. One non-public TODO reminder: `Future project — upload supporting material to OneDrive`.
4. A clear list of any facts, outcomes, links, images, or privacy questions that require Bryan's decision.

Do not modify the public research or projects pages in this directive. This directive is the content-discovery and approval gate for M-002.

## In-scope work

1. Pull the current `agent/professional-portfolio-redesign` branch. Before making any change, record its exact current head as `Starting SHA` in `.project-loop/STATUS.md`. Verify that it is a descendant of this directive's base SHA and that the intervening changes are only Director-owned `.project-loop/PLAN.md`, `.project-loop/REVIEW.md`, and `.project-loop/DIRECTIVE.md` updates.
2. Inspect OneDrive material that is clearly Bryan's project work and relevant to a professional technical/research portfolio.
3. Inspect existing repository material needed to corroborate public routes, existing study notes, and already-public GitHub links.
4. Select three to five candidate projects using these criteria:
   - relevance to research, software, AI/data, quantitative, actuarial, or technical work;
   - clear evidence of Bryan's own contribution;
   - enough material to state the problem, role, methods, and outcome or learning accurately;
   - no obvious confidentiality, assessment-integrity, licensing, personal-data, or third-party ownership concern.
5. For each candidate, prepare in the private Codex response:
   - proposed public title;
   - one-sentence problem or purpose;
   - Bryan's role and contribution;
   - methods, technologies, or analytical approach;
   - evidence-backed result or main learning;
   - proposed public link, or `no public link`;
   - evidence source location in OneDrive or the repository;
   - privacy/licensing/assessment risks;
   - concise proposed website copy.
6. Prepare proposed research-page facts covering the problem, motivation, approach, current status, and any genuinely public outputs or links.
7. Include the exact non-public TODO reminder `Future project — upload supporting material to OneDrive` in the private approval packet only.
8. Update `.project-loop/STATUS.md` only with a non-sensitive summary such as the number of candidate projects reviewed, whether an approval packet was returned privately, validation performed, and any blocker. Do not put OneDrive paths, private titles, private URLs, raw excerpts, screenshots, or proposed confidential copy in the public status file.
9. Post only a generic PR notification such as `CODEX_APPROVAL_REQUIRED D-0002` after the private packet is delivered. Do not place the packet in the public PR description or comments.

## Explicitly out of scope

- Changing `pages/projects.html`, `pages/research.html`, home-page project content, public metadata, or built website output.
- Adding a public placeholder project card or any public `coming soon`, `placeholder`, or future-upload message.
- Copying, uploading, committing, or linking raw OneDrive files.
- Publishing private OneDrive URLs, local paths, credentials, secrets, unpublished research, private coursework, assessment questions/solutions, restricted datasets, third-party personal data, or material Bryan does not clearly own or control.
- Guessing Bryan's role, outcomes, metrics, dates, collaborators, repository links, or publication status.
- Merging PR #11 or deploying the site.

## Mapped acceptance criteria

This directive prepares evidence for AC-002, AC-004, AC-005, AC-011, AC-012, and AC-014. It does not complete those criteria and must not claim that M-002 is implemented.

## Required evidence

- Exact starting and final branch SHAs.
- Number of OneDrive candidate projects inspected and number shortlisted.
- Private approval packet delivered directly to Bryan with the required fields.
- Confirmation that the future-upload TODO appears only in the private packet.
- Confirmation that no OneDrive file, private URL, sensitive excerpt, asset, or unapproved public copy was committed or posted to GitHub.
- A concise public-safe update in `.project-loop/STATUS.md`.
- Exact command results for the validation commands below.

## Exact validation commands

Record the exact pre-work branch head in `STARTING_SHA`, then run:

```bash
git merge-base --is-ancestor 22db5223a0ec1c59500b9371aa33960f04711fa6 "$STARTING_SHA"
git diff --name-only 22db5223a0ec1c59500b9371aa33960f04711fa6..."$STARTING_SHA"
git diff --check
git status --short --branch
git diff --name-only "$STARTING_SHA"...HEAD
```

The pre-work diff from the directive base to `STARTING_SHA` must contain only Director-owned `.project-loop/PLAN.md`, `.project-loop/REVIEW.md`, and `.project-loop/DIRECTIVE.md`. The post-work diff from `STARTING_SHA` to final head must contain no public website source or OneDrive-derived asset; apart from Codex-owned `.project-loop/STATUS.md`, any unexpected file change requires escalation.

## Publication permission

Codex may continue on `agent/professional-portfolio-redesign`, commit and push a non-sensitive `.project-loop/STATUS.md` update, and update the existing draft PR with a generic readiness/approval-required notification.

Codex must not commit OneDrive-derived project content, public page changes, candidate titles, private source paths, links, images, or raw material under D-0002. Codex must not merge or deploy.

## Stop and escalate conditions

Codex must stop and report `BLOCKED` when:

- OneDrive access is unavailable or the relevant project location cannot be identified safely.
- Ownership, confidentiality, licensing, assessment integrity, or permission to publish is unclear.
- A candidate's role, methods, result, or link cannot be supported by evidence.
- Fewer than three suitable candidates can be identified without exposing private or low-quality material.
- The current branch head contains unexpected non-Director changes after the directive base SHA.
- Completing the task would require placing private information in GitHub or weakening AC-002's no-placeholder requirement.

## Next Project Director review focus

- Whether the candidate packet is evidence-backed and useful for Bryan's approval.
- Whether the strongest three to five projects were selected rather than merely the easiest files to find.
- Whether research claims are appropriately modest and current.
- Whether privacy, assessment integrity, ownership, and licensing risks were surfaced.
- Whether the future-upload reminder remained private and no public placeholder was introduced.
- Whether no OneDrive-derived material was exposed through the public repository or PR.
