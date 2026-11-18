# Product Backlog

The backlog is prioritised and will be refined as the project progresses. Story points are relative estimates, not hours.

| Order | ID | Backlog item | Priority | Points | Planned increment | Status |
|---:|---|---|---|---:|---|---|
| 1 | US01 | Text input comparison | Must | 2 | Sprint 1 | Complete |
| 2 | US02 | Text preprocessing | Must | 3 | Sprint 1 | Complete |
| 3 | US03 | TF-IDF similarity percentage | Must | 3 | Sprint 1 | Complete |
| 4 | US10 | Automated tests for core algorithm | Must | 5 | Sprint 1 | Complete |
| 5 | US04 | Sentence-level matching indicators | Should | 5 | Sprint 2 | Complete |
| 6 | US05 | TXT/PDF/DOCX upload and extraction | Should | 5 | Sprint 3 | Complete |
| 7 | US06 | Compare against locally stored documents | Should | 5 | Sprint 3 | Complete |
| 8 | US07 | SQLite check history | Could | 3 | Sprint 4 | Planned |
| 9 | US08 | Dashboard summary | Could | 3 | Sprint 4 | Planned |
| 10 | US09 | Downloadable PDF report | Could | 3 | Sprint 4 | Planned |

**Initial estimated backlog total:** 37 story points. This is a planning estimate, not completed velocity.

## Sprint outline

### Sprint 1 – Working text comparison
**Goal:** Deliver a usable, tested text-comparison flow from input to similarity result.

US01, US02, US03 and US10 formed one integrated increment. The outcome was a Streamlit text comparison flow with preprocessing, a TF-IDF/cosine similarity percentage and automated tests.

**Status:** Complete.

### Sprint 2 – Sentence-level matching
**Goal:** Extend comparison results with sentence-level matching indicators.

US04 delivered sentence splitting, TF-IDF/cosine similarity between sentences and display of matching pairs using a default 50% threshold.

**Status:** Complete.

### Sprint 3 – Document workflow
**Goal:** Support document extraction and comparison against a local document collection.

US05 and US06 delivered TXT/PDF/DOCX extraction, local document storage, ranked collection comparison and sentence matching against the closest stored document.

**Status:** Complete. User-reported local validation: 35 automated tests passed.

### Sprint 4 – Persistence and reporting
**Goal:** Make comparison results easier to review and retain.

- US07 – Save check history using SQLite.
- US08 – Display dashboard summaries.
- US09 – Generate downloadable PDF reports.

**Status:** Planned; not yet implemented.

### Sprint 5 – Stabilisation
Potential work includes broader regression testing, refactoring, continuous integration and final documentation. Scope will be refined after Sprint 4.

## Planning notes
- Related stories are implemented and validated as coherent sprint increments rather than being released as isolated mini-features.
- Sprint dates and capacity should reflect the actual academic schedule.
- Story points are estimates and are not a measure of hours.
- Do not report planned work as completed work.
