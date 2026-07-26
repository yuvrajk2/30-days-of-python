# Python Developer Project Roadmap

This roadmap contains projects a Python developer should build to turn
language knowledge into practical experience. Work through the levels in
order, but revisit earlier projects when you learn a better technique.

For every project, write a README, use a virtual environment, validate
inputs, handle expected errors, and add tests for the important behavior.

## How to Use This Roadmap

For each project:

1. Build a small working version first.
2. Separate user-interface code from business logic.
3. Store data in an appropriate format.
4. Add tests before making large refactors.
5. Add type hints, docstrings, and formatting.
6. Record limitations and future improvements in the README.

The goal is not to collect unfinished tutorials. The goal is to finish
projects that another person can run, understand, and use.

---

# Level 1 – Beginner Mini Projects

These projects develop syntax, input/output, conditionals, loops, functions,
and basic collections.

| Project | Core skills |
|---------|-------------|
| Simple Calculator | Input, arithmetic, functions, error handling |
| Unit Converter | Functions, menus, numeric conversion |
| Grade Calculator | Conditions, validation, averages |
| Number Guessing Game | Loops, `random`, attempts, hints |
| Multiplication Table Generator | Loops, ranges, formatted output |
| Rock-Paper-Scissors | Conditions, randomness, score tracking |
| Dice Rolling Simulator | Modules, loops, random values |
| Mad Libs Generator | Strings, templates, user input |
| Temperature Converter | Functions, formulas, validation |
| Leap Year and Age Calculator | Dates, conditions, input validation |
| Basic Quiz Game | Lists, dictionaries, scoring |
| Countdown Timer | Loops, `time`, formatted output |

## Beginner Definition of Done

- The program has a clear start and exit path.
- Invalid input does not crash the program unexpectedly.
- Repeated logic is moved into functions.
- The README includes an example session.
- At least five normal and edge-case inputs have been tried.

## Beginner Upgrade Challenge

Choose one project and add:

- A menu-driven interface.
- A replay option.
- Persistent high scores or history in a JSON file.
- Automated tests for the core functions.

---

# Level 2 – Core Python Projects

These projects develop lists, dictionaries, files, exceptions, modules, and
object-oriented programming.

| Project | Core skills |
|---------|-------------|
| Student Marks Manager | Lists, dictionaries, averages, reports |
| Contact Book | CRUD operations, searching, JSON persistence |
| Student Management System | Classes, validation, file storage |
| Expense Tracker | CSV/JSON files, dates, totals, filtering |
| To-Do List CLI | CRUD, priorities, due dates, persistence |
| Notes Application | File handling, search, timestamps |
| Library Management System | OOP, checkout rules, records |
| Inventory Management System | Products, stock levels, reports |
| Bank Account Simulator | Classes, transactions, exceptions |
| ATM Simulation | Authentication flow, balance rules, menus |
| File Organizer | `pathlib`, file extensions, safe moves |
| Log File Analyzer | Text processing, regular expressions, reports |
| Password Generator | `secrets`, character sets, validation |
| Address Book Importer | CSV parsing, duplicate detection, export |
| Personal Finance Report | Categories, date ranges, aggregation |

## Core Project Definition of Done

- Data operations are separated from the command-line interface.
- The program handles missing files and malformed records.
- Classes are used where they make the domain clearer.
- Records can be added, viewed, edited, and deleted where appropriate.
- Tests cover success, empty, duplicate, missing, and invalid cases.

## Core Upgrade Challenge

Convert one command-line project into a reusable Python package:

- Add a `pyproject.toml`.
- Add a `src/` package layout.
- Add type hints and docstrings.
- Add a test suite.
- Add a command-line entry point.
- Use `logging` instead of scattered debug prints.

---

# Level 3 – Intermediate Portfolio Projects

These projects introduce APIs, databases, authentication, web interfaces,
external services, and stronger testing.

| Project | Core skills |
|---------|-------------|
| To-Do REST API | Flask/FastAPI, CRUD routes, JSON, status codes |
| Student REST API | Pydantic validation, filtering, pagination |
| Book Review API | Relationships, authentication, database queries |
| Habit Tracker | Dates, recurring data, dashboards |
| Weather API Client | HTTP requests, API errors, caching |
| Currency Converter | External API integration, rates, fallbacks |
| URL Shortener | Database models, unique codes, redirects |
| Blog API | Users, posts, permissions, pagination |
| Recipe Manager | Search, tags, images, structured data |
| Job Application Tracker | Forms, statuses, reminders, reporting |
| Help Desk Ticket System | Roles, workflows, comments, audit history |
| Personal Dashboard | Multiple data sources, charts, scheduled updates |
| Web Scraper and Monitor | Requests, parsing, rate limits, change detection |
| Email Report Generator | Templates, scheduled jobs, attachments |
| Chat Application | WebSockets, sessions, message history |

## Intermediate Project Definition of Done

- The API has documented endpoints and example requests.
- Request data is validated at the boundary.
- Errors use useful messages and appropriate HTTP status codes.
- Data is stored in SQLite or PostgreSQL instead of only memory.
- Authentication and authorization rules are explicit.
- Tests include API routes and important business rules.
- Configuration and secrets are read from environment variables.
- The project includes a local setup guide.

## Intermediate Upgrade Challenge

Deploy one API and add:

- Database migrations.
- Structured logging.
- Health and readiness endpoints.
- API documentation with OpenAPI.
- Rate limiting or request-size limits.
- A CI check that runs formatting, linting, and tests.

---

# Level 4 – Advanced Python Projects

These projects demonstrate architecture, concurrency, algorithms,
observability, security awareness, and production-quality engineering.

| Project | Core skills |
|---------|-------------|
| E-commerce Backend | Domain modeling, payments, orders, inventory |
| Multi-tenant SaaS API | Tenant isolation, roles, billing boundaries |
| Background Job Queue | Workers, retries, scheduling, idempotency |
| Distributed Web Scraper | Async I/O, queues, rate limiting, persistence |
| Data Pipeline | ETL, validation, batching, observability |
| Recommendation Engine | Data processing, ranking, evaluation |
| Search Service | Indexing, tokenization, ranking, query performance |
| Real-Time Collaboration Tool | WebSockets, concurrency, conflict handling |
| Event-Driven Order System | Events, consumers, retries, dead-letter handling |
| Feature Flag Service | Rule evaluation, caching, audit history |
| Metrics and Monitoring Service | Time series, aggregation, alerting |
| Secure Secrets Vault Prototype | Encryption concepts, access control, auditing |
| Static Type Checker or Linter | AST parsing, visitors, diagnostics |
| Python Package for Public Release | API design, packaging, compatibility |
| Custom Scheduler | Priority queues, persistence, job execution |

## Advanced Project Definition of Done

- The architecture and major trade-offs are documented.
- Components have clear boundaries and interfaces.
- Long-running or concurrent work can be observed and stopped safely.
- Retries do not duplicate unsafe operations.
- Sensitive data is not logged or committed.
- Performance characteristics are measured rather than guessed.
- Tests include failure paths and integration behavior.
- The project has reproducible development and deployment instructions.

## Advanced Upgrade Challenge

For one project, add:

- Docker or a documented production-like environment.
- CI/CD checks.
- Structured logs and metrics.
- Load or performance tests.
- A threat model and security review.
- A rollback or recovery plan.

---

# Essential Projects by Python Career Direction

## Python Backend Developer

Build a CRUD API, authentication service, blog API, background job queue,
and one production-style database application.

## Data and Automation Developer

Build a CSV/JSON pipeline, web scraper, ETL system, report generator, and
dashboard that explains the output.

## QA or Test Automation Developer

Build a tested CLI application, API test suite, browser automation project,
fixture library, and CI pipeline.

## Data Scientist or Machine Learning Developer

Build a data-cleaning pipeline, exploratory analysis notebook, prediction
service, model evaluation report, and monitored inference API.

## DevOps or Platform Developer

Build a log analyzer, deployment health checker, job scheduler, metrics
collector, and service that exposes health and readiness information.

---

# Portfolio Standards

Every portfolio project should include:

- A concise README explaining the problem and intended user.
- Installation and run instructions that work from a clean checkout.
- Screenshots, sample output, or API examples.
- A clear project structure.
- A `pyproject.toml` with project metadata and tools.
- Type hints on important public functions.
- Automated tests and one documented test command.
- Consistent formatting and linting.
- Explicit error handling.
- No committed passwords, tokens, or private data.
- A short section describing trade-offs and future work.

Avoid presenting ten nearly identical tutorial projects. A stronger portfolio
has three to five finished projects that show increasing complexity and
different skills.

---

# Suggested Portfolio Sequence

Complete these projects in order:

1. **Expense Tracker CLI** – files, validation, reports, tests.
2. **Library Management System** – OOP, search, persistence.
3. **File Organizer** – filesystem operations and safe error handling.
4. **To-Do REST API** – Flask or FastAPI, validation, JSON, tests.
5. **Weather API Client** – external APIs, caching, failure handling.
6. **Blog or Book Review API** – authentication, database relationships.
7. **Background Job Queue** – workers, retries, logging, scheduling.
8. **Capstone of Choice** – a complete application with documentation,
   testing, deployment, and a retrospective.

---

# Final Project Checklist

- [ ] The project solves a specific problem.
- [ ] The smallest useful version is complete.
- [ ] The main flow is tested.
- [ ] Invalid input is handled explicitly.
- [ ] Data persistence is reliable when required.
- [ ] Configuration is separate from source code.
- [ ] Documentation is sufficient for a new user.
- [ ] Formatting, linting, and tests pass.
- [ ] The README explains one important design decision.
- [ ] The project has a realistic next improvement.