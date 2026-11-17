# User Stories and Acceptance Criteria

Story points are initial relative estimates, not hours. Estimates may change after backlog refinement.

| ID | User story | Priority | Estimate |
|---|---|---:|---:|
| US01 | As a user, I want to enter two text samples so that I can compare them. | Must | 2 |
| US02 | As a user, I want text to be cleaned consistently so that comparison is less affected by formatting. | Must | 3 |
| US03 | As a user, I want to see a similarity percentage so that I can understand the degree of textual overlap. | Must | 3 |
| US04 | As a user, I want similar sentences or passages to be identified so that I can inspect the overlap. | Should | 5 |
| US05 | As a user, I want to upload TXT, PDF or DOCX files so that I can compare real documents. | Should | 5 |
| US06 | As a user, I want to compare an uploaded document with documents stored in the app so that I can check against a local collection. | Should | 5 |
| US07 | As a user, I want previous checks to be saved so that I can review them later. | Could | 3 |
| US08 | As a user, I want a dashboard summary so that I can view basic usage and result information. | Could | 3 |
| US09 | As a user, I want to download a report so that I can keep a record of a comparison. | Could | 3 |
| US10 | As a developer, I want automated tests for core behaviour so that changes can be checked reliably. | Must | 5 |

## Acceptance criteria

### US01 – Compare two text samples
- Two separate text inputs are available.
- User can submit both texts for comparison.
- Empty input is rejected with a clear message.
- A result is displayed without crashing the app.

### US02 – Preprocess text
- Processing handles upper/lower case consistently.
- Extra whitespace and basic punctuation are handled consistently.
- Original input is not silently overwritten in the UI.

### US03 – Similarity percentage
- A numeric similarity result is displayed as a percentage.
- Identical non-empty texts produce a higher score than unrelated texts.
- The UI explains that the score indicates textual similarity, not proof of plagiarism.

### US04 – Identify matching sentences
- Text is split into sentences for comparison.
- Likely matching sentences are identified using a documented threshold or rule.
- The result makes clear which text each match came from.

### US05 – Upload documents
- TXT, text-based PDF and DOCX files are accepted.
- Unsupported file types and unreadable/empty documents produce clear errors.
- The extracted text can be passed to the comparison feature.

### US06 – Compare with stored documents
- A document can be compared with the local collection.
- Results identify the stored document that produced each comparison.
- An empty collection is handled gracefully.

### US07 – Check history
- A completed check can be stored locally.
- The history view shows useful metadata such as date and score.
- Database errors do not expose stack traces to the user.

### US08 – Dashboard
- The dashboard displays available summary metrics from stored checks.
- Empty history is handled gracefully.

### US09 – Download report
- A report can be generated for a completed comparison.
- The report includes the compared document names or labels, score and limitation note.
- The download works for a normal completed check.

### US10 – Automated tests
- Core preprocessing and similarity functions have automated tests.
- Tests include identical, different and invalid/empty inputs.
- The test command and outcome are recorded accurately.

## Definition of Done
A story is Done only when its acceptance criteria are met, relevant tests pass, the change has been reviewed by a teammate where possible, the code is committed, and related documentation is updated. If a review or test is not applicable, the reason is recorded rather than assumed.
