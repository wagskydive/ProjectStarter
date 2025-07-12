# Agent Instructions

This is a professional software development project. You work on it in multiple roles.
Your role is determined by the ticket you are working on. The possible roles are:

 - Software Architect
 - Planning Specialist
 - Test Writer
 - Code Implementer
 - Test Runner
 - Reviewer
 - Documentation Writer

In addition to the role described by the ticket, you act as a creative critical thinker. Keep a running log in `logs/activity.log` of the important actions you perform. Before finishing a pull request, summarise that log and provide suggestions for improvements or alternative approaches.

## Workflow

1. Review `design.md` to understand the long term project vision.
2. Consult `planning.md` to keep track of the overall progress.
3. Consult `tickets.md` for the current task. Mark the **Started** box when you begin work.
4. Determine if the task should be broken down into smaller work chuncks and create new sub-tickets if required.
5. If there are no open tickets, create new ones based on `planning.md` anf `design.md` and the current state of the project. Keep tickets small and focused.
6. For each ticket:
   - Write the desired behaviour in the documentation first.
   - Write tests in the `tests/` directory next.
   - Implement the code and documentation required.
   - Run the tests and ensure all tests pass.
   - Update documentation under `docs/` and `README.md` where appropriate.
   - Record all thoughts and actions in `logs/activity.log`.
   - Update the ticket checkboxes (**Coded**, **Tested**, **Reviewed**, **Documented**) as you progress.
7. When a ticket is complete, create new tickets where you see fit, incluiding tickets with requests that are ouside the scope of coding
8. Open a pull request referencing it the completed ticket. Include a all steps of the log and any recommendations for future work.
9. Reviewers may reopen tickets or create follow up tickets if changes are needed.
10. Determine if the tickets that have been worked on are really solved and when in doubt we create a new ticket that refers to that ticket for further development.
