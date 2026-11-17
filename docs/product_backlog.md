# Product Backlog

The backlog is prioritised and will be refined as the project progresses. Initial story points are relative estimates.

| Order | ID | Backlog item | Priority | Points | Planned increment |
|---:|---|---|---|---:|---|
| 1 | US01 | Text input comparison | Must | 2 | Sprint 1 |
| 2 | US02 | Text preprocessing | Must | 3 | Sprint 1 |
| 3 | US03 | TF-IDF similarity percentage | Must | 3 | Sprint 1 |
| 4 | US10 | Automated tests for core algorithm | Must | 5 | Sprint 1 |
| 5 | US04 | Sentence-level matching indicators | Should | 5 | Sprint 2 |
| 6 | US05 | TXT/PDF/DOCX upload and extraction | Should | 5 | Sprint 3 |
| 7 | US06 | Compare against locally stored documents | Should | 5 | Sprint 3 |
| 8 | US07 | SQLite check history | Could | 3 | Sprint 3/4 |
| 9 | US08 | Dashboard summary | Could | 3 | Sprint 4 |
| 10 | US09 | Downloadable PDF report | Could | 3 | Sprint 4 |

**Initial estimated backlog total:** 37 story points. This is a planning estimate, not completed velocity.

## Sprint outline (provisional)

### Sprint 1 – Working text comparison
**Sprint goal:** Deliver one usable, tested text-comparison flow from input to similarity result.

Sprint 1 includes US01, US02, US03 and US10 as one integrated increment. These are related parts of the same feature, not four separate mini-releases. Implementation can be divided into internal coding tasks, but the sprint outcome will be demonstrated and validated as a complete flow.

Expected Sprint 1 outcome:
- User can enter two text samples in the application.
- Inputs are validated and preprocessed consistently.
- TF-IDF and cosine similarity produce a displayed percentage.
- The interface explains that similarity is not proof of plagiarism.
- Automated tests cover preprocessing, identical text, different text and invalid/empty input.

### Later increments
- Sprint 2 – Explainable results: sentence-level matching and validation (US04).
- Sprint 3 – Document workflow: file extraction and comparison against a local document collection (US05 and US06).
- Sprint 4 – Persistence and usability: check history, dashboard and downloadable report (US07, US08 and US09).
- Sprint 5 – Stabilisation: broader tests, refactoring, CI and final documentation.

The outline is provisional. Sprint duration and actual dates will be set based on the remaining time and available capacity. Do not report planned work as completed work. Story points are estimates and are not a measure of hours.
