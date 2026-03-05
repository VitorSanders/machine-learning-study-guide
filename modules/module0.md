# Module 0 – Setup & Tools 🛠️

> "Every expert started by setting up their first environment."

**Resources:**
- Friendly walkthroughs (YouTube search "install Python Windows 3.x beginner")
- Intro Git video or blog (e.g. "Git for Beginners" on freeCodeCamp)
- VS Code Quick Start guide

This preliminary module makes sure you have the same basic tools used by professional developers. Before writing a single line of Python, you’ll understand what each piece of software is for and why it matters, so you won’t feel like you’re just following arbitrary commands.

---

---

## 0.1 Installing Python & Managing Versions
Before you can write any code, you need a program that understands Python instructions. Python is the language in which you’ll tell the computer what to do, and installing it gives you the interpreter that executes your programs. This section explains why and how you install Python.

Python is the programming language we'll use. Find the latest stable release at [python.org](https://www.python.org/downloads/).

### 0.1.1 Windows Setup
These steps get Python onto your computer and make it easy to run from the command line.

1. Download the Windows installer (3.x series).
2. **Important:** check "Add Python to PATH" during installation — this lets you type `python` anywhere.
3. After installation, open PowerShell and run:
   ```powershell
   python --version
   pip --version
   ```
   You should see versions displayed (e.g. `Python 3.11.2`).

If you see an error like "python is not recognized", you either skipped the PATH step or need to close and reopen the terminal. See the troubleshooting section below.

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
Git is a tool that **remembers every change** you make to your files. Imagine writing a story and saving a checkpoint every few paragraphs; if you later dislike your edits you can go back to an earlier checkpoint. That’s what a *commit* is. GitHub is an online service that stores your project so you can access it from any computer or share it with others.

Understanding Git will save you from the chaos of accidentally deleting work or losing track of what you changed.

### 0.3.1 Git Basics
1. Install Git from https://git-scm.com/.
2. Configure your identity (author name and email used in commits):
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "you@example.com"
   ```
3. Initialize a repository (think of this as starting a new save file):
   ```bash
   git init             # create a hidden .git folder that will track changes
   git add README.md    # stage README.md for saving
   git commit -m "Initial commit"  # create your first checkpoint
   ```
   - `git add` tells Git which files you want to include in the next commit.
   - `git commit` actually records a snapshot of the staged files.

Later, `git status` will show what has changed, and `git log` shows the history of commits.

### 0.3.2 GitHub Workflow
1. Create a new repository on GitHub with a similar name.
2. Add it as a *remote* — a copy of your project stored online — and push your commits there:
   ```bash
   git remote add origin https://github.com/username/machine-learning-study-guide.git
   git push -u origin main   # upload your local commits to GitHub
   ```
   - `git push` sends your local commits to the remote and makes the online copy match your computer.
3. Make commits regularly; use branches (separate lines of work) when trying experimental changes.

Think of the remote like cloud storage for your save files; you can access it from anywhere and others can review your progress.

---

## 0.4 Command Line Fundamentals (PowerShell)
The command line is a text interface where you type commands to instruct your computer. It may look intimidating at first, but every developer uses it—it’s faster than clicking around.

### 0.4.1 Navigation
- `pwd` – print working directory
- `ls` or `Get-ChildItem` – list files
- `cd folder` – change directory

### 0.4.2 Running Python
```powershell
python script.py
```
- Use `python -m module_name` to run modules from a package.
- Press `Ctrl+C` to stop a running script if it gets stuck.

### 0.4.3 Editing Files
You can open files in VS Code directly from the terminal:
```powershell
code .  # open current folder
code modules\module0.md
```

---

## 0.5 Productivity Tips
This section is optional for now; as you become more comfortable with tools you'll naturally start organizing your work. For beginners it can be enough to remember to:
- Save your code frequently and commit to Git so you don’t lose progress.
- Write short comments explaining what a tricky piece of code does.
- Keep instructions in the README so you or others can run your project later.

---

## 0.6 Delivery: Hello World Repository
This is your first coding milestone. You’ve installed Python, set up Git, and now you’ll create a repository and push a simple script. Celebrate this moment—you now have the **same setup used by professional machine learning engineers**!

Steps:
1. Create a GitHub repo called `machine-learning-study-guide` (or similar).
2. Clone it locally:
   ```bash
   git clone https://github.com/username/machine-learning-study-guide.git
   cd machine-learning-study-guide
   ```
3. Add a Python file `hello_world.py` containing:
   ```python
   print("Hello, world!")
   ```
4. Commit and push the file:
   ```bash
   git add hello_world.py
   git commit -m "Add hello world"
   git push
   ```
5. Open the URL of your repository in a browser and admire your work—the code you just wrote is now accessible online!

Share this link with a friend or save it somewhere; it’s your first step on the machine learning journey and a great thing to look back on.

---

## 0.7 Recommended Reading
- "Installing Python on Windows" (search for a short YouTube video) – a visual walk‑through is easier than reading docs.
- freeCodeCamp’s [Git & GitHub for Beginners](https://www.freecodecamp.org/news/git-and-github-for-beginners/) article.
- Intro to PowerShell video or blog (look for "PowerShell for absolute beginners").


---

## 0.8 Common Issues & Troubleshooting
A few things beginners frequently run into:
- **Python not recognized**: you skipped the "Add Python to PATH" option or reopened the terminal after installation.
- **Wrong Python version**: some systems have `python` pointing to Python 2. If `python --version` shows `2.x`, try `python3` instead or adjust your PATH.
- **pip not found**: run `python -m ensurepip --upgrade` to install pip.
- **Git command not found**: make sure Git is installed and open a new terminal; the installer adds it to PATH.

If you run into other errors, search the exact message online—most issues have already been solved on Stack Overflow.

*With your environment ready, you are fully equipped to tackle Module 1 and beyond.*