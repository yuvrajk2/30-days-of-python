# Python Notes – Day 18
## pyproject.toml, Poetry, and Project Structure

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand `pyproject.toml` and why it replaces `setup.py`.
- Use Poetry for dependency management and packaging.
- Structure a Python project professionally.
- Understand what goes in each project file.

---

# Why Modern Project Tooling?

Traditional Python packaging (`setup.py`, `requirements.txt`) had many pain points:

- No lock file (reproducibility issues).
- Manual virtual environment management.
- Separate tools for packaging and dependency management.

Modern tools consolidate these into one workflow.

---

# `pyproject.toml`

The standard configuration file for Python projects (PEP 517/518/621).

```toml
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "my-project"
version = "0.1.0"
description = "A sample Python project"
authors = ["Raj <raj@example.com>"]
readme = "README.md"
python = "^3.11"

[tool.poetry.dependencies]
python = "^3.11"
requests = "^2.31"
flask = "^3.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^23.0"
ruff = "^0.1"
```

---

# Poetry

Poetry is a modern dependency manager and packaging tool.

## Installing Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

---

## Core Poetry Commands

| Command | Description |
|---------|-------------|
| `poetry new project-name` | Create a new project |
| `poetry init` | Initialise in an existing folder |
| `poetry install` | Install dependencies from lock file |
| `poetry add package` | Add a dependency |
| `poetry add --group dev package` | Add a dev-only dependency |
| `poetry remove package` | Remove a dependency |
| `poetry update` | Update all dependencies |
| `poetry run python script.py` | Run inside the venv |
| `poetry shell` | Activate the venv shell |
| `poetry show` | List installed packages |
| `poetry build` | Build distributable package |
| `poetry publish` | Publish to PyPI |
| `poetry lock` | Update `poetry.lock` |

---

## Creating a New Project

```bash
poetry new my-project
cd my-project

poetry add requests
poetry add --group dev pytest black
poetry install

poetry run python src/my_project/main.py
```

---

## `poetry.lock`

A lock file that pins exact versions of every package for reproducibility.

- Always commit `poetry.lock` to git.
- Never edit it manually.

---

# Standard Python Project Structure

```
my-project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── docs/
├── .env
├── .gitignore
├── pyproject.toml
├── poetry.lock
└── README.md
```

---

## What Each File Does

| File/Folder | Purpose |
|-------------|---------|
| `src/my_project/` | Main application code |
| `__init__.py` | Marks directory as a Python package |
| `tests/` | Unit and integration tests |
| `docs/` | Documentation |
| `.env` | Environment variables (never commit) |
| `.gitignore` | Files to exclude from git |
| `pyproject.toml` | Project metadata, dependencies, tool config |
| `poetry.lock` | Exact locked dependency versions |
| `README.md` | Project documentation |

---

## `.gitignore` Template

```
# Virtual environment
.venv/
venv/
__pycache__/
*.pyc
*.pyo

# Environment variables
.env

# Build artifacts
dist/
build/
*.egg-info/

# IDE files
.idea/
.vscode/

# Coverage reports
.coverage
htmlcov/
```

---

# `__init__.py`

Makes a directory a Python package.

```python
# src/my_project/__init__.py
__version__ = "0.1.0"
```

---

# Configuring Tools in `pyproject.toml`

```toml
[tool.black]
line-length = 88
target-version = ["py311"]

[tool.ruff]
line-length = 88
select = ["E", "F", "W"]
ignore = ["E501"]

[tool.pytest.ini_options]
testpaths = ["tests"]
```

---

# Alternative: `setup.py` and `setup.cfg` (Legacy)

Still seen in older projects.

```python
# setup.py (legacy)
from setuptools import setup, find_packages

setup(
    name="my-project",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["requests>=2.31"],
)
```

Prefer `pyproject.toml` for new projects.

---

# Practice Tasks

## Basic

1. Install Poetry on your system.
2. Create a new project with `poetry new`.
3. Add `requests` as a dependency.
4. Add `pytest` and `black` as dev dependencies.
5. Run `poetry show` to view installed packages.
6. Run a script with `poetry run python`.
7. Create the standard folder structure manually.
8. Write a basic `README.md`.
9. Create a `.gitignore` for a Python project.
10. Initialise a git repository and make an initial commit.

---

## Intermediate

11. Configure `black` settings in `pyproject.toml`.
12. Configure `ruff` for linting in `pyproject.toml`.
13. Configure `pytest` paths in `pyproject.toml`.
14. Build the project with `poetry build`.
15. Explore `poetry.lock` and understand its structure.

---

# Mini Project – Python Project Template

Create a complete ready-to-use project template:

```
calculator-project/
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── operations.py
├── tests/
│   └── test_operations.py
├── pyproject.toml
├── README.md
└── .gitignore
```

**`src/calculator/operations.py`**

```python
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
```

**`tests/test_operations.py`**

```python
import pytest
from calculator.operations import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 8

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
```

**`pyproject.toml`**

```toml
[tool.poetry]
name = "calculator"
version = "0.1.0"
description = "A simple calculator"
authors = ["Your Name"]

[tool.poetry.dependencies]
python = "^3.11"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0"
black = "^23.0"
```

---

# Day 18 Summary

After completing Day 18, you should be able to:

- Understand `pyproject.toml` and its role in modern Python.
- Use Poetry to create and manage projects.
- Apply the standard Python project structure.
- Configure tools like `black`, `ruff`, and `pytest` in `pyproject.toml`.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Hands-on Setup | 60 minutes |
| Practice Tasks | 45 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
