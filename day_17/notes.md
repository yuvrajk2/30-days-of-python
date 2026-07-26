# Python Notes – Day 17
## Virtual Environments and pip

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand why virtual environments are needed.
- Create and activate a virtual environment.
- Install, upgrade, and uninstall packages with `pip`.
- Freeze and restore dependencies with `requirements.txt`.

---

# The Problem Without Virtual Environments

When you work on multiple Python projects, each may need different versions of the same library:

- Project A needs `requests==2.26`
- Project B needs `requests==2.31`

Installing globally causes version conflicts. Virtual environments solve this by giving each project its own isolated package space.

---

# Virtual Environment Tools

| Tool | Description |
|------|-------------|
| `venv` | Built-in (Python 3.3+) — recommended |
| `virtualenv` | Third-party, supports older Python |
| `conda` | Manages both packages and Python versions |
| `poetry` | Modern dependency management (Day 18) |

---

# Creating a Virtual Environment

```bash
# Create
python -m venv venv

# Windows activate
venv\Scripts\activate

# macOS/Linux activate
source venv/bin/activate

# Deactivate (any platform)
deactivate
```

When activated, your terminal prompt shows `(venv)`.

---

# Verifying the Environment

```bash
which python    # macOS/Linux
where python    # Windows

python --version
pip --version
```

Both should point inside the `venv` folder.

---

# pip – Python Package Installer

| Command | Description |
|---------|-------------|
| `pip install package` | Install latest version |
| `pip install package==1.2.3` | Install specific version |
| `pip install package>=1.0` | Install at least version 1.0 |
| `pip install -r requirements.txt` | Install from file |
| `pip uninstall package` | Remove a package |
| `pip list` | List installed packages |
| `pip show package` | Show package details |
| `pip search keyword` | Search PyPI (deprecated; use pypi.org) |
| `pip freeze` | Output installed packages and versions |
| `pip install --upgrade package` | Upgrade a package |

---

# `requirements.txt`

A file listing all packages a project needs.

## Create

```bash
pip freeze > requirements.txt
```

## Contents Example

```
requests==2.31.0
flask==3.0.0
python-dotenv==1.0.0
```

## Restore (on another machine)

```bash
pip install -r requirements.txt
```

---

# Typical Project Setup Workflow

```bash
# 1. Create the project folder
mkdir my_project && cd my_project

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate   # macOS/Linux

# 4. Install packages
pip install requests flask

# 5. Save dependencies
pip freeze > requirements.txt

# 6. Work on the project...

# 7. Deactivate when done
deactivate
```

---

# `.gitignore` for Virtual Environments

Never commit the `venv` folder to git. Add to `.gitignore`:

```
venv/
__pycache__/
*.pyc
.env
```

---

# Useful Packages to Know

| Package | Purpose |
|---------|---------|
| `requests` | HTTP requests |
| `flask` | Web framework |
| `fastapi` | Modern async API framework |
| `sqlalchemy` | Database ORM |
| `pandas` | Data analysis |
| `numpy` | Numerical computing |
| `matplotlib` | Plotting |
| `pytest` | Testing |
| `black` | Code formatter |
| `python-dotenv` | Load `.env` files |
| `pydantic` | Data validation |

---

# Environment Variables with `.env`

Store secrets outside your code using a `.env` file.

```bash
pip install python-dotenv
```

`.env` file:

```
API_KEY=abc123secret
DATABASE_URL=sqlite:///mydb.db
DEBUG=True
```

Python code:

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
print(api_key)
```

---

# Checking Installed Package Info

```bash
pip show requests
```

**Output**

```
Name: requests
Version: 2.31.0
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Location: /path/to/venv/lib/...
Requires: certifi, charset-normalizer, idna, urllib3
```

---

# Common Mistakes

## Forgetting to Activate Before Installing

```bash
pip install flask   # installs globally if venv not active
```

Always check for `(venv)` in your prompt.

---

## Committing `venv/` to Git

The folder can be hundreds of MB. Use `.gitignore`.

---

## Missing `requirements.txt`

Without it, collaborators cannot reproduce your environment.

---

# Practice Tasks

## Basic

1. Create a virtual environment for a new project.
2. Activate and verify the environment.
3. Install `requests` and verify with `pip list`.
4. Show package details with `pip show`.
5. Create a `requirements.txt`.
6. Uninstall a package and verify.
7. Recreate the environment from `requirements.txt`.
8. Install a specific version of a package.
9. Upgrade an installed package.
10. Deactivate the virtual environment.

---

## Intermediate

11. Install `python-dotenv`, create a `.env` file, and load it in a script.
12. Create a project with multiple packages and record all dependencies.
13. Simulate a fresh install from `requirements.txt` in a new venv.
14. Use `pip list --outdated` to find packages that need upgrading.
15. Write a shell script that automates venv creation and package installation.

---

# Mini Project – Environment Setup

```bash
# Create a reusable setup script
```

```python
# setup_check.py — run after activating your venv

import sys
import importlib

required = ["requests", "flask", "python-dotenv"]

print(f"Python version: {sys.version}")
print(f"Python path:    {sys.executable}\n")

print("Package check:")
all_ok = True
for pkg in required:
    try:
        mod = importlib.import_module(pkg.replace("-", "_"))
        version = getattr(mod, "__version__", "unknown")
        print(f"  ✓ {pkg} ({version})")
    except ImportError:
        print(f"  ✗ {pkg} NOT INSTALLED")
        all_ok = False

print()
if all_ok:
    print("All required packages are installed. Environment ready!")
else:
    print("Run: pip install -r requirements.txt")
```

---

# Day 17 Summary

After completing Day 17, you should be able to:

- Create and activate a virtual environment with `venv`.
- Install, upgrade, and remove packages with `pip`.
- Manage dependencies using `requirements.txt`.
- Use `.env` files to manage secrets safely.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 20 minutes |
| Hands-on Setup | 45 minutes |
| Practice Tasks | 45 minutes |
| Mini Project | 20 minutes |

**Total:** Approximately **2 hours**
