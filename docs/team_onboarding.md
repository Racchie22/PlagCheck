# Team Onboarding – PlagCheck

## Before development starts
The repository owner should invite the other team members as collaborators:
- Rohit
- Harsh
- Jayant

Each person should accept the invitation using their own GitHub account and confirm that they can open the private repository.

## What every member should do
1. Read README.md, docs/project_proposal.md, docs/user_stories.md and docs/product_backlog.md.
2. Confirm or discuss the proposed responsibilities in docs/team_roles.md.
3. Open the GitHub Project board and review the issues.
4. Set up Python and the project locally by following the README.
5. Agree on a sprint goal, duration and realistic capacity with the whole team.
6. Work on an assigned issue and communicate blockers early.
7. Commit their own changes using their own GitHub account.
8. Request review from another team member before merging where practical.
9. Update the issue and board when work moves through To Do, In Progress, Testing and Done.
10. Be prepared to explain the module they worked on and how it integrates with the application.

## Suggested initial ownership
- Rachit: coordination, integration and project documentation.
- Rohit: text preprocessing, TF-IDF/cosine similarity and algorithm tests.
- Harsh: Streamlit interface, input validation and document upload.
- Jayant: SQLite persistence, report generation and quality/testing support.

These are proposed responsibilities. Confirm them together before assigning issues.

## Local setup
1. Install Python 3.11 or newer.
2. Clone the repository.
3. Create and activate a virtual environment.
4. Install dependencies with `pip install -r requirements.txt`.
5. Run the starter application with `streamlit run app.py`.

The starter app is only a project placeholder at this stage. Core plagiarism comparison will be implemented in Sprint 1.

## Git working rules
- Use a separate feature branch for a substantial task where practical.
- Keep commits small and describe the real change.
- Do not commit passwords, API keys, private student documents or local database files.
- Do not mark an issue Done until its acceptance criteria are met and the result has been tested.
