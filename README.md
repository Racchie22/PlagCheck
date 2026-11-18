# PlagCheck – Smart Plagiarism Detection System

PlagCheck is a student-built web application for checking textual similarity between documents. The current application compares two user-provided text samples.

## Current project status
**Sprint 1:** Core text comparison is implemented. The user has run the Sprint 1 tests successfully and confirmed the app launches and produces a comparison result.

**Sprint 2:** Sentence-level matching (US04) is under implementation and local validation.

## Current functionality
- Enter two text samples in the Streamlit interface.
- Validate that both text boxes contain text.
- Normalise text by lowercasing, replacing punctuation and collapsing whitespace.
- Calculate an overall similarity percentage using TF-IDF and cosine similarity.
- Split text into sentences and find the closest sentence in Text 2 for each sentence in Text 1.
- Display sentence pairs whose similarity is at least 50%.
- Explain that similarity is not proof of plagiarism.

## Sentence matching rule
Sentence matching uses TF-IDF vectors and cosine similarity. For each sentence in Text 1, the application selects its most similar sentence in Text 2. A pair is displayed when its score is at least 50%. This is a heuristic threshold for inspecting possible overlap, not a plagiarism verdict. A sentence may be paired with the same Text 2 sentence as another sentence in Text 1.

## Planned later features
- Upload TXT, PDF and DOCX documents.
- Compare against documents stored in the application.
- Save check history in SQLite.
- Dashboard and downloadable report.

## Scope and limitations
The application checks similarity only between text supplied to it. It does not search the entire internet. A similarity score is an indicator of textual overlap, not a final judgement of plagiarism or academic misconduct. Sentence splitting currently uses common punctuation (period, question mark and exclamation mark); abbreviations and complex formatting may need more advanced handling later.

## Technology
Python, Streamlit, scikit-learn, SQLite, Pytest, pypdf and python-docx.

## Run locally
1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m pytest -q`
4. Start the app: `streamlit run app.py`

## Repository structure
- `app.py` – Streamlit application
- `modules/preprocessing.py` – text normalisation
- `modules/similarity.py` – overall TF-IDF similarity
- `modules/matching.py` – sentence-level matching
- `tests/` – automated tests
- `docs/` – project and Agile artefacts

See [project proposal](docs/project_proposal.md), [user stories](docs/user_stories.md), [product backlog](docs/product_backlog.md) and [execution log](docs/agile_execution_log.md).
