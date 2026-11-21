# PlagCheck – Smart Plagiarism Detection System

PlagCheck is a student-built Streamlit application for checking textual similarity between text samples and uploaded documents. It uses TF-IDF vectorisation and cosine similarity to identify textual overlap and likely matching sentences.

## Project status

| Sprint | Deliverable | Status |
|---|---|---|
| Sprint 1 | Core text comparison and preprocessing | Complete |
| Sprint 2 | Sentence-level matching | Complete |
| Sprint 3 | Document upload and local collection comparison | Complete |
| Sprint 4 | SQLite history, dashboard and PDF reports | Complete |
| Sprint 5 | Stabilisation, CI and final documentation | Planned |

## Current functionality

### Text comparison
- Enter two text samples in the Streamlit interface.
- Validate that both inputs contain text.
- Preprocess text by lowercasing, replacing punctuation and normalising whitespace.
- Calculate an overall similarity percentage using TF-IDF and cosine similarity.

### Sentence-level matching
- Split text into sentences using common sentence-ending punctuation.
- For each sentence in Text 1, find its closest sentence in Text 2.
- Display sentence pairs that meet the default 50% similarity threshold.
- Handle whitespace and line breaks commonly introduced during PDF text extraction.

### Document upload and comparison
- Upload TXT, PDF and DOCX documents.
- Extract text using pypdf and python-docx.
- Add documents to a local document collection.
- Compare an uploaded document against readable documents in that collection.
- Rank results by similarity percentage.
- Display the closest matching document and matching sentence pairs.

### Automated testing
- Pytest coverage for preprocessing, similarity calculation, sentence matching, document extraction and document storage.
- Includes a multi-page PDF extraction test.
- Latest user-reported local test result: **35 tests passed**.

## Technology stack

- Python
- Streamlit
- scikit-learn
- TF-IDF and cosine similarity
- pypdf
- python-docx
- Pytest
- ReportLab (dependency included for PDF report work planned in Sprint 4)
- SQLite (planned for Sprint 4)

## Run locally

1. Create and activate a Python virtual environment.
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m pytest -v`
4. Start the app: `streamlit run app.py`

## Repository structure

```text
PlagCheck/
├── app.py
├── requirements.txt
├── README.md
├── modules/
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── matching.py
│   ├── document_reader.py
│   └── document_store.py
├── data/
│   └── documents/
│       └── .gitkeep
├── tests/
│   ├── test_preprocessing.py
│   ├── test_similarity.py
│   ├── test_matching.py
│   ├── test_document_reader.py
│   └── test_document_store.py
└── docs/
    ├── agile_execution_log.md
    ├── github_project_board_setup.md
    ├── product_backlog.md
    ├── project_proposal.md
    ├── team_onboarding.md
    └── user_stories.md
```

## Scope and limitations

- PlagCheck compares user-provided text and documents against a local collection. It does not search the entire internet.
- Similarity scores indicate textual overlap; they are not proof of plagiarism or academic misconduct.
- TF-IDF is based on word usage and does not understand meaning like a semantic language model.
- The sentence-matching threshold is heuristic. Each sentence in Text 1 is matched independently to its closest sentence in Text 2, so multiple sentences may select the same match.
- Scanned/image-only PDFs may not provide extractable text because OCR is not currently implemented.
- Documents added to the local collection are excluded from Git tracking.

## Project documentation

- [Project Proposal](docs/project_proposal.md)
- [User Stories](docs/user_stories.md)
- [Product Backlog](docs/product_backlog.md)
- [Agile Execution Log](docs/agile_execution_log.md)
- [GitHub Project Board Setup](docs/github_project_board_setup.md)
