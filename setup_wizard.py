# -*- coding: utf-8 -*-
"""Project Setup Wizard

Creates a new project folder containing only ``design.md``, ``AGENTS.md`` and ``tickets.md``.
"""

from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def create_file(path: Path, content: str = ""):
    """Write ``content`` to ``path`` without creating new directories."""
    if not path.parent.exists():
        raise FileNotFoundError(f"Directory {path.parent} does not exist.")
    path.write_text(content, encoding="utf-8")


def _empty_design(name: str) -> str:
    return f"# {name} Design Document\n\n"


def _default_agents() -> str:
    """Return the default agent instructions from the template file."""
    template_path = Path(__file__).with_name("default_agent_text.md")
    return template_path.read_text(encoding="utf-8")


def _default_tickets(design_provided: bool, name: str = "", description: str = "") -> str:
    """Return the default tickets text from the appropriate template."""
    if design_provided:
        path = Path(__file__).with_name("default_tickets_with_design.md")
        return path.read_text(encoding="utf-8")

    path = Path(__file__).with_name("default_tickets_no_design.md")
    template = path.read_text(encoding="utf-8")
    return template.format(name=name, description=description)


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

        tk.Button(self.root, text="Create Project", command=self._submit).grid(row=5, column=0, columnspan=3, pady=10)

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
        if self.design_mode.get() == "file":
            design_path = Path(self.design_path_var.get()).expanduser()
            self._create(project_dir, design_path=design_path, design_provided=True)
        else:
            name = self.name_var.get().strip() or project_dir.name
            description = self.desc_text.get("1.0", tk.END).strip()
            self._create(project_dir, name=name, description=description, design_provided=False)
        messagebox.showinfo("Success", f"Project initialized at {project_dir.resolve()}")
        self.root.quit()

    def _create(
        self,
        project_dir: Path,
        design_path: Path = None,
        name: str = "",
        description: str = "",
        design_provided: bool = True,
    ):
        if not project_dir.exists():
            raise FileNotFoundError(f"Directory {project_dir} does not exist.")

        if design_provided:
            if design_path is None:
                design_path = project_dir / "design.md"
            # Always rename the copied design document to "design.md" inside the
            # new project regardless of the original file name.
            create_file(
                project_dir / "design.md",
                Path(design_path).read_text(encoding="utf-8")
                if design_path.exists()
                else "",
            )
        else:
            create_file(project_dir / "design.md", _empty_design(name))

        create_file(project_dir / "AGENTS.md", _default_agents())
        create_file(project_dir / "tickets.md", _default_tickets(design_provided, name, description))


def main():
    gui = SetupWizardGUI()
    gui.root.mainloop()


if __name__ == "__main__":
    main()
