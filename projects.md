# Python Projects to Build

This is a focused project path, not a list of every possible Python
project. It contains 20 practical projects. Build them in order, starting
with the basic version and then adding the improvements listed for each
project.

For every project, create a README, use functions instead of one giant
script, handle invalid input, and add tests for the important logic.

---

# Beginner Projects

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

## 2. Unit Converter

### What you will build

A menu-driven program that converts values between units such as Celsius
and Fahrenheit, kilometers and miles, and kilograms and pounds.

### It must be able to

- Show available conversion choices.
- Accept a value from the user.
- Perform the selected conversion.
- Display the result with a clear unit.
- Reject invalid choices and values.

### You will learn

Functions, formulas, menus, numeric conversion, and input validation.

### Improve it later

Add more units, a two-way conversion option, and tests for every formula.

---

## 3. Quiz Game

### What you will build

A command-line quiz that asks multiple-choice questions and displays the
user's final score.

### It must be able to

- Store several questions and answer choices.
- Accept and check the user's answer.
- Keep track of the score.
- Show the correct answer when the user is wrong.
- Display the final score and percentage.

### You will learn

Lists, dictionaries, loops, conditions, functions, and scoring.

### Improve it later

Load questions from JSON, shuffle the questions, add categories, and save
high scores.

---

## 4. Number Guessing Game

### What you will build

A game where the computer chooses a random number and the user tries to
guess it.

### It must be able to

- Generate a random number in a chosen range.
- Tell the user whether the guess is too high or too low.
- Count the number of attempts.
- Stop when the user guesses correctly.
- Handle invalid guesses.

### You will learn

Loops, the `random` module, comparisons, counters, and exception handling.

### Improve it later

Add difficulty levels, a maximum number of guesses, and a high-score table.

---

## 5. Expense Tracker

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

## 6. Contact Book

### What you will build

A command-line contact book that stores people's names, phone numbers, and
email addresses.

### It must be able to

- Add a contact.
- List all contacts.
- Search by name or phone number.
- Edit and delete a contact.
- Save and load contacts from a JSON file.

### You will learn

Dictionaries, CRUD operations, searching, JSON persistence, and validation.

### Improve it later

Add groups, duplicate detection, CSV import/export, and alphabetical
sorting.

---

## 7. Library Management System

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

## 8. Student Management System

### What you will build

A program that stores student details and marks, then produces useful
student reports.

### It must be able to

- Add, edit, remove, and list students.
- Store marks for several subjects.
- Calculate each student's average and grade.
- Find the highest-scoring student.
- Save student records to a file.

### You will learn

Classes, lists, dictionaries, calculations, file handling, and reporting.

### Improve it later

Add attendance, search and filtering, a database, and a REST API.

---

## 9. File Organizer

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

## 10. Notes Application

### What you will build

A command-line notes application where users can create, search, edit, and
delete personal notes.

### It must be able to

- Create a note with a title and body.
- List all saved notes.
- Search note titles and content.
- Edit and delete notes.
- Save notes to JSON or text files.

### You will learn

File handling, timestamps, CRUD operations, searching, and error handling.

### Improve it later

Add tags, archive support, Markdown notes, and full-text search.

---

# Intermediate Projects

## 11. Weather API Client

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

## 12. Log File Analyzer

### What you will build

A tool that reads an application log file and reports how many information,
warning, and error messages it contains.

### It must be able to

- Read a log file line by line.
- Recognize log levels and timestamps.
- Count each type of message.
- Display the most common errors.
- Report malformed lines instead of silently ignoring them.

### You will learn

Text processing, regular expressions, dictionaries, files, and reporting.

### Improve it later

Add date filtering, CSV reports, charts, and support for large files.

---

## 13. To-Do REST API

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

## 14. Blog REST API

### What you will build

A web API where users can create accounts, publish blog posts, and leave
comments. Use Flask or FastAPI.

### It must be able to

- Register and authenticate users.
- Create, view, edit, and delete posts.
- List posts with pagination.
- Allow comments on posts.
- Prevent users from editing other users' posts.
- Store data in a database.

### You will learn

API design, authentication, authorization, database relationships,
validation, pagination, and API testing.

### Improve it later

Add tags, search, image uploads, email verification, and deployment.

---

## 15. Background Job Queue

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

## Advanced Projects

## 16. Web Scraper and Monitor

### What you will build

A program that visits selected web pages, extracts specific information,
and reports when that information changes.

### It must be able to

- Read a list of URLs from a configuration file.
- Fetch pages safely with timeouts.
- Extract the required text or data.
- Save previous results.
- Detect and report changes.
- Respect delays and handle failed requests.

### You will learn

HTTP clients, HTML parsing, configuration, persistence, scheduling, and
responsible automation.

### Improve it later

Add a dashboard, email notifications, concurrent requests, and a database.

---

## 17. E-commerce Backend

### What you will build

A backend for a small online store where customers can browse products,
add items to a cart, and place orders.

### It must be able to

- Create, edit, and list products.
- Organize products into categories.
- Add and remove products from a shopping cart.
- Create an order with customer and delivery details.
- Reduce product stock after an order is placed.
- Prevent orders when there is not enough stock.
- Store users, products, carts, and orders in a database.

### You will learn

Database relationships, transactions, business rules, authentication,
inventory management, and API design.

### Improve it later

Add payment-provider integration, order emails, coupons, product images,
admin permissions, and deployment.

---

## 18. Data Processing Pipeline

### What you will build

A program that reads raw data from CSV or JSON files, cleans it, validates
it, calculates useful results, and saves a report.

### It must be able to

- Read data from one or more input files.
- Detect missing, duplicate, and invalid records.
- Clean and normalize the data.
- Calculate summary statistics.
- Save cleaned data and a report.
- Log how many records succeeded or failed.

### You will learn

ETL design, data validation, generators, batching, logging, error reports,
and processing larger files efficiently.

### Improve it later

Add a database, scheduled runs, parallel processing, a dashboard, and
monitoring metrics.

---

## 19. Real-Time Chat Application

### What you will build

A chat application where users can join rooms and exchange messages in
real time through a web interface.

### It must be able to

- Register and authenticate users.
- Create or join chat rooms.
- Send and receive messages without refreshing the page.
- Store message history.
- Show when a user joins or leaves a room.
- Prevent unauthenticated users from reading private rooms.

### You will learn

WebSockets, asynchronous programming, sessions, authentication,
concurrency, and real-time event handling.

### Improve it later

Add typing indicators, file sharing, message search, notifications, and
message delivery status.

---

## 20. Multi-Tenant SaaS API

### What you will build

A subscription-style web application where multiple organizations use the
same system while each organization can see only its own data.

### It must be able to

- Register an organization and its users.
- Keep organization data separate.
- Support owner, admin, and regular-user roles.
- Allow users to create and manage organization records.
- Reject requests for data belonging to another organization.
- Record important account and permission changes.

### You will learn

Tenant isolation, role-based access control, authentication, database
design, audit logs, and security-focused API development.

### Improve it later

Add subscription plans, usage limits, invitations, billing integration,
background jobs, and organization-level analytics.

---

# Advanced Project Quality Checklist

Before calling an advanced project complete:

- [ ] The architecture is explained in the README.
- [ ] Database changes can be reproduced with migrations.
- [ ] Authentication and authorization rules are tested.
- [ ] Failure paths and retry behavior are tested.
- [ ] Logs do not contain passwords, tokens, or private user data.
- [ ] Long-running work can be monitored and stopped safely.
- [ ] Configuration and secrets are outside the source code.
- [ ] Performance has been measured for the important operations.
- [ ] The project has a documented deployment or production-like setup.

---

# Recommended Build Order

1. Simple Calculator
2. Unit Converter
3. Quiz Game
4. Number Guessing Game
5. Expense Tracker
6. Contact Book
7. Library Management System
8. Student Management System
9. File Organizer
10. Notes Application
11. Weather API Client
12. Log File Analyzer
13. To-Do REST API
14. Blog REST API
15. Background Job Queue
16. Web Scraper and Monitor
17. E-commerce Backend
18. Data Processing Pipeline
19. Real-Time Chat Application
20. Multi-Tenant SaaS API

Projects 1–4 build your fundamentals. Projects 5–10 teach file handling,
data modeling, and object-oriented programming. Projects 11–14 introduce
external APIs and backend development. Project 15 teaches reliability and
background processing. Projects 16–20 are advanced portfolio projects that
combine multiple Python skills and production-style design.

# Definition of Done

A project is finished when:

- Another person can run it by following the README.
- The main user flow works from start to finish.
- Invalid input produces a clear error.
- Important logic is covered by tests.
- Secrets are stored outside the code.
- The code is formatted and organized into understandable files.
- You have written down one limitation and one future improvement.