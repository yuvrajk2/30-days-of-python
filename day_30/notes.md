# Python Notes – Day 30
## Final Revision and Capstone Project

---

# Learning Objectives

By the end of this final day, you should be able to:

- Review the complete 30-day Python learning path.
- Choose a project with a clear scope and useful outcome.
- Plan features before writing code.
- Combine Python fundamentals, files, data structures, testing, and APIs.
- Present a maintainable capstone project.

---

# Complete Roadmap Review

## Week 1 – Fundamentals

- Variables, data types, input/output, and operators.
- Conditions, loops, and functions.
- Lists, tuples, sets, and dictionaries.
- Project milestone: a working Student Management System.

## Week 2 – Intermediate Python

- Modules and standard-library tools.
- Exceptions and validation.
- Text and CSV file handling.
- Classes, inheritance, and polymorphism.
- Functional programming tools.
- Project milestone: a working Library Management System.

## Week 3 – Advanced Python

- Comprehensions and generators.
- Decorators and context managers.
- Regular expressions.
- Virtual environments and package installation.
- Type hints, Pydantic basics, and code formatting.
- Project milestone: a working Password Manager design.

## Week 4 – Data Structures and Real Projects

- Arrays, linked lists, stacks, queues, heaps, hash tables, and sets.
- Recursion, binary search trees, sorting, and searching.
- Automated testing.
- Documentation and a first Flask or FastAPI application.
- Project milestone: a tested and documented capstone.

---

# Capstone Planning

Choose one project:

1. Expense Tracker.
2. Advanced Student Management System.
3. Library Management System.
4. Password Manager.
5. Contact Book.
6. To-Do API.
7. Weather API Client.
8. File Organizer.

Choose a project that is small enough to finish but rich enough to show
what you learned.

## Define the Minimum Viable Version

Write down:

- Who will use it?
- What problem does it solve?
- What are the three most important features?
- What data must be stored?
- What invalid input must be rejected?
- How will a user run it?

Do not begin with every possible feature. Finish a small, reliable version
before adding optional improvements.

---

# Suggested Project Structure

```text
capstone/
├── README.md
├── pyproject.toml
├── src/
│   └── capstone/
│       ├── __init__.py
│       ├── models.py
│       ├── services.py
│       └── cli.py
├── tests/
│   ├── test_models.py
│   └── test_services.py
└── data/
    └── .gitkeep
```

For a small learning project, a flat structure is also acceptable. The
important goals are clear responsibilities, repeatable commands, and tests.

---

# Build in Small Milestones

### Milestone 1: Core Data

Create the data model and a few functions that add, list, update, and
remove records. Test these functions before adding a user interface.

### Milestone 2: Persistence

Store data in JSON or CSV. Handle missing files, malformed records, and
empty data safely.

### Milestone 3: User Interface

Add a clear command-line menu or a small Flask/FastAPI API. Validate input
at the boundary and keep business rules in separate functions.

### Milestone 4: Quality

Add type hints, docstrings, formatting, tests, and a useful README.

### Milestone 5: Review

Try normal inputs, empty inputs, invalid inputs, duplicate records, and
large enough inputs to expose slow algorithms.

---

# Example: Expense Tracker Capstone

Minimum features:

- Add an expense with date, category, description, and amount.
- List all expenses.
- Calculate total spending.
- Filter by category or date.
- Save and load records from a CSV file.

Possible data model:

```python
from dataclasses import dataclass
from datetime import date

@dataclass
class Expense:
    amount: float
    category: str
    description: str
    spent_on: date
```

Possible service functions:

```python
def total_expenses(expenses):
    return sum(expense.amount for expense in expenses)

def by_category(expenses, category):
    return [
        expense for expense in expenses
        if expense.category.casefold() == category.casefold()
    ]
```

Write tests for totals, empty lists, category matching, invalid amounts,
and saving/loading records.

---

# Capstone Quality Checklist

## Functionality

- [ ] The main user flow works from a clean checkout.
- [ ] Invalid input produces a helpful message.
- [ ] Data can be saved and loaded when persistence is required.
- [ ] The project has a clear exit path and does not hang unexpectedly.

## Code Quality

- [ ] Functions have focused responsibilities.
- [ ] Names are descriptive and formatting is consistent.
- [ ] Type hints and docstrings cover important public code.
- [ ] No passwords, API keys, or private data are committed.

## Testing

- [ ] Core business rules have automated tests.
- [ ] Normal, boundary, empty, and invalid cases are covered.
- [ ] Tests can be run with one documented command.

## Documentation

- [ ] README explains the project and setup.
- [ ] Example commands or API requests are included.
- [ ] Known limitations and future improvements are listed.

---

# Presentation

When sharing the project, explain:

1. The problem and intended user.
2. The main features.
3. The data model and program flow.
4. One design or algorithm decision.
5. How tests protect the project.
6. What you would improve next.

Being able to explain trade-offs is as important as writing the code.

---

# Final Practice Tasks

1. Choose a capstone and write a one-page plan.
2. Draw the data flow from user input to output.
3. Implement the smallest working feature.
4. Add one test before adding the next feature.
5. Run a formatting and test check.
6. Write setup instructions from the perspective of a new user.
7. Ask someone else to follow the README without extra help.
8. Record three improvements for a future version.

---

# Mini Project – Complete Python Application

Build and present one complete application from the capstone list. It
should include:

- A clear purpose and a documented setup command.
- At least three useful user-facing features.
- Input validation and explicit error handling.
- Persistent data when the project needs it.
- Type hints and docstrings on important code.
- Automated tests for its core behavior.
- A README with examples and limitations.

The project is complete when another person can clone it, follow the
README, run it, use the main flow, and run the tests without guessing.

---

# Day 30 Summary

After completing Day 30, you should be able to:

- Explain the major concepts from the full roadmap.
- Plan and scope a realistic Python application.
- Combine data structures, files, functions, classes, and testing.
- Document and present a finished project.
- Identify the next skill to learn through a real project.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Roadmap revision | 45 minutes |
| Capstone planning | 30 minutes |
| Coding | 90 minutes |
| Testing and documentation | 45 minutes |

**Total:** Approximately **3.5 hours**