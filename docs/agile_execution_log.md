# Agile Execution Log

This log records the project's actual planning and development activities. Update it as work happens; do not record planned work as completed.

## Project baseline
- Project: PlagCheck – Smart Plagiarism Detection System
- Repository: https://github.com/Racchie22/PlagCheck
- Initial repository branch: main
- Current stage: Phase 0 – planning and setup
- Current working arrangement: Initial planning and implementation are being handled by the repository owner. Additional collaborators may be invited later.

## Phase 0 checklist
| Activity | Status | Evidence / notes |
|---|---|---|
| Create private GitHub repository | Completed | PlagCheck repository; main branch |
| Define problem statement and scope | Completed | docs/project_proposal.md |
| Prepare user stories and acceptance criteria | Completed | docs/user_stories.md |
| Prioritise product backlog and estimates | Completed | docs/product_backlog.md; initial estimate: 37 points |
| Define Definition of Done | Drafted | docs/user_stories.md |
| Create GitHub issues for user stories | Completed | Issues #1–#10 |
| Create GitHub Project board and add issues | Completed | PlagCheck Agile Project Board; board currently used as a planning view |
| Confirm additional team participation and any later role allocation | Deferred | Revisit only if additional collaborators join |
| Confirm Sprint 1 duration and capacity | Pending | Set before implementation based on remaining time |

## Activity log

### 18 November 2026 – Project initiation and planning setup
- Goal: Establish the repository and prepare the initial project plan.
- Participants: Repository owner.
- Work completed: Created the project proposal, README, requirements file, user stories, product backlog, execution log and initial application placeholder. Created GitHub issues #1–#10 from the user stories.
- Decisions: Use Python, Streamlit, scikit-learn, SQLite and Pytest as the planned technology stack. Begin with text-to-text comparison before adding document uploads and reporting. Handle initial planning and implementation individually; discuss additional collaborators later.
- Blockers: Sprint duration and capacity still need to be confirmed.
- Evidence: Initial baseline commit and GitHub issues #1–#10 in the PlagCheck repository.
- Next actions: Confirm Sprint 1 timebox, then implement and validate the complete Sprint 1 increment.

### [Actual date] – GitHub Project board created
- Goal: Set up a visual view for tracking the product backlog.
- Participants: Repository owner.
- Work completed: Created the PlagCheck board and added the ten user-story issues. Configured Backlog, To Do, In Progress, Testing and Done columns.
- Decisions: The initial card arrangement is a sample/planning arrangement, not a claim that those user stories have reached those development stages. Board statuses will be updated to match actual work.
- Evidence: PlagCheck GitHub Project board.
- Next actions: Update card statuses as real implementation and testing progress occurs.

## Sprint execution approach
A sprint is planned and delivered as one coherent increment. Related user stories can be worked on together and integrated before the sprint outcome is demonstrated. Internal tasks may be completed in parallel or in sequence as practical, but individual user stories do not need to be released one at a time.

### Sprint 1 – Working text comparison
- Planned scope: US01, US02, US03 and US10.
- Sprint goal: Deliver one usable, tested flow that accepts two text samples, preprocesses them, calculates a similarity percentage and validates core behaviour through automated tests.
- Status: Not started.
- Actual start/end dates: To be recorded when known.
- Review outcome and evidence: To be recorded after implementation and demonstration.

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
