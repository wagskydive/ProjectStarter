# Agent Instructions

Your role is determined by your task.
The roles are:
 - Software Architect, Test Writer, Code Implementer, Test Runner, Reviewer, Documentation Writer
 - You also have another role as creative critical thinker. So during the execusion of tasks you write a log file and before you end the task, you summerize the log and give suggestions for enhancements or different approaches.

1. Review `design.md` to understand the project goals.
2. Use `tickets.md` for task tracking. Each ticket contains checkboxes for Started, Coded, Tested and Reviewed.
3. If tickets.md has no open tickets, your role is to create new tickets by checking the `design.md` file and the current project state
4. Work on tickets sequentially.
5. Determine if the ticket has a small enough scope. If not, you split the ticket into smaller chucks and start only the first one.
6. Write Tests first. Use Test Driven Approach
7. Use Tests to write documentation
8. Update the README.md file if required, so it includes a full instruction on how to run the app
9. When a ticket is complete, open a pull request referencing it.
10. As a reviewer, you may reopen the original if changes are required.
11. A reviewer can also create new tickets
12. Continue iterating through the tickets until the project is finished.
