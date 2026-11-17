# Agile Execution Log

This log records the project's actual planning and development activities. Update it as work happens; do not record planned work as completed.

## Project baseline
- Project: PlagCheck – Smart Plagiarism Detection System
- Repository: https://github.com/Racchie22/PlagCheck
- Initial repository branch: main
- Current stage: Sprint 1 – implementation and validation
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

### [Actual date] – GitHub Project board created
- Goal: Set up a visual view for tracking the product backlog.
- Participants: Repository owner.
- Work completed: Created the PlagCheck board and added the ten user-story issues. Configured Backlog, To Do, In Progress, Testing and Done columns.
- Decisions: The initial card arrangement is a sample/planning arrangement, not a claim that user stories have reached those development stages. Board statuses will be updated to match actual work.
- Evidence: PlagCheck GitHub Project board.

## Sprint 1 – Working text comparison

**Sprint goal:** Deliver one usable text-comparison flow that accepts two text samples, preprocesses them, calculates a similarity percentage and has automated tests for core behaviour.

**Selected user stories:** US01, US02, US03 and US10 (13 estimated story points).

### Work completed so far
- Added `modules/preprocessing.py` with lowercase conversion, punctuation replacement and whitespace normalisation.
- Added `modules/similarity.py` using scikit-learn TF-IDF vectorisation and cosine similarity.
- Added input validation for empty text and non-string values.
- Replaced the initial placeholder screen in `app.py` with a two-text Streamlit comparison form and similarity result display.
- Added automated test files for preprocessing and similarity behaviour.

### Validation progress
- The 12 core test cases were run against an isolated local copy of the Sprint 1 preprocessing and similarity implementation: **12 passed**.
- The tests still need to be run from the actual repository checkout using its installed dependencies.
- Streamlit launch and manual UI checks: Pending.
- Sprint review / final acceptance: Pending.

### Remaining Sprint 1 actions
1. In the project virtual environment, install dependencies from `requirements.txt`.
2. Run `python -m pytest -q` from the repository root and resolve any failures.
3. Run `streamlit run app.py` and manually check valid and invalid inputs.
4. Confirm the acceptance criteria for US01, US02, US03 and US10.
5. Record actual test output and update issue/board statuses based on evidence.

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
