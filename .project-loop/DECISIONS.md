# Project Decisions

## DEC-001 — Approve the COMP6713 public-edition scope

State: APPROVED  
Date: 2026-08-04  
Decision owner: Bryan Jen

### Context

D-0001 completed a private, read-only eligibility audit of Bryan's COMP6713 material. The audit inspected 255 associated files, including 133 Markdown note bodies. Filesystem evidence did not certify any file for direct publication because authorship metadata was incomplete and much of the material closely followed official slides, tutorials, notebooks, or other permission-sensitive sources.

The private packet classified:

- 0 files as publishable as-is;
- 97 candidate notes as potentially usable only after Bryan confirms authorship and the public edition is independently rewritten;
- 53 files as official, third-party, or permission-sensitive; and
- 105 files as restricted, assessment-related, duplicate, private-metadata, or otherwise excluded.

Bryan reviewed the private packet and explicitly approved the publication decisions below.

### Decision

1. Bryan confirms that the 97 candidate notes are his own synthesis. They may be used only as private conceptual input for an independently authored public edition; they may not be exported, copied, lightly paraphrased, or treated as publishable source text.
2. All nine proposed modules are approved for the public-edition implementation:
   - Foundations of NLP
   - Representation Learning
   - Attention and Transformers
   - Modern Language Models
   - Sentiment Analysis
   - Sequence Tagging
   - Machine Translation
   - Summarisation and Question Answering
   - NLP Applications and Responsible Deployment
3. The approved public title is:

   `COMP6713 Natural Language Processing — Personal Study Notes`
4. The approved disclaimer is:

   `These are Bryan Jen’s personal study notes for COMP6713 Natural Language Processing. They are not official UNSW course materials and are not endorsed by UNSW. Assessment questions, solutions, marking guidance, restricted course content, and copied teaching materials are intentionally excluded. Any errors are my own.`
5. The approved module order and routes are:
   - `/study-notes/comp6713/notes/foundations-of-nlp.html`
   - `/study-notes/comp6713/notes/representation-learning.html`
   - `/study-notes/comp6713/notes/attention-and-transformers.html`
   - `/study-notes/comp6713/notes/modern-language-models.html`
   - `/study-notes/comp6713/notes/sentiment-analysis.html`
   - `/study-notes/comp6713/notes/sequence-tagging.html`
   - `/study-notes/comp6713/notes/machine-translation.html`
   - `/study-notes/comp6713/notes/summarisation-and-question-answering.html`
   - `/study-notes/comp6713/notes/nlp-applications-and-responsible-deployment.html`
6. The public edition must be text-and-mathematics first, with no private links and no reuse of existing code, outputs, datasets, trained models, tables, screenshots, PDFs, diagrams, course attachments, or other raw assets.
7. Newly authored code examples are approved when pedagogically useful. Every executable example must be minimal, independently written, tested, use synthetic data, require no credentials or network access, and must not derive from course notebooks, assignments, solutions, team projects, saved outputs, or private datasets.
8. Mathematics must be independently re-derived and checked. The implementation must not copy formula explanations or worked examples from the private vault or official material.
9. A local source-similarity, technical-accuracy, citation/attribution, privacy, and assessment-integrity review is required before the implementation may be accepted. Private source files and overlap excerpts must remain outside GitHub; only public-safe aggregate results may be recorded.
10. The following exclusions are permanent for this publication cycle:
    - official slides, tutorials, handouts, notebooks, attachments, and solutions;
    - assignment specifications, assessment questions, rubrics, answers, project code, and examination preparation;
    - textbooks, copied readings, third-party diagrams/tables/code, and unclear-permission material;
    - the mixed examination/course-recap note;
    - archived duplicates, hidden artifacts, private metadata, private communications, and student data; and
    - the entire team-assessment collection.

### Consequences

- M-001's private discovery and approval dependency is satisfied.
- M-002 may implement all nine modules as a clean public edition under D-0002.
- Public prose, equations, examples, code, tables, and structure must be independently authored rather than transformed from the private files.
- No excluded material, private evidence, private path, raw file, existing asset, or assessment content may enter GitHub or the built site.
- PR #13 remains draft. Codex and the Project Director must not merge or deploy.

### Affected acceptance criteria, milestones, and directives

- Acceptance criteria: AC-002 through AC-012
- Accepted milestone: M-001
- Active milestone: M-002
- Completed directive: D-0001
- Active directive: D-0002

The completed professional-portfolio redesign decisions remain archived under:

`.project-loop/archive/2026-08-04-professional-portfolio-redesign/DECISIONS.md`
