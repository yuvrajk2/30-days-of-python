# Beginner Python Learning Plan

Welcome! This plan is for someone who is starting Python from the
beginning. Follow the steps in order and do not worry about understanding
everything immediately. Programming becomes easier through small,
consistent practice.

This plan combines:

- The 30-day Python learning roadmap.
- The daily notes in `day_1/` through `day_30/`.
- The weekly projects from the roadmap.
- The larger project path in `projects.md`.

---

# 1. What You Need Before Starting

You do not need previous programming experience. You only need:

- A computer.
- The ability to create folders and files.
- A willingness to practice every day.
- About 3 hours per study day, or smaller sessions if needed.

The examples in this repository use **Python 3.12**. The lessons do not
require extra packages at the beginning.

## How to Run a Lesson Script

Open a terminal in the project folder and run a Python file like this:

```bash
python day_1/Day1.py
```

The scripts ask questions in the terminal. Type an answer and press Enter.
If your system uses `python3` instead of `python`, use:

```bash
python3 day_1/Day1.py
```

The main learning material is in Markdown files:

```text
day_1/notes.md
day_2/notes.md
...
day_30/notes.md
```

Read the notes before attempting the mini-project.

---

# 2. Your Daily Study Routine

Use this routine on every study day:

| Activity | Suggested time | What to do |
|----------|----------------|------------|
| Read the notes | 30 minutes | Read the day's `notes.md` carefully |
| Copy and run examples | 45–60 minutes | Type examples yourself instead of only reading |
| Solve exercises | 45–60 minutes | Complete basic questions first |
| Build the mini-project | 45–60 minutes | Create your own version |
| Review | 10 minutes | Write down what was difficult |

The full routine takes about **3–4 hours**. If that is too long, split it
into two sessions:

1. Read and practice examples.
2. Solve exercises and build the project.

## Important Beginner Rule

Do not copy a complete solution and consider the project finished. First
try to write the solution yourself. When you are stuck:

1. Read the relevant section again.
2. Break the problem into smaller steps.
3. Write pseudocode in plain English.
4. Test one small part at a time.
5. Then compare your work with the example.

---

# 3. The 30-Day Learning Plan

Each day has a topic, a mini-project, and a folder containing the notes.
Complete the project even if your first version is simple.

## Week 1 – Python Fundamentals

### Day 1 – Start with Python

- **Learn:** Installation, VS Code, syntax, variables, data types, input,
  and output.
- **Read:** `day_1/notes.md`
- **Build:** Simple Calculator.
- **Goal:** Ask for two numbers and print their sum, difference, product,
  division, and exponentiation.

### Day 2 – Operators and Decisions

- **Learn:** Arithmetic, comparison, logical, assignment, identity, and
  membership operators; type casting; `if`, `elif`, and `else`.
- **Read:** `day_2/notes.md`
- **Build:** Grade Calculator.
- **Goal:** Accept marks from 0 to 100 and display the correct grade.

### Day 3 – Loops

- **Learn:** `for`, `while`, nested loops, `range()`, `break`,
  `continue`, and `pass`.
- **Read:** `day_3/notes.md`
- **Build:** Multiplication Table Generator.
- **Goal:** Ask for a number and print its table using a loop.

### Day 4 – Functions

- **Learn:** Functions, parameters, return values, scope, default
  arguments, `*args`, `**kwargs`, and built-in functions.
- **Read:** `day_4/notes.md`
- **Build:** Unit Converter.
- **Goal:** Put each conversion in a function and let the user choose one.

### Day 5 – Lists

- **Learn:** Creating lists, indexing, slicing, list methods, and list
  operations.
- **Read:** `day_5/notes.md`
- **Build:** Student Marks Manager.
- **Goal:** Store marks, calculate an average, and display the highest mark.

### Day 6 – Python Collections

- **Learn:** Tuples, sets, and dictionary basics.
- **Read:** `day_6/notes.md`
- **Build:** Contact Book.
- **Goal:** Store contacts and search for a contact by name.

### Day 7 – Dictionaries and Review

- **Learn:** Dictionary methods, nested dictionaries, and revision of
  Week 1.
- **Read:** `day_7/notes.md`
- **Build:** Student Management System.
- **Goal:** Add, view, search, update, and remove student records.

### Week 1 Checkpoint

Before starting Week 2, you should be able to:

- Create variables and use common data types.
- Read input and convert it to a number.
- Write conditions and loops.
- Create and call functions.
- Use lists and dictionaries.
- Build a small menu-driven program.

**Weekly project:** Finish a basic Student Management System.

If you are not comfortable yet, repeat Days 2–7. Repetition is normal.

---

## Week 2 – Intermediate Python

### Day 8 – Modules

- **Learn:** `math`, `random`, `datetime`, `os`, imports, and modules.
- **Read:** `day_8/notes.md`
- **Build:** Random Password Generator.
- **Goal:** Generate passwords with a chosen length and character types.

### Day 9 – Exception Handling

- **Learn:** `try`, `except`, `else`, `finally`, and `raise`.
- **Read:** `day_9/notes.md`
- **Build:** ATM Simulation.
- **Goal:** Support balance checks, deposits, withdrawals, and invalid
  input without crashing.

### Day 10 – Files and CSV

- **Learn:** Reading, writing, appending, file paths, and CSV basics.
- **Read:** `day_10/notes.md`
- **Build:** Notes Application.
- **Goal:** Create, view, search, and save notes.

### Day 11 – Object-Oriented Programming Basics

- **Learn:** Classes, objects, constructors, attributes, and methods.
- **Read:** `day_11/notes.md`
- **Build:** Bank Account Class.
- **Goal:** Create an account that supports deposits, withdrawals, and
  balance checks.

### Day 12 – Advanced OOP

- **Learn:** Inheritance, encapsulation, polymorphism, and dunder methods.
- **Read:** `day_12/notes.md`
- **Build:** Employee Management System.
- **Goal:** Represent different employee types and calculate their details.

### Day 13 – Functional Programming

- **Learn:** Lambda functions, `map()`, `filter()`, `reduce()`, and
  iterators.
- **Read:** `day_13/notes.md`
- **Build:** Data Processing Program.
- **Goal:** Transform, filter, sort, and summarize a collection of records.
- **Weekly checkpoint:** Expand the notes' Library Management System
  checkpoint.

### Week 2 Checkpoint

Build a **Library Management System** with:

- A book record containing ID, title, author, and availability.
- Add and list book operations.
- Search by title or author.
- Checkout and return operations.
- A clear message for an unknown book.
- File persistence.

You should now be able to organize a medium-sized program into functions,
classes, and separate data operations.

---

## Week 3 – Advanced Python Techniques

### Day 14 – Comprehensions and Generators

- **Learn:** List comprehensions and generator expressions.
- **Read:** `day_14/notes.md`
- **Build:** Password List Generator.
- **Goal:** Generate and filter password candidates without unnecessary
  repeated code.

### Day 15 – Decorators and Context Managers

- **Learn:** Decorators, `with`, context managers, and resource cleanup.
- **Read:** `day_15/notes.md`
- **Build:** File Logger.
- **Goal:** Record program events safely in a log file.

### Day 16 – Regular Expressions

- **Learn:** Patterns, character classes, groups, anchors, and `re`.
- **Read:** `day_16/notes.md`
- **Build:** Email Validator.
- **Goal:** Check whether email input follows a reasonable format.

### Day 17 – Virtual Environments and Packages

- **Learn:** Virtual environments, `pip`, and package installation.
- **Read:** `day_17/notes.md`
- **Build:** Environment Setup.
- **Goal:** Create an isolated environment and install a package safely.

### Day 18 – Project Structure

- **Learn:** `pyproject.toml`, Poetry concepts, package layout, and
  project organization.
- **Read:** `day_18/notes.md`
- **Build:** Python Project Template.
- **Goal:** Create a clean project with source code, tests, and metadata.

### Day 19 – Types and Validation

- **Learn:** Type hints, `typing`, mypy concepts, and Pydantic basics.
- **Read:** `day_19/notes.md`
- **Build:** User Data Validator.
- **Goal:** Validate user records and report helpful errors.

### Day 20 – Code Quality

- **Learn:** Black, Ruff, imports, formatting, and linting.
- **Read:** `day_20/notes.md`
- **Build:** Format Previous Projects.
- **Goal:** Format and lint one earlier project.
- **Weekly checkpoint:** Begin the Password Manager checkpoint in the notes.

### Week 3 Checkpoint

Build a learning-only **Password Manager prototype** with:

- A service name, username, and password record.
- Secure random password generation using `secrets`.
- Search by service.
- Input validation.
- Local practice storage.

Never use real passwords in this learning project and never commit secrets
to the repository. A real password manager requires encryption and a
careful security review.

---

## Week 4 – Data Structures and Real Projects

### Day 21 – Arrays and Linked Lists

- **Learn:** Array concepts and linked-list implementation.
- **Read:** `day_21/notes.md`
- **Build:** Custom Linked List.
- **Goal:** Add, remove, search, and display nodes.

### Day 22 – Stack, Queue, and Heap

- **Learn:** Stacks, queues, priority queues, and heaps.
- **Read:** `day_22/notes.md`
- **Build:** Stack Calculator.
- **Goal:** Evaluate a postfix expression using a stack.

### Day 23 – Hash Tables

- **Learn:** Hashing, dictionaries, sets, collisions, and lookup cost.
- **Read:** `day_23/notes.md`
- **Build:** Word Frequency Counter.
- **Goal:** Count and rank the words in a text.

### Day 24 – Recursion

- **Learn:** Base cases, recursive cases, call stacks, and memoization.
- **Read:** `day_24/notes.md`
- **Build:** Recursive Calculator Collection.
- **Goal:** Implement recursive factorial, Fibonacci, power, GCD, and
  palindrome checks.

### Day 25 – Binary Search Trees

- **Learn:** Tree nodes, insertion, search, deletion, and traversals.
- **Read:** `day_25/notes.md`
- **Build:** BST Implementation.
- **Goal:** Insert, search, delete, and traverse values in a binary search
  tree.

### Day 26 – Sorting Algorithms

- **Learn:** Bubble, selection, insertion, merge, and quick sort.
- **Read:** `day_26/notes.md`
- **Build:** Sorting Visualizer for the console.
- **Goal:** Compare sorting algorithms and count their operations.

### Day 27 – Searching Algorithms

- **Learn:** Linear search, binary search, and algorithm analysis.
- **Read:** `day_27/notes.md`
- **Build:** Search Utility.
- **Goal:** Search values, report the index, and compare operations.

### Day 28 – Testing

- **Learn:** `unittest`, `pytest`, assertions, fixtures, and edge cases.
- **Read:** `day_28/notes.md`
- **Build:** Test Your Calculator.
- **Goal:** Write tests for calculator success cases and division by zero.

### Day 29 – Documentation and APIs

- **Learn:** Docstrings, Sphinx concepts, Flask, FastAPI, routes, JSON,
  and HTTP status codes.
- **Read:** `day_29/notes.md`
- **Build:** Simple REST API.
- **Goal:** Create endpoints that list and create items with validation.

### Day 30 – Revision and Capstone

- **Learn:** How to plan, build, test, and document a complete application.
- **Read:** `day_30/notes.md`
- **Build:** Complete Python Application.
- **Goal:** Choose a capstone, define its minimum features, and build the
  first working version.

### Week 4 Checkpoint

Choose one capstone:

- Expense Tracker.
- Advanced Student Management System.
- Library Management System.
- Password Manager prototype.
- Contact Book.
- To-Do API.
- Weather API Client.
- File Organizer.

Your capstone should have a clear purpose, at least three useful features,
input validation, tests, documentation, and a way to save data when needed.

---

# 4. What to Do After Day 30

The 30-day roadmap gives you the foundation. Do not immediately start all
20 projects. Choose one project at a time from `projects.md`.

## Stage 1 – Beginner Projects

Start with these projects:

1. Simple Calculator.
2. Unit Converter.
3. Quiz Game.
4. Number Guessing Game.
5. Expense Tracker.
6. Contact Book.
7. Library Management System.
8. Student Management System.
9. File Organizer.
10. Notes Application.

At this stage, focus on writing readable Python, using functions, handling
errors, and saving data.

## Stage 2 – Intermediate Projects

After completing several beginner projects, build:

11. Weather API Client.
12. Log File Analyzer.
13. To-Do REST API.
14. Blog REST API.
15. Background Job Queue.

At this stage, focus on APIs, databases, external services, tests, and
project structure.

## Stage 3 – Advanced Projects

When you are comfortable with the intermediate projects, try:

16. Web Scraper and Monitor.
17. E-commerce Backend.
18. Data Processing Pipeline.
19. Real-Time Chat Application.
20. Multi-Tenant SaaS API.

At this stage, focus on architecture, concurrency, security, performance,
reliability, and deployment.

Read `projects.md` for the exact features and improvement ideas for every
project.

---

# 5. Beginner Progress Checklist

## After Week 1

- [ ] I can write variables and use common data types.
- [ ] I can accept user input.
- [ ] I can use `if`, `elif`, and `else`.
- [ ] I can write `for` and `while` loops.
- [ ] I can write and call functions.
- [ ] I can use lists and dictionaries.

## After Week 2

- [ ] I can import and use modules.
- [ ] I can handle expected errors.
- [ ] I can read and write files.
- [ ] I can create simple classes.
- [ ] I can organize a program into smaller functions.

## After Week 3

- [ ] I understand comprehensions and generators.
- [ ] I can write a basic decorator.
- [ ] I can use regular expressions for simple validation.
- [ ] I can create a virtual environment.
- [ ] I understand type hints and validation.
- [ ] I can format and lint my code.

## After Week 4

- [ ] I understand common data structures.
- [ ] I can explain basic algorithm complexity.
- [ ] I can implement simple sorting and searching.
- [ ] I can write automated tests.
- [ ] I can document a Python project.
- [ ] I can create a basic REST API.

---

# 6. Rules for Finishing Projects

Do not call a project finished just because the code runs once. A finished
project should:

- Have a clear README.
- Have a simple setup and run command.
- Separate user-interface code from core logic.
- Handle invalid input clearly.
- Save data correctly when persistence is required.
- Include tests for important behavior.
- Use formatting consistently.
- Keep passwords, API keys, and tokens out of the code.
- Explain one limitation and one future improvement.

If a project feels too difficult, reduce its scope. A small finished
project is more valuable than a large unfinished one.

---

# 7. When You Are Stuck

Being stuck is part of learning. Use this process:

1. Read the error message from the bottom upward.
2. Identify the file and line number.
3. Print the values involved.
4. Test the smallest piece of code separately.
5. Search the day's notes for the concept.
6. Write a smaller example.
7. Ask for help with the exact error and what you already tried.

Keep a short learning journal. For each difficult problem, record:

- What I expected.
- What actually happened.
- Why it happened.
- What fixed it.

This journal will become one of your most useful learning tools.