# Python Notes – Day 20
## Code Formatting – black and ruff

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand why code formatting matters.
- Use `black` to auto-format Python code.
- Use `ruff` to lint and auto-fix code.
- Configure both tools in `pyproject.toml`.
- Integrate formatting into a development workflow.

---

# Why Format Code?

- **Readability** — consistent style makes code easier to read.
- **Team collaboration** — no arguments about spacing or quotes.
- **Fewer errors** — linters catch bugs before runtime.
- **Professionalism** — every serious Python project uses formatting.

> "Any style is better than no style. An automatic style is better than any style."

---

# PEP 8 — Python Style Guide

PEP 8 is the official Python style guide. Key rules:

| Rule | Example |
|------|---------|
| 4 spaces for indentation | `    return x` |
| 79 characters max per line | Keep lines short |
| Two blank lines between top-level defs | Function/class separation |
| One blank line between methods | Inside classes |
| Spaces around operators | `x = a + b` |
| No trailing whitespace | — |
| `snake_case` for variables/functions | `my_function` |
| `PascalCase` for classes | `MyClass` |
| `UPPER_CASE` for constants | `MAX_SIZE = 100` |

---

# black — The Uncompromising Formatter

`black` reformats your code to a consistent style with **zero configuration needed**.

```bash
pip install black
```

---

## Basic Usage

```bash
# Format a single file
black script.py

# Format an entire directory
black src/

# Check without changing (CI mode)
black --check src/

# Show a diff of what would change
black --diff script.py
```

---

## Before and After black

### Before

```python
def add(a,b):
    return a+b

x={'name':'Raj','age':20}
y=[1,2,   3,4,5]
if x['age']>18: print("adult")
```

### After `black`

```python
def add(a, b):
    return a + b


x = {"name": "Raj", "age": 20}
y = [1, 2, 3, 4, 5]
if x["age"] > 18:
    print("adult")
```

---

## What black Does

- Uses double quotes for strings.
- Adds trailing commas in long collections.
- Adds spaces around operators.
- Breaks long lines automatically.
- Adds/removes blank lines correctly.
- Formats function signatures consistently.

---

## Configuring black in `pyproject.toml`

```toml
[tool.black]
line-length = 88
target-version = ["py311"]
skip-string-normalization = false
exclude = '''
/(
    \.git
  | \.venv
  | dist
  | build
)/
'''
```

---

# ruff — Fast Python Linter and Formatter

`ruff` is an extremely fast linter (written in Rust) that also includes a formatter.

```bash
pip install ruff
```

---

## ruff Linting

```bash
# Lint a file
ruff check script.py

# Lint a directory
ruff check src/

# Auto-fix fixable issues
ruff check --fix src/

# Watch mode (re-runs on save)
ruff check --watch src/
```

---

## ruff Formatting (Replaces black)

```bash
# Format files
ruff format src/

# Check only
ruff format --check src/
```

---

## Common ruff Error Codes

| Code | Rule | Example |
|------|------|---------|
| `E501` | Line too long | Line > 88 chars |
| `F401` | Unused import | `import os` never used |
| `F811` | Redefined unused name | Define same var twice |
| `E711` | Comparison to None | `x == None` → `x is None` |
| `E712` | Comparison to True | `x == True` → `x is True` |
| `F841` | Local variable assigned but never used | `x = 5` then never used |
| `W292` | No newline at end of file | — |
| `I001` | Import order | Wrong import ordering |

---

## Configuring ruff in `pyproject.toml`

```toml
[tool.ruff]
line-length = 88
target-version = "py311"

[tool.ruff.lint]
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort (import sorting)
    "B",   # flake8-bugbear
    "UP",  # pyupgrade
]
ignore = ["E501"]  # ignore line-length (handled by formatter)
fixable = ["ALL"]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["F401"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

---

# isort — Import Sorting

`ruff` includes isort rules (`I`). Imports should be in this order:

1. Standard library (`os`, `sys`, `math`)
2. Third-party (`requests`, `flask`)
3. Local (`from myapp import utils`)

Each group separated by a blank line:

```python
# Correct order
import os
import sys

import requests
from flask import Flask

from myapp.utils import helper
```

---

# Complete Pre-commit Workflow

```bash
# Install pre-commit
pip install pre-commit
```

`.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.1.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
```

```bash
pre-commit install     # runs checks on every git commit
pre-commit run --all   # run on all files now
```

---

# black vs ruff Formatter

| Feature | black | ruff format |
|---------|-------|------------|
| Speed | Fast | ~100× faster |
| Compatibility | High | Very high (black-compatible) |
| Configuration | Minimal | Flexible |
| Standalone | Yes | Yes (ruff also lints) |

**Recommendation**: Use `ruff` for both linting and formatting in new projects.

---

# Practice Tasks

## Basic

1. Install `black` and `ruff`.
2. Write poorly-formatted Python code and run `black` on it.
3. Run `black --check` to see what would change without changing it.
4. Run `ruff check` on your project and review the errors.
5. Use `ruff check --fix` to auto-fix issues.
6. Configure `black` in `pyproject.toml`.
7. Configure `ruff` with specific rule sets.
8. Sort imports correctly using `ruff`'s `I` rules.
9. Add a line that is too long and see how `black` handles it.
10. Run `ruff format` on a file.

---

## Intermediate

11. Format an entire previous day's project with `black`.
12. Fix all linting issues `ruff` finds in your Day 18 project template.
13. Set up `pre-commit` with `ruff`.
14. Configure `ruff` to ignore specific rules per file.
15. Write a `Makefile` with targets: `format`, `lint`, `test`.

---

# Mini Project – Format Previous Projects

Apply formatting tools to all Python files from previous days:

```bash
# Install tools
pip install black ruff

# Check all previous days
black --check day_1/ day_2/ day_3/

# See what would change
black --diff day_2/basic.py

# Apply formatting
black day_1/ day_2/ day_3/ day_4/ day_5/

# Lint all files
ruff check day_1/ day_2/ day_3/ --fix

# Verify clean
ruff check day_1/ day_2/ day_3/
```

`format_all.py` — a helper script:

```python
import subprocess
import sys
from pathlib import Path

days = sorted(Path(".").glob("day_*/"))
py_files = [str(f) for d in days for f in d.glob("*.py")]

if not py_files:
    print("No Python files found.")
    sys.exit(0)

print(f"Found {len(py_files)} Python files\n")

print("Running black...")
subprocess.run(["black"] + py_files, check=False)

print("\nRunning ruff (auto-fix)...")
subprocess.run(["ruff", "check", "--fix"] + py_files, check=False)

print("\nRunning ruff (check)...")
result = subprocess.run(["ruff", "check"] + py_files, capture_output=True, text=True)
if result.returncode == 0:
    print("All files are clean!")
else:
    print(result.stdout)
```

---

# Day 20 Summary

After completing Day 20, you should be able to:

- Format code automatically with `black`.
- Lint and auto-fix code with `ruff`.
- Configure both tools in `pyproject.toml`.
- Organise imports correctly.
- Integrate formatting into your daily workflow.

---

# Week 3 Project Checkpoint – Password Manager

The roadmap's Week 3 goal is a Password Manager. For this learning project,
focus on structure, validation, and safe handling rather than building a
production password vault.

## Minimum Features

- Add a service name, username, and password entry.
- Search entries by service.
- Generate strong random passwords.
- Validate required fields.
- Save and load entries only in a clearly identified local practice file.

```python
import secrets
import string

def generate_password(length=16):
    if length < 8:
        raise ValueError("Password length must be at least 8")
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))
```

Use the Day 16 regex notes to validate service names and usernames, Day 19
type hints to describe records, and Day 20 formatting tools to keep the
project readable. Never commit real passwords or secret keys. A production
password manager requires encryption, key management, and careful security
review; this checkpoint is an educational prototype only.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 20 minutes |
| Hands-on Formatting | 45 minutes |
| Practice Tasks | 45 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **2.5 hours**
