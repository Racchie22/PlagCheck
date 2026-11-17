# Project Proposal – PlagCheck

## 1. Problem statement
Manually checking whether an academic document contains text that overlaps with other documents can be slow and inconsistent. Students and reviewers need a simple way to compare text and see where similar wording occurs.

## 2. Proposed solution
PlagCheck will be a web application built with Python and Streamlit. A user will provide two pieces of text or upload a document. The application will preprocess the text, calculate similarity using TF-IDF vectors and cosine similarity, and present an overall similarity score. Later increments will add sentence-level matching, document uploads, comparison against a local document collection, history and downloadable reports.

## 3. Objectives
- Provide a simple interface for comparing text.
- Explain similarity results in an understandable way.
- Support common document formats (TXT, PDF and DOCX).
- Maintain a local history of checks.
- Apply Agile practices through backlog planning, incremental delivery, testing, review and retrospective.

## 4. Initial scope
**Included:** text-to-text comparison; TF-IDF and cosine similarity; sentence-level overlap indicators; TXT/PDF/DOCX extraction; comparison against documents stored by the app; SQLite history; basic dashboard and PDF report.

**Not included in the initial version:** searching the public internet, institutional repository integration, source attribution across the web, or definitive automated decisions about academic misconduct.

## 5. Proposed technology
- Language: Python
- Interface: Streamlit
- Similarity: scikit-learn (TF-IDF and cosine similarity)
- Document extraction: pypdf and python-docx
- Storage: SQLite
- Testing: Pytest
- Version control and CI: Git, GitHub and GitHub Actions

## 6. Expected outcome
A working local web application that compares user-provided documents and reports textual similarity with clear limitations. The project will also provide evidence of the team's Agile process through genuine planning artefacts, incremental commits, tests and reviews.

## 7. Risks and mitigations
| Risk | Mitigation |
|---|---|
| PDF text extraction may fail for scanned/image-only PDFs | Explain the limitation and accept text-based PDFs in the first version |
| Similarity score may be misunderstood | Display an explanation that similarity is not proof of plagiarism |
| Common phrases may inflate similarity | Show matching passages and document limitations |
| Short project deadline | Prioritise a working core comparison before optional features |
| Integration conflicts | Use small modules, Git branches/pull requests where practical, and regular integration |

## 8. Success criteria
- User can compare two text inputs and receive a similarity score.
- Invalid or empty input is handled with a clear message.
- Matching sentence indicators are understandable.
- Supported document types can be parsed in the completed version.
- Automated tests cover core text processing and similarity behaviour.
- Project documentation accurately records completed work and known limitations.

## 9. Agile approach
The team intends to use a Scrum-inspired workflow with a prioritised product backlog, short implementation increments, reviews and retrospectives. Kanban-style task tracking and WIP limits will be used where helpful. Because the academic submission deadline is short, actual execution dates may be compressed; planned sprint durations will not be presented as elapsed time.
