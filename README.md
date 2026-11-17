# PlagCheck – Smart Plagiarism Detection System

PlagCheck is a student-built web application for checking textual similarity between documents. The initial version will compare user-provided text and uploaded documents against other documents added to the application.

## Project status
**Phase 0 – Initiation and planning.** The repository and initial planning documents are being prepared. Implementation and test results will be recorded only after the relevant work is completed.

## Planned core features
- Compare two text passages or documents.
- Calculate a similarity percentage using TF-IDF and cosine similarity.
- Identify sentences with strong textual overlap.
- Upload TXT, PDF and DOCX documents.
- Compare a submitted document against documents stored in the application.
- Save check history in SQLite.
- Generate a downloadable report.

## Scope and limitations
The first version checks similarity only against text supplied to or stored in PlagCheck. It does not search the entire internet. A similarity score is an indicator of textual overlap, not a final judgement of plagiarism or academic misconduct. Quoted text, references, common phrases and document length can affect the score.

## Planned technology
Python, Streamlit, scikit-learn, SQLite, Pytest, pypdf and python-docx.

## Run locally
1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`

The application entry point and dependencies will be completed in the implementation sprints.

## Repository structure
- `app.py` – Streamlit application entry point
- `modules/` – text processing, similarity, document parsing and database modules
- `tests/` – automated tests
- `docs/` – project and Agile artefacts
- `sample_documents/` – small sample files for local testing
- `reports/` – generated example reports (not user submissions)

## Agile working agreement
Work is planned in small increments. Each feature will have acceptance criteria, be tested, reviewed and documented before being marked complete. Sprint dates, commits, velocity and test outcomes will reflect work actually performed; planned estimates will be labelled as estimates.

See [project proposal](docs/project_proposal.md), [user stories](docs/user_stories.md), [product backlog](docs/product_backlog.md) and [execution log](docs/agile_execution_log.md).
