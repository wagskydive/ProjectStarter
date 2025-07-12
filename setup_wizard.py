# -*- coding: utf-8 -*-
"""Project Setup Wizard

Creates a new project folder with standard structure and tickets.
"""

from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

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


def _empty_design(name: str) -> str:
    return f"# {name} Design Document\n\n"


def _default_agents() -> str:
    return (
        "# Agent Instructions\n\n"
        "Your role is determined by your task.\n"
        
        "1. Review `design.md` to understand the project goals.\n"
        "2. Use `tickets.md` for task tracking. Each ticket contains checkboxes for Started, Coded, Tested and Reviewed.\n"
        "3. If tickets.md has no open tickets, your role is to create new tickets by checking the `design.md` file and the current project state"
        "4. Work on tickets sequentially.\n" 
        "5. Determine if the ticket has a small enough scope and if not you split the ticket op in smaller chucks and start only the first one.\n"
        "6. Write Tests first. Use Test Driven Approach\n"
        "7. Use Tests to write documentation\n"
        "8. When a ticket is complete, open a pull request referencing it.\n"
        "9. As a reviewer, you may reopen the original if changes are required.\n"
        "10. A reviewer can also create new tickets\n"
        "11. Continue iterating through the tickets until the project is finished."
    )


def _default_tickets(design_provided: bool, name: str = "", description: str = "") -> str:
    if design_provided:
        return (
            "# Tickets\n\n"
            "## Ticket 1 - Project Setup\n"
            "- [ ] Started\n"
            "- [ ] Coded\n"
            "- [ ] Tested\n"
            "- [ ] Reviewed\n"
            "- [ ] Documented\n"
            "- Read the design document and create `scripts/setup.bat` that:\n"
            "  - creates a virtual environment\n"
            "  - sets up folders (src, scripts, docs, config)\n"
            "  - installs dependencies from `requirements.txt`\n"
            "\n"
            "## Ticket 2 - Update Agents Instructions\n"
            "- [ ] Started\n"
            "- [ ] Coded\n"
            "- [ ] Tested\n"
            "- [ ] Reviewed\n"
            "- [ ] Documented\n"
            "- Review the design document and expand `agents.md` with detailed project guidelines and iterative workflow instructions."
        )

    return (
        "# Tickets\n\n"
        "## Ticket 1 - Create Design Document\n"
        "- [ ] Started\n"
        "- [ ] Coded\n"
        "- [ ] Tested\n"
        "- [ ] Reviewed\n"
        "- [ ] Documented\n"
        "- Use the following information to write `design.md`:\n"
        f"  - Name: {name}\n"
        f"  - Description: {description}\n"
        "\n"
        "## Ticket 2 - Project Setup\n"
        "- [ ] Started\n"
        "- [ ] Coded\n"
        "- [ ] Tested\n"
        "- [ ] Reviewed\n"
        "- [ ] Documented\n"
        "- After the design document is ready, create `scripts/setup.bat` that:\n"
        "  - creates a virtual environment\n"
        "  - sets up folders (src, scripts, docs, config)\n"
        "  - installs dependencies from `requirements.txt`\n"
        "\n"
        "## Ticket 3 - Update Agents Instructions\n"
        "- [ ] Started\n"
        "- [ ] Coded\n"
        "- [ ] Tested\n"
        "- [ ] Reviewed\n"
        "- [ ] Documented\n"
        "- Review the design document and expand `agents.md` with detailed project guidelines and iterative workflow instructions."
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


# ---------------------------------------------------------------------------
# GUI implementation
# ---------------------------------------------------------------------------

class SetupWizardGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Project Setup Wizard")

        tk.Label(self.root, text="Project Directory").grid(row=0, column=0, sticky="w")
        self.project_dir_var = tk.StringVar(value="new_project")
        tk.Entry(self.root, textvariable=self.project_dir_var, width=40).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self._browse_project).grid(row=0, column=2)

        self.design_mode = tk.StringVar(value="file")
        tk.Radiobutton(self.root, text="Use design.md", variable=self.design_mode, value="file", command=self._toggle_mode).grid(row=1, column=0, sticky="w")
        tk.Radiobutton(self.root, text="Provide name & description", variable=self.design_mode, value="desc", command=self._toggle_mode).grid(row=1, column=1, sticky="w")

        tk.Label(self.root, text="Design.md Path").grid(row=2, column=0, sticky="w")
        self.design_path_var = tk.StringVar(value="design.md")
        self.design_entry = tk.Entry(self.root, textvariable=self.design_path_var, width=40)
        self.design_entry.grid(row=2, column=1, padx=5, pady=5)
        tk.Button(self.root, text="Browse", command=self._browse_design).grid(row=2, column=2)

        tk.Label(self.root, text="Project Name").grid(row=3, column=0, sticky="w")
        self.name_var = tk.StringVar()
        self.name_entry = tk.Entry(self.root, textvariable=self.name_var, width=40)
        self.name_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Description").grid(row=4, column=0, sticky="nw")
        self.desc_text = tk.Text(self.root, width=30, height=5)
        self.desc_text.grid(row=4, column=1, padx=5, pady=5)

        tk.Label(self.root, text="Template").grid(row=5, column=0, sticky="w")
        self.template_var = tk.StringVar(value="python")
        ttk.Combobox(self.root, textvariable=self.template_var, values=["python", "node", "godot", "arduino"]).grid(row=5, column=1, padx=5, pady=5)

        tk.Button(self.root, text="Create Project", command=self._submit).grid(row=6, column=0, columnspan=3, pady=10)

        self._toggle_mode()

    def _browse_project(self):
        path = filedialog.askdirectory()
        if path:
            self.project_dir_var.set(path)

    def _browse_design(self):
        path = filedialog.askopenfilename(filetypes=[("Markdown", "*.md"), ("All files", "*.*")])
        if path:
            self.design_path_var.set(path)

    def _toggle_mode(self):
        mode = self.design_mode.get()
        if mode == "file":
            self.design_entry.configure(state=tk.NORMAL)
            self.name_entry.configure(state=tk.DISABLED)
            self.desc_text.configure(state=tk.DISABLED)
        else:
            self.design_entry.configure(state=tk.DISABLED)
            self.name_entry.configure(state=tk.NORMAL)
            self.desc_text.configure(state=tk.NORMAL)

    def _submit(self):
        project_dir = Path(self.project_dir_var.get()).expanduser()
        template = self.template_var.get().lower()
        if self.design_mode.get() == "file":
            design_path = Path(self.design_path_var.get()).expanduser()
            self._create(project_dir, template, design_path=design_path, design_provided=True)
        else:
            name = self.name_var.get().strip() or project_dir.name
            description = self.desc_text.get("1.0", tk.END).strip()
            self._create(project_dir, template, name=name, description=description, design_provided=False)
        messagebox.showinfo("Success", f"Project initialized at {project_dir.resolve()}")
        self.root.quit()

    def _create(self, project_dir: Path, template: str, design_path: Path = None, name: str = "", description: str = "", design_provided: bool = True):
        project_dir.mkdir(parents=True, exist_ok=True)
        _create_structure(project_dir)

        if design_provided:
            if design_path is None:
                design_path = project_dir / "design.md"
            # Always rename the copied design document to "design.md" inside the
            # new project regardless of the original file name.
            create_file(
                project_dir / "design.md",
                Path(design_path).read_text() if design_path.exists() else "",
            )
        else:
            create_file(project_dir / "design.md", _empty_design(name))

        create_file(project_dir / "README.md", f"# {project_dir.name}\n")
        create_file(project_dir / "agents.md", _default_agents())
        create_file(project_dir / "tickets.md", _default_tickets(design_provided, name, description))

        if template == "python":
            create_file(project_dir / "requirements.txt")
            create_file(project_dir / "scripts" / "setup.bat", _setup_bat())
            create_file(project_dir / ".github" / "workflows" / "python.yml", _workflow_yaml("python"))
        elif template == "node":
            create_file(project_dir / "package.json", _package_json(project_dir.name))
            create_file(project_dir / "src" / "index.js", "// entry point\n")
            create_file(project_dir / ".github" / "workflows" / "node.yml", _workflow_yaml("node"))
        elif template == "godot":
            create_file(project_dir / "project.godot")
            create_file(project_dir / ".github" / "workflows" / "godot.yml", _workflow_yaml("godot"))
        elif template == "arduino":
            create_file(project_dir / "src" / "sketch.ino", "// Arduino sketch\n")
            create_file(project_dir / ".github" / "workflows" / "arduino.yml", _workflow_yaml("arduino"))
        else:
            print(f"Unknown template '{template}', using generic setup.")


def main():
    gui = SetupWizardGUI()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
