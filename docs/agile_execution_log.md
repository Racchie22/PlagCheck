# Agile Execution Log

This log records the project's actual planning and development activities. Update it as work happens; do not record planned work as completed.

## Project baseline
- Project: PlagCheck – Smart Plagiarism Detection System
- Repository: https://github.com/Racchie22/PlagCheck
- Initial repository branch: main
- Current stage: Sprint 2 – implementation and validation
- Current working arrangement: Initial planning and implementation are being handled by the repository owner. Additional collaborators may be invited later.

## Phase 0 – Planning and setup
| Activity | Status | Evidence / notes |
|---|---|---|
| Create private GitHub repository | Completed | PlagCheck repository; main branch |
| Define problem statement and scope | Completed | docs/project_proposal.md |
| Prepare user stories and acceptance criteria | Completed | docs/user_stories.md |
| Prioritise product backlog and estimates | Completed | docs/product_backlog.md; initial estimate: 37 points |
| Define Definition of Done | Drafted | docs/user_stories.md |
| Create GitHub issues for user stories | Completed | Issues #1–#10 |
| Create GitHub Project board and add issues | Completed | PlagCheck Agile Project Board; initial card arrangement was a planning example |
| Confirm additional team participation and any later role allocation | Deferred | Revisit only if additional collaborators join |

## Phase 0 activity log

### 18 November 2026 – Project initiation and planning setup
- Goal: Establish the repository and prepare the initial project plan.
- Participants: Repository owner.
- Work completed: Created the project proposal, README, requirements file, user stories, product backlog, execution log and initial application placeholder. Created GitHub issues #1–#10 from the user stories.
- Decisions: Use Python, Streamlit, scikit-learn, SQLite and Pytest as the planned technology stack. Begin with text-to-text comparison before adding document uploads and reporting. Handle initial planning and implementation individually; discuss additional collaborators later.
- Evidence: Initial baseline commit and GitHub issues #1–#10 in the PlagCheck repository.

### GitHub Project board setup
- Goal: Set up a visual view for tracking the product backlog.
- Participants: Repository owner.
- Work completed: Created the PlagCheck board and added the ten user-story issues. Configured Backlog, To Do, In Progress, Testing and Done columns.
- Decisions: The initial card arrangement is a sample/planning arrangement, not a claim that user stories have reached those development stages. Board statuses will be updated to match actual work.
- Evidence: PlagCheck GitHub Project board.

## Sprint 1 – Working text comparison

**Sprint goal:** Deliver one usable text-comparison flow that accepts two text samples, preprocesses them, calculates a similarity percentage and has automated tests for core behaviour.

**Selected user stories:** US01, US02, US03 and US10 (13 estimated story points).

### Work completed
- Added `modules/preprocessing.py` with lowercase conversion, punctuation replacement and whitespace normalisation.
- Added `modules/similarity.py` using scikit-learn TF-IDF vectorisation and cosine similarity.
- Added input validation for empty text and non-string values.
- Built the two-text Streamlit comparison form and similarity result display.
- Added automated test files for preprocessing and similarity behaviour.
- User confirmed that the Sprint 1 tests ran successfully in their local project environment.
- User launched the Streamlit application locally and successfully completed a sample text comparison.

### Sprint 1 close-out
- User-reported automated test result: passed. Exact terminal output has not been added to this log.
- Sample UI comparison: successful.
- Sprint 1 implementation was retained in a separate local backup folder by the repository owner.
- Formal review/retrospective notes and screenshots can be added if required for the course submission.

## Sprint 2 – Sentence-level matching

**Sprint goal:** Extend the text comparison result so users can inspect likely sentence-level overlap between the two text samples.

**Selected user story:** US04 – Identify matching sentences (5 estimated story points).

### Initial implementation
- Added `modules/matching.py` to split text using common sentence punctuation and compare sentence vectors using TF-IDF and cosine similarity.
- Added a documented 50% similarity threshold. For each sentence in Text 1, the function selects its closest sentence in Text 2 and reports the pair only when it reaches the threshold.
- Updated `app.py` to display matching sentence pairs and their similarity percentages, or a message when no pairs meet the threshold.
- Added `tests/test_matching.py` for sentence splitting, exact matches, likely matches, unrelated sentences, custom threshold, empty input and invalid values.

### Validation status
- Implementation has been committed to the GitHub main branch.
- Local execution of the new Sprint 2 tests and UI checks: Pending.
- Sprint review and acceptance of US04: Pending.

### Remaining Sprint 2 actions
1. Pull the latest main branch into the local working copy.
2. Run `python -m pytest -v` and resolve any failures.
3. Run the Streamlit app and test exact matches, partial matches, unrelated sentences and empty input.
4. Review whether the 50% threshold gives sensible results for representative text.
5. Record actual test output and screenshots before marking US04 Done.

## Activity entry template
Copy this section for each real event.

### [Actual date] – [Event / sprint]
- Goal:
- Participants:
- Work completed:
- Decisions:
- Blockers:
- Evidence (issue, pull request, commit, test output):
- Next actions:

## Metrics
Record velocity, cycle time, burndown and completed story points only after actual sprint work has occurred. Initial story-point estimates are not velocity.
