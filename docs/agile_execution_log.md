# Agile Execution Log

This log records actual planning and development activities. Planned work is not recorded as completed work.

## Project baseline
- Project: PlagCheck – Smart Plagiarism Detection System
- Repository: https://github.com/Racchie22/PlagCheck
- Main branch: `main`
- Current stage: Sprint 4 in progress; US07 and US09 completed, US08 pending.
- Initial implementation was carried out by the repository owner.

## Phase 0 – Planning and setup

| Activity | Status | Evidence / notes |
|---|---|---|
| Create private GitHub repository | Completed | PlagCheck repository; main branch |
| Define problem statement and scope | Completed | `docs/project_proposal.md` |
| Prepare user stories and acceptance criteria | Completed | `docs/user_stories.md` |
| Prioritise product backlog and estimates | Completed | `docs/product_backlog.md`; initial estimate: 37 points |
| Create GitHub issues for user stories | Completed | Issues #1–#10 |
| Create GitHub Project board and add issues | Completed | PlagCheck Agile Project Board |
| Confirm additional team participation | Deferred | Revisit if collaborators join |

### 18 November 2026 – Project initiation and planning
- Created the project proposal, README, requirements file, user stories, product backlog and execution log.
- Created GitHub issues #1–#10 from the user stories.
- Selected Python, Streamlit, scikit-learn, SQLite and Pytest as the planned technology stack.
- Decided to deliver text comparison first, followed by sentence matching, document comparison and reporting.

### GitHub Project board setup
- Created the PlagCheck board and added the ten user-story issues.
- Configured Backlog, To Do, In Progress, Testing and Done columns.
- Initial card placement was a planning arrangement, not evidence of completed work. Board statuses should reflect actual progress.

## Sprint 1 – Working text comparison

**Sprint goal:** Deliver a usable text-comparison flow that accepts two text samples, preprocesses them, calculates a similarity percentage and has automated tests.

**Selected user stories:** US01, US02, US03 and US10 (13 estimated story points).

### Work completed
- Added `modules/preprocessing.py` for lowercasing, punctuation replacement and whitespace normalisation.
- Added `modules/similarity.py` using scikit-learn TF-IDF vectorisation and cosine similarity.
- Added input validation for empty text and non-string values.
- Built the two-text Streamlit comparison form and similarity result display.
- Added automated tests for preprocessing and similarity behaviour.
- User confirmed that the Sprint 1 tests passed locally and that the Streamlit application launched and produced a sample comparison.

### Sprint 1 close-out
- User-reported local tests passed; exact terminal output was not archived in this log.
- Sample UI comparison was successful.

## Sprint 2 – Sentence-level matching

**Sprint goal:** Extend text comparison with sentence-level matching so users can inspect likely textual overlap.

**Selected user story:** US04 – Identify matching sentences (5 estimated story points).

### Work completed
- Added `modules/matching.py` to split text into sentences and compare sentence vectors using TF-IDF and cosine similarity.
- Set a default matching threshold of 50%.
- For each sentence in Text 1, the algorithm selects its closest sentence in Text 2 and returns the pair when it meets the threshold.
- Updated `app.py` to display matching sentence pairs and similarity percentages.
- Added `tests/test_matching.py` for sentence splitting, identical and unrelated sentences, custom thresholds, empty input and invalid values.
- Improved whitespace normalisation to handle line breaks commonly introduced by PDF text extraction and filtered fragments shorter than two words.

### Validation and close-out
- User manually tested sentence matching, including examples with line breaks.
- Sprint 2 implementation was committed and pushed to the GitHub main branch.
- US04 implementation and validation were completed.

## Sprint 3 – Document upload and collection comparison

**Sprint goal:** Allow users to upload common document formats, store documents locally and compare an uploaded document against the stored collection.

**Selected user stories:**
- US05 – Upload TXT/PDF/DOCX documents (5 estimated story points).
- US06 – Compare against stored documents (5 estimated story points).

### Work completed

#### Document extraction
- Added `modules/document_reader.py`.
- Implemented TXT extraction using UTF-8 decoding, PDF extraction using pypdf and DOCX extraction using python-docx.
- Added validation for unsupported formats, unreadable files and empty extracted text.
- PDF extraction combines text from all pages.

#### Local document collection
- Added `modules/document_store.py`.
- Implemented local storage under `data/documents/`.
- Added filename sanitisation and duplicate filename handling to avoid overwriting existing documents.
- Implemented retrieval of stored documents.
- Implemented comparison of uploaded text against readable stored documents.
- Sorted comparison results by similarity percentage in descending order.

#### Streamlit integration
- Updated `app.py` with separate Text Comparison and Document Comparison tabs.
- Added multi-file upload for adding documents to the local collection.
- Added document upload and comparison against the collection.
- Displayed ranked similarity results and the closest matching document.
- Integrated sentence-level matching with the closest stored document.

#### Testing and validation
- Added `tests/test_document_reader.py` and `tests/test_document_store.py`.
- Extended sentence-matching tests for whitespace and PDF line-break handling.
- Added a multi-page PDF extraction test.
- User confirmed that all **35 automated tests passed locally**.
- User manually tested TXT, PDF and DOCX uploads, local document storage and document comparison.
- Updated `.gitignore` so uploaded documents are not committed; retained `data/documents/.gitkeep` to preserve the directory in Git.

### Sprint 3 close-out
- Implementation committed as `be882a1`.
- Commit message: `Sprint 3: Add document upload and collection comparison`.
- Changes successfully pushed to the GitHub `main` branch.
- US05 and US06 implementation and validation completed.
- Sprint 3 is complete.

### Sprint 3 outcome
The application supports text-to-text comparison and document-to-local-collection comparison. Users can inspect overall similarity scores and sentence-level matches. The local document collection is intentionally not tracked by Git.

## Sprint 4 – History, dashboard and PDF reports

**Sprint goal:** Add persistence, summary information and reporting so users can review and retain previous comparison results.

**Selected user stories:**
- US07 – Save check history (3 estimated story points).
- US08 – Dashboard summary (3 estimated story points).
- US09 – Downloadable PDF report (3 estimated story points).

### US07 – Save check history (Complete)

#### Implementation
- Added `modules/history.py` with SQLite database initialisation and operations to save and retrieve comparison records.
- Stored comparison type, source and target labels/names, similarity score, matching sentence data and timestamp.
- Integrated history saving into text and document comparison flows in `app.py`.
- Added a Comparison History tab to display saved checks, their scores, timestamps, compared items and matching sentences.
- Kept the local SQLite database out of version control through the existing `.gitignore` rules.

#### Validation and evidence
- Added `tests/test_history.py` covering database creation, saving and retrieving records, newest-first ordering, match data, missing IDs and invalid inputs.
- User reported that all **7 history tests passed locally**.
- US07 was committed and pushed to `main` in commit `daf63b5` – `Sprint 4: Implement comparison history US07 integration`.

### US09 – Download comparison report (Complete)

#### Implementation
- Added `modules/report_generator.py` using ReportLab to generate PDF reports in memory.
- Reports include the comparison type, source and target names/labels, generation date, overall similarity score, matching sentence pairs and an important limitation note.
- Integrated a PDF download button into the text comparison flow.
- Integrated individual PDF download buttons for document-to-collection comparison results.
- Used PDF bytes directly for Streamlit downloads; generated reports do not need to be saved as permanent files.

#### Validation and evidence
- Added `tests/test_report_generator.py` covering PDF generation, comparison details, matching sentence content, the limitation note and invalid inputs.
- User reported that all **7 report-generator tests passed locally**.
- User manually confirmed that PDF downloads work in the application.
- US09 was committed and pushed to `main` in commit `c9f59da` – `Sprint 4: Add downloadable PDF comparison reports US09 integration`.

### Sprint 4 status
- US07 – Complete.
- US09 – Complete.
- US08 – Pending; dashboard summary has not yet been implemented.
- Sprint 4 remains in progress until US08 is implemented and validated.

## Activity entry template

Copy this section for each new real event.

### [Actual date] – [Event / sprint]
- Goal:
- Participants:
- Work completed:
- Decisions:
- Blockers:
- Evidence (issue, pull request, commit, test output):
- Next actions:

## Metrics

The initial product backlog estimate is 37 story points. Do not report this estimate as velocity. Record velocity, cycle time, burndown and completed points only when supported by actual sprint tracking.
