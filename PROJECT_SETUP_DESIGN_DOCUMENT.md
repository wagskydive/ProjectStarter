
# Mini Project Design Document: Project Setup Wizard

## Project Name
**Project Setup Wizard**

## Objective
To create a simple and modular executable tool that initializes a new software development project with standardized files and folder structure, including a task management system (`tickets.md`) and agent instructions (`agents.md`), to get the project ready for vibe coding.

## Goals
- Automate the setup of new coding projects
- Standardize initial project structure
- Include automation via batch files or scripts
- Enable integration with OpenAI Codex and GitHub repositories

## Features
- Wizard-like executable for user inputs (path to project parent folder, design.md)
- Creation of:
  - An `agents.md` file with instructions for the ai agent to use the `tickets.md` and an Agile approach with an explaination of the ticket system.
  - Creation of `tickets.md`.
- The first ticket in `tickets.md`:
  - Setup instructions for the agent, including:
    - Read the design.md and create a batch file that does setup of the project:
    - Virtual environment 
    - Predefined folder structure (src, scripts, docs, config)
    - `requirements.txt` file for dependencies
    - install the dependencies
- The second ticket in `tickets.md`:
  - Read the design file and modify the `agents.md` file so it includes everything to work on the project.
  - Add instrictions for aniterative approach in the `agents.md`.  When a ticket is send as a pull request, a review ticket is created and a reviewer can reopen the ticket.
- Option to connect with a GitHub repository

## Project Structure
```
project_name/
│
├── src/
├── scripts/
│   └── setup.bat
├── docs/
├── config/
├── .github/
│   └── workflows/
│       └── python-app.yml
├── agents.md
├── tickets.md
├── README.md
├── requirements.txt
```

## Development Phases
### Phase 1: MVP
- Collect user input through a simple form
- Generate batch file for setup
- Create `agents.md` and `tickets.md`

### Phase 2: Enhancement
- Add GUI for wizard
- Include template selection (Python, Node.js, Godot, Arduino)
- Advanced options for configuring CI/CD, linter, and formatter

## Tools and Technologies
- Python (for logic)
- Batch scripting (for automation on Windows)
- Markdown (for documentation)
- GitHub (for version control)
- Open Interpreter (for code generation and automation)

## Agile Sprints
### Sprint 1:
- Set up repo and folder structure
- Write basic batch script
- Create basic `README.md`, `tickets.md`, and `agents.md`

### Sprint 2:
- Expand script for full automation
- Test setup on clean environment

### Sprint 3:
- Add flexibility and error handling
- Add support for template selection

## License
MIT License

## Authors
Willem de Groot

## Future Considerations
- Add support for Linux and macOS
- Docker support
- Web-based setup interface
