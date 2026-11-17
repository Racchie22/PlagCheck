# PlagCheck – Smart Plagiarism Detection System

PlagCheck is a student-built web application for checking textual similarity between documents. The first increment compares two user-provided text samples.

## Current project status
**Sprint 1 – implementation and validation.** The text comparison interface, preprocessing module, TF-IDF similarity engine and automated test cases have been added. Test execution and manual application validation are still pending.

## Sprint 1 functionality
- Enter two text samples in the Streamlit interface.
- Validate that both text boxes contain text.
- Normalise text by lowercasing, replacing punctuation and collapsing whitespace.
- Calculate a similarity percentage using TF-IDF and cosine similarity.
- Display an explanation that similarity is not proof of plagiarism.
- Run automated tests for preprocessing and similarity behaviour.

## Planned later features
- Identify matching sentences or passages.
- Upload TXT, PDF and DOCX documents.
- Compare against documents stored in the application.
- Save check history in SQLite.
- Dashboard and downloadable report.

## Scope and limitations
The first version checks similarity only between text supplied to the application. It does not search the entire internet. A similarity score is an indicator of textual overlap, not a final judgement of plagiarism or academic misconduct. Quoted text, references, common phrases and document context can affect the score.

## Technology
Python, Streamlit, scikit-learn, SQLite, Pytest, pypdf and python-docx.

## Run locally
1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest`
4. Start the app: `streamlit run app.py`

## Repository structure
- `app.py` – Streamlit application
- `modules/preprocessing.py` – text normalisation
- `modules/similarity.py` – TF-IDF and cosine similarity
- `tests/` – automated tests
- `docs/` – project and Agile artefacts

See [project proposal](docs/project_proposal.md), [user stories](docs/user_stories.md), [product backlog](docs/product_backlog.md) and [execution log](docs/agile_execution_log.md).
