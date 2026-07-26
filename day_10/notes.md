# Python Notes – Day 10
## File Handling – Read, Write, Append, and CSV Basics

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Open, read, write, and append to text files.
- Use the `with` statement for safe file handling.
- Work with file paths and modes.
- Read and write CSV files using the `csv` module.

---

# Why File Handling?

Programs often need to **persist data** between runs — save settings, store records, log events. Files make this possible without a database.

---

# Opening a File

```python
f = open("filename.txt", mode)
```

| Mode | Description |
|------|-------------|
| `"r"` | Read (default) — file must exist |
| `"w"` | Write — creates or overwrites |
| `"a"` | Append — creates or adds to end |
| `"x"` | Exclusive create — fails if exists |
| `"r+"` | Read and write |
| `"rb"` | Read binary |
| `"wb"` | Write binary |

---

# Writing to a File

```python
f = open("notes.txt", "w")
f.write("Hello, Python!\n")
f.write("This is line 2.\n")
f.close()
```

---

# The `with` Statement (Recommended)

Automatically closes the file even if an error occurs.

```python
with open("notes.txt", "w") as f:
    f.write("Hello, Python!\n")
    f.write("This is line 2.\n")
# file is closed here automatically
```

---

# Reading from a File

## `read()` — Read entire file

```python
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
```

---

## `readline()` — Read one line at a time

```python
with open("notes.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()
```

---

## `readlines()` — Read all lines into a list

```python
with open("notes.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

---

## Looping Directly (Most Efficient)

```python
with open("notes.txt", "r") as f:
    for line in f:
        print(line.strip())
```

---

# Appending to a File

```python
with open("notes.txt", "a") as f:
    f.write("This line is appended.\n")
```

`"a"` mode adds to the end without erasing existing content.

---

# Checking if a File Exists

```python
import os

if os.path.exists("notes.txt"):
    with open("notes.txt", "r") as f:
        print(f.read())
else:
    print("File not found.")
```

---

# `writelines()` — Write a List of Lines

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

---

# File Pointer Methods

| Method | Description |
|--------|-------------|
| `tell()` | Return current position |
| `seek(pos)` | Move to a position |

```python
with open("notes.txt", "r") as f:
    print(f.tell())      # 0
    f.read(5)
    print(f.tell())      # 5
    f.seek(0)            # back to start
```

---

# CSV Basics

CSV (Comma-Separated Values) stores tabular data in plain text.

```
name,age,city
Raj,20,Delhi
Priya,22,Mumbai
```

---

## Writing a CSV

```python
import csv

students = [
    ["name", "age", "marks"],
    ["Raj", 20, 85],
    ["Priya", 22, 92],
    ["Sam", 21, 78]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)
```

---

## Reading a CSV

```python
import csv

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

---

## CSV with DictReader / DictWriter

```python
# Reading as dicts
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["marks"])

# Writing as dicts
fields = ["name", "age", "marks"]
rows = [{"name": "Raj", "age": 20, "marks": 85}]

with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
```

---

# Common Mistakes

## Forgetting `newline=""` in CSV

On Windows, forgetting this adds extra blank lines.

```python
with open("data.csv", "w", newline="") as f:   # always add newline=""
```

---

## Not Closing the File

```python
f = open("file.txt", "w")
f.write("data")
# forgot f.close() — use with instead
```

---

# Practice Questions

## Basic

1. Write "Hello, World!" to a file.
2. Read and print the contents of a file.
3. Append a new line to an existing file.
4. Count the number of lines in a file.
5. Count the number of words in a file.
6. Copy the contents of one file to another.
7. Search for a word in a file and print the line number.
8. Write a list of names to a file (one per line).
9. Read only the first 3 lines of a file.
10. Check if a file exists before reading it.

---

## Intermediate

11. Write student data to a CSV file.
12. Read a CSV file and calculate the average marks.
13. Find the student with the highest marks from a CSV.
14. Append a new student record to an existing CSV.
15. Count word frequency in a text file.

---

# Mini Project – Notes Application

```python
import os

NOTES_FILE = "notes.txt"

def add_note():
    note = input("Write your note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("Note saved.")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes yet.")
        return
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()
    if not lines:
        print("No notes yet.")
    else:
        print("\n--- Your Notes ---")
        for i, line in enumerate(lines, 1):
            print(f"{i}. {line.strip()}")

def delete_note():
    view_notes()
    if not os.path.exists(NOTES_FILE):
        return
    try:
        num = int(input("Note number to delete: "))
        with open(NOTES_FILE, "r") as f:
            lines = f.readlines()
        if 1 <= num <= len(lines):
            lines.pop(num - 1)
            with open(NOTES_FILE, "w") as f:
                f.writelines(lines)
            print("Note deleted.")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_notes():
    confirm = input("Delete all notes? (yes/no): ")
    if confirm.lower() == "yes":
        open(NOTES_FILE, "w").close()
        print("All notes cleared.")

while True:
    print("\n=== Notes App ===")
    print("1. Add Note\n2. View Notes\n3. Delete Note\n4. Clear All\n5. Exit")
    choice = input("Choice: ")

    if choice == "1":   add_note()
    elif choice == "2": view_notes()
    elif choice == "3": delete_note()
    elif choice == "4": clear_notes()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
```

---

# Day 10 Summary

After completing Day 10, you should be able to:

- Open files in read, write, and append mode.
- Use `with` for safe file handling.
- Read files line by line and as a whole.
- Write and read CSV files using the `csv` module.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
