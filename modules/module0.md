# Module 0 – Setup & Tools 🛠️

> "A good craftsman never blames his tools. But he does learn how to use them well."

This preliminary module prepares your environment so you're ready to write the code that will power the rest of the guide. Every bit of software and workflow introduced here will be used continuously throughout the course.

---

## 0.1 Installing Python & Managing Versions
Python is the programming language we'll use. Find the latest stable release at [python.org](https://www.python.org/downloads/).

### 0.1.1 Windows Setup
1. Download the Windows installer (3.x series).
2. **Important:** check "Add Python to PATH" during installation.
3. After installation, open PowerShell and run:
   ```powershell
   python --version
   pip --version
   ```
   You should see versions displayed (e.g. `Python 3.11.2`).

### 0.1.2 Virtual Environments
A **virtual environment** (often shortened to *venv*) is a self-contained directory tree that contains a **Python interpreter** and a **private set of installed packages**. When you activate the environment, your `python` and `pip` commands reference the copies inside the venv instead of the global installation.

Think of a venv as a sandbox: each project gets its own sandbox where you can install whatever dependencies you need without worrying about version conflicts with other projects or the system Python. This isolation is crucial when different modules or libraries require incompatible versions of the same package.

#### How it works
- The `venv` module (part of the standard library) creates a folder structure like:
  ```text
  .venv/
    Scripts/       # executables (python.exe, pip.exe, activate scripts)
    Lib/           # installed packages
    pyvenv.cfg     # configuration metadata
  ```
- Activation simply adjusts your **PATH** so that the shell resolves `python` and `pip` to the venv copies. Nothing magical is installed globally; the environment can be deleted without impacting other code.

#### Creating and using a venv
```powershell
# make a new environment in the current folder
python -m venv .venv

# switch into it (PowerShell syntax)
.\.venv\Scripts\Activate

# upgrade core tooling inside the venv
pip install --upgrade pip setuptools wheel
```

Once activated, any package you install with `pip install` is placed into `.venv\Lib\site-packages` and will only be available while this venv is active. You can have multiple venvs side by side (e.g. `.venv`, `env`, `venv3.9`) each with different dependency sets.

#### Why use venvs?
- **Dependency management:** avoid "it works on my machine" problems.
- **Reproducibility:** the `requirements.txt` or `pip freeze` output from one venv can recreate the same environment on another computer.
- **System safety:** you won't accidentally upgrade or break the system Python used by the OS.

To deactivate the environment, run:
```powershell
Deactivate
```
After deactivation, `python` and `pip` revert to the global installation.

A well‑maintained project always includes instructions for creating and activating a virtual environment as part of its setup steps.

---

## 0.2 Choosing and Configuring an IDE
We recommend **Visual Studio Code** (VS Code): lightweight, extensible, and free.

### 0.2.1 Installation & Setup
1. Download from https://code.visualstudio.com/.
2. Install the **Python** extension by Microsoft.
3. In VS Code, open the project folder (`machine-learning-study-guide`).
4. Select the Python interpreter from the status bar (`.venv` if using virtual env).

### 0.2.2 Useful Extensions
- **Pylance** – for type checking and completion
- **GitLens** – enhances Git support
- **Jupyter** – run notebooks inline

Configure formatting (e.g., Black or autopep8) and linting via settings.

---

## 0.3 Git & GitHub
Version control is essential for tracking your progress and collaborating.

### 0.3.1 Git Basics
1. Install Git from https://git-scm.com/.
2. Configure your identity:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
3. Initialize a repository:
   ```bash
   git init
   git add README.md
   git commit -m "Initial commit"
   ```

### 0.3.2 GitHub Workflow
1. Create a new repository on GitHub with a similar name.
2. Add it as a remote and push:
   ```bash
   git remote add origin https://github.com/username/machine-learning-study-guide.git
   git push -u origin main
   ```
3. Make commits regularly; use branches for experiments.

---

## 0.4 Command Line Fundamentals (PowerShell)
The command line is how you’ll run scripts and manage files.

### 0.4.1 Navigation
- `pwd` – print working directory
- `ls` or `Get-ChildItem` – list files
- `cd folder` – change directory

### 0.4.2 Running Python
```powershell
python script.py
```
- Use `python -m` to run modules
o
- Press `Ctrl+C` to stop a running script

### 0.4.3 Editing Files
You can open files in VS Code directly from the terminal:
```powershell
code .  # open current folder
code modules\module0.md
```

---

## 0.5 Productivity Tips
- **README**: keep it updated with instructions and links.
- **Documentation**: write comments in your code and maintain a `docs/` folder if necessary.
- **Backup**: push to GitHub frequently.

---

## 0.6 Delivery: Hello World Repository
Perform these steps as your first delivery:
1. Create a GitHub repo called `machine-learning-study-guide` (or similar).
2. Clone it locally.
3. Add a Python file `hello_world.py` containing:
   ```python
   print("Hello, world!")
   ```
4. Commit and push the file.
5. Record the URL to the repository in a local note.

When done, share the link with a friend or keep it for yourself—this confirms your toolchain works.

---

## 0.7 Recommended Reading
- Python’s official [installation guide](https://docs.python.org/3/using/index.html)
- GitHub’s [Hello World guide](https://docs.github.com/en/get-started/quickstart/hello-world)
- PowerShell [getting started](https://learn.microsoft.com/powershell/scripting/learn/ps101/01-getting-started)


---

*With your environment ready, you are fully equipped to tackle Module 1 and beyond.*