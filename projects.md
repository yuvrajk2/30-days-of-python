# Python Projects to Build

This is a focused project path, not a list of every possible Python
project. Build these projects in order. Start with the basic version, then
add the improvements listed for that project.

For every project, create a README, use functions instead of one giant
script, handle invalid input, and add tests for the important logic.

---

## 1. Simple Calculator

### What you will build

A command-line calculator that asks for two numbers and an operation, then
prints the result.

### It must be able to

- Add, subtract, multiply, and divide.
- Reject invalid numbers.
- Prevent division by zero.
- Let the user perform another calculation or exit.

### You will learn

Variables, input, type conversion, conditions, functions, loops, and
exception handling.

### Improve it later

Add powers, percentages, a calculation history, and tests for every
operation.

---

## 2. Expense Tracker

### What you will build

A command-line program where a user records personal expenses and checks
how much they have spent.

### It must be able to

- Add an expense with an amount, category, description, and date.
- List all expenses.
- Show the total amount spent.
- Filter expenses by category.
- Save expenses to a CSV or JSON file.
- Load saved expenses when the program starts.

### You will learn

Lists, dictionaries, dates, file handling, CSV/JSON, validation, and
separating data logic from the menu.

### Improve it later

Add monthly reports, spending limits, charts, and automated tests.

---

## 3. Library Management System

### What you will build

A small library program that manages books and records which books are
available or checked out.

### It must be able to

- Add, edit, remove, and list books.
- Search by title or author.
- Check out an available book.
- Return a checked-out book.
- Show which books are available.
- Save the library records to a file.

### You will learn

Classes, objects, dictionaries, CRUD operations, search, persistence, and
business rules.

### Improve it later

Add members, borrowing dates, overdue notices, a database, and tests for
checkout and return rules.

---

## 4. File Organizer

### What you will build

A utility that scans a folder and moves files into folders such as
`Images`, `Documents`, `Videos`, and `Other` based on their extensions.

### It must be able to

- Accept a folder path from the user.
- Detect file extensions.
- Create destination folders when needed.
- Move files safely.
- Avoid overwriting files with the same name.
- Show a summary of what was moved.

### You will learn

`pathlib`, filesystem operations, functions, error handling, and safe
automation.

### Improve it later

Add a preview mode, undo support, a configuration file, logging, and tests
using temporary directories.

---

## 5. Weather API Client

### What you will build

A command-line application that asks for a city and displays current
weather information from a public weather API.

### It must be able to

- Accept a city name.
- Call an HTTP API.
- Display temperature, conditions, and location.
- Handle an unknown city.
- Handle network errors and API errors.
- Read the API key from an environment variable instead of source code.

### You will learn

HTTP requests, JSON responses, environment variables, API keys, error
handling, and working with external services.

### Improve it later

Add a five-day forecast, response caching, unit selection, tests with mocked
responses, and a simple web interface.

---

## 6. To-Do REST API

### What you will build

A web API where clients can create, view, update, and delete to-do items.
Use Flask or FastAPI.

### It must be able to

- `GET /tasks` — list tasks.
- `GET /tasks/{id}` — view one task.
- `POST /tasks` — create a task.
- `PATCH /tasks/{id}` — update a task.
- `DELETE /tasks/{id}` — delete a task.
- Validate required fields.
- Return useful HTTP status codes and error messages.
- Store tasks in SQLite or another database.

### You will learn

REST APIs, routing, JSON, validation, databases, HTTP status codes, and
automated API tests.

### Improve it later

Add user accounts, authentication, pagination, filtering, OpenAPI
documentation, database migrations, and deployment.

---

## 7. Background Job Queue

### What you will build

A service that accepts jobs, places them in a queue, and lets a worker
process them in the background. Example jobs include sending an email,
generating a report, or resizing an image.

### It must be able to

- Add a job to a queue.
- Give each job an ID and status.
- Process jobs with a worker.
- Mark jobs as completed or failed.
- Retry a failed job a limited number of times.
- Record useful logs without exposing secrets.

### You will learn

Queues, workers, concurrency, retries, logging, job status, and designing
reliable long-running programs.

### Improve it later

Add scheduled jobs, multiple workers, persistent storage, graceful shutdown,
monitoring, and a web dashboard.

---

# Recommended Build Order

1. Simple Calculator
2. Expense Tracker
3. Library Management System
4. File Organizer
5. Weather API Client
6. To-Do REST API
7. Background Job Queue

The first four build your Python fundamentals. The Weather API Client
teaches external services. The REST API teaches backend development. The
Background Job Queue is the advanced project that combines reliability,
concurrency, and production-style thinking.

# Definition of Done

A project is finished when:

- Another person can run it by following the README.
- The main user flow works from start to finish.
- Invalid input produces a clear error.
- Important logic is covered by tests.
- Secrets are stored outside the code.
- The code is formatted and organized into understandable files.
- You have written down one limitation and one future improvement.