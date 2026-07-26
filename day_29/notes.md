# Python Notes – Day 29
## Documentation with Sphinx and Introduction to Flask or FastAPI

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Write useful docstrings and README documentation.
- Understand the role of Sphinx in generating documentation.
- Create a minimal Flask web API.
- Create a minimal FastAPI web API.
- Choose a framework based on project needs.

---

# Why Documentation Matters

Documentation helps another person understand how to install, use, and
extend a project. It also helps your future self.

Useful documentation usually includes:

- What the project does.
- Installation instructions.
- A quick-start example.
- Input and output formats.
- Error behavior.
- Development and testing commands.

---

# Docstrings

A docstring describes a module, function, class, or method:

```python
def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert a temperature from Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32
```

Python exposes docstrings through `help()` and the `__doc__` attribute:

```python
print(celsius_to_fahrenheit.__doc__)
```

Document parameters, return values, raised exceptions, and side effects
when they are not obvious.

---

# Sphinx

Sphinx turns reStructuredText or Markdown source files into HTML, PDF, and
other documentation formats. It is commonly used for Python libraries.

Install and initialize a documentation project:

```bash
python -m pip install sphinx
mkdir docs
cd docs
sphinx-quickstart
```

For a Python package, enable autodoc in `conf.py` and add extensions:

```python
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]
```

`autodoc` can include documentation from Python docstrings. `napoleon`
allows Google-style and NumPy-style docstrings.

Build HTML documentation from the `docs` directory:

```bash
sphinx-build -b html . _build/html
```

The generated site is in `docs/_build/html`. Keep generated output out of
version control unless the project specifically publishes it.

---

# Documenting a Function

```python
def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: The numerator.
        b: The denominator. Must not be zero.

    Returns:
        The quotient.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b
```

Good documentation explains the contract rather than repeating the code.

---

# What Is a Web API?

An API lets programs communicate over HTTP. A REST-style API commonly uses:

| Method | Typical purpose |
|--------|-----------------|
| `GET` | Read data |
| `POST` | Create data |
| `PUT`/`PATCH` | Update data |
| `DELETE` | Remove data |

Common status codes include `200 OK`, `201 Created`, `400 Bad Request`,
`404 Not Found`, and `500 Internal Server Error`.

JSON is a common format for request and response bodies.

---

# 1. Minimal Flask API

Flask is a lightweight framework with a flexible, explicit style:

```bash
python -m pip install flask
```

Create `app.py`:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/hello")
def hello():
    return jsonify({"message": "Hello, Python API!"})

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
```

Run it:

```bash
python app.py
```

Then open `http://127.0.0.1:5000/hello`.

Do not use `debug=True` in production. Development debug mode can expose
useful diagnostics that should not be public.

---

# 2. Minimal FastAPI API

FastAPI uses Python type hints to validate data and generate interactive
OpenAPI documentation:

```bash
python -m pip install fastapi uvicorn
```

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI(title="Study API")

@app.get("/hello")
def hello():
    return {"message": "Hello, Python API!"}

@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}
```

Run it:

```bash
uvicorn main:app --reload
```

FastAPI provides interactive documentation at `/docs` and an alternative
documentation page at `/redoc`.

---

# Flask or FastAPI?

Choose **Flask** when you want:

- A small, flexible framework.
- Minimal built-in assumptions.
- To choose extensions yourself.

Choose **FastAPI** when you want:

- Type-based request validation.
- Automatic OpenAPI documentation.
- Modern async support and strong editor hints.

Both can build production APIs. Learn the conventions of the framework you
choose and keep routes, validation, business logic, and storage organized.

---

# API Design Checklist

Before calling an API complete, check:

1. Are routes named consistently?
2. Are inputs validated?
3. Are errors returned with useful status codes?
4. Is the response shape documented?
5. Are secrets and debug settings kept out of production?
6. Are endpoints covered by automated tests?

---

# Practice Questions

## Basic

1. Add a `/greet/<name>` route in Flask.
2. Add a `/students` route in FastAPI.
3. Write a docstring for a calculator function.
4. Return a `404` response for a missing item.
5. List the API endpoints in a README.

## Intermediate

6. Add a POST endpoint that validates JSON input.
7. Create a Sphinx page that includes module docstrings.
8. Add tests for the API health endpoint.
9. Separate API routes from business logic.
10. Compare Flask and FastAPI response validation.

---

# Mini Project – Simple REST API

Build a small student or task API with:

- `GET /items` to list items.
- `GET /items/<id>` to retrieve one item.
- `POST /items` to create an item.
- Validation for required fields.
- A useful `404` response for missing items.
- A README containing setup, run, and example requests.

Start with in-memory data:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
items = [{"id": 1, "name": "Read Python notes"}]

@app.get("/items")
def list_items():
    return jsonify(items)

@app.post("/items")
def create_item():
    data = request.get_json(silent=True) or {}
    name = data.get("name", "").strip()
    if not name:
        return jsonify({"error": "name is required"}), 400

    item = {"id": len(items) + 1, "name": name}
    items.append(item)
    return jsonify(item), 201

if __name__ == "__main__":
    app.run()
```

After the basic version works, add tests and move the data operations into
separate functions.

---

# Day 29 Summary

After completing Day 29, you should be able to:

- Write clear docstrings and project documentation.
- Describe Sphinx's role in generating documentation.
- Build a minimal Flask API.
- Build a minimal FastAPI API.
- Validate inputs and return appropriate HTTP status codes.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 75 minutes |
| Practice Problems | 45 minutes |
| Mini Project | 60 minutes |

**Total:** Approximately **3.5 hours**