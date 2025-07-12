# -*- coding: utf-8 -*-
"""Project Setup Wizard

Creates a new project folder with standard structure and tickets.
"""

from pathlib import Path


def prompt(text: str, default: str = "") -> str:
    response = input(f"{text} [{default}]: ").strip()
    return response or default


def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def _create_structure(project_dir: Path):
    for sub in ["src", "scripts", "docs", "config", ".github/workflows"]:
        (project_dir / sub).mkdir(parents=True, exist_ok=True)


def _package_json(name: str) -> str:
    return (
        '{\n'
        f'  "name": "{name}",\n'
        '  "version": "1.0.0"\n'
        '}\n'
    )


def main():
    project_dir = Path(prompt("Project directory", "new_project"))
    design_path = Path(prompt("Path to design document", "design.md"))
    template = prompt(
        "Project template (python/node/godot/arduino)", "python"
    ).lower()
    project_dir.mkdir(parents=True, exist_ok=True)

    _create_structure(project_dir)

    create_file(project_dir / "README.md", f"# {project_dir.name}\n")
    create_file(project_dir / "agents.md", _default_agents())
    create_file(project_dir / "tickets.md", _default_tickets(design_path))

    if template == "python":
        create_file(project_dir / "requirements.txt")
        create_file(project_dir / "scripts" / "setup.bat", _setup_bat())
        create_file(
            project_dir / ".github" / "workflows" / "python.yml",
            _workflow_yaml("python"),
        )
    elif template == "node":
        create_file(project_dir / "package.json", _package_json(project_dir.name))
        create_file(project_dir / "src" / "index.js", "// entry point\n")
        create_file(
            project_dir / ".github" / "workflows" / "node.yml",
            _workflow_yaml("node"),
        )
    elif template == "godot":
        create_file(project_dir / "project.godot")
        create_file(
            project_dir / ".github" / "workflows" / "godot.yml",
            _workflow_yaml("godot"),
        )
    elif template == "arduino":
        create_file(project_dir / "src" / "sketch.ino", "// Arduino sketch\n")
        create_file(
            project_dir / ".github" / "workflows" / "arduino.yml",
            _workflow_yaml("arduino"),
        )
    else:
        print(f"Unknown template '{template}', using generic setup.")

    print(
        f"Project initialized at {project_dir.resolve()} using {template} template"
    )


def _default_agents() -> str:
    return (
        "# Agent Instructions\n\n"
        "Use `tickets.md` for task tracking in an agile manner. "
        "Each ticket can be turned into a pull request. Reviewers may reopen tickets if needed."
    )


def _default_tickets(design_path: Path) -> str:
    return (
        "# Tickets\n\n"
        "## Ticket 1 - Project Setup\n"
        "- Read the design document and create `scripts/setup.bat` that:\n"
        "  - creates a virtual environment\n"
        "  - sets up folders (src, scripts, docs, config)\n"
        "  - installs dependencies from `requirements.txt`\n"
        "\n"
        "## Ticket 2 - Update Agents Instructions\n"
        "- Review the design document and expand `agents.md` with detailed "
        "project guidelines and iterative workflow instructions."
    )


def _setup_bat() -> str:
    return (
        "@echo off\n"
        "python -m venv venv\n"
        "call venv\\Scripts\\activate\n"
        "pip install -r requirements.txt\n"
    )


def _workflow_yaml(template: str) -> str:
    if template == "python":
        return (
            "name: Python package\n\n"
            "on: [push]\n\n"
            "jobs:\n"
            "  build:\n"
            "    runs-on: ubuntu-latest\n"
            "    steps:\n"
            "      - uses: actions/checkout@v3\n"
            "      - uses: actions/setup-python@v4\n"
            "        with:\n"
            "          python-version: '3.x'\n"
            "      - run: pip install -r requirements.txt\n"
            "      - run: echo Build completed\n"
        )
    if template == "node":
        return (
            "name: Node.js CI\n\n"
            "on: [push]\n\n"
            "jobs:\n"
            "  build:\n"
            "    runs-on: ubuntu-latest\n"
            "    steps:\n"
            "      - uses: actions/checkout@v3\n"
            "      - uses: actions/setup-node@v3\n"
            "        with:\n"
            "          node-version: '16'\n"
            "      - run: npm install\n"
            "      - run: npm test --if-present\n"
        )
    return (
        "name: CI\n\n"
        "on: [push]\n\n"
        "jobs:\n"
        "  build:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - uses: actions/checkout@v3\n"
        "      - run: echo Build placeholder\n"
    )


if __name__ == "__main__":
    main()
