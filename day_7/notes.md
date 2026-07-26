# Python Notes – Day 7
## Dictionary Methods, Nested Dictionaries, and Revision

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Use all important dictionary methods.
- Work with nested dictionaries.
- Apply dictionary comprehensions.
- Revise Week 1 concepts and build a complete mini project.

---

# Dictionary Methods (Full Reference)

| Method | Description |
|--------|-------------|
| `keys()` | Return all keys |
| `values()` | Return all values |
| `items()` | Return all key-value pairs |
| `get(key, default)` | Return value or default |
| `update(dict)` | Merge another dict |
| `pop(key)` | Remove and return value |
| `popitem()` | Remove and return last pair |
| `setdefault(key, val)` | Set key if not present |
| `clear()` | Remove all items |
| `copy()` | Shallow copy |

---

### Examples

```python
student = {"name": "Raj", "age": 20, "city": "Delhi"}

# keys, values, items
print(list(student.keys()))    # ['name', 'age', 'city']
print(list(student.values()))  # ['Raj', 20, 'Delhi']
print(list(student.items()))   # [('name','Raj'), ('age',20), ('city','Delhi')]

# update
student.update({"grade": "A", "age": 21})
print(student)

# setdefault
student.setdefault("score", 95)  # adds only if not present

# popitem
last = student.popitem()
print(last)
```

---

# Iterating a Dictionary

```python
student = {"name": "Raj", "age": 20, "city": "Delhi"}

for key in student:
    print(key, "->", student[key])

for key, value in student.items():
    print(f"{key}: {value}")
```

---

# Sorting a Dictionary

## By Key

```python
d = {"b": 2, "a": 1, "c": 3}
sorted_by_key = dict(sorted(d.items()))
print(sorted_by_key)   # {'a': 1, 'b': 2, 'c': 3}
```

## By Value

```python
sorted_by_value = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_by_value)   # {'a': 1, 'b': 2, 'c': 3}
```

---

# Nested Dictionaries

A dictionary where values are also dictionaries.

```python
school = {
    "student1": {"name": "Raj", "age": 20, "marks": 85},
    "student2": {"name": "Priya", "age": 22, "marks": 92}
}

print(school["student1"]["name"])    # Raj
print(school["student2"]["marks"])   # 92
```

---

## Iterating Nested Dictionaries

```python
for student_id, info in school.items():
    print(f"\n{student_id}")
    for key, value in info.items():
        print(f"  {key}: {value}")
```

---

## Adding to Nested Dict

```python
school["student3"] = {"name": "Sam", "age": 21, "marks": 78}
```

---

# Dictionary Comprehension

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### With Condition

```python
even_sq = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_sq)
```

---

# `len()` and `in`

```python
d = {"a": 1, "b": 2, "c": 3}
print(len(d))        # 3
print("a" in d)      # True
print(4 in d.values())  # False
```

---

# Merging Dictionaries

## Using `update()`

```python
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d1.update(d2)
print(d1)
```

## Using `**` Unpacking (Python 3.5+)

```python
merged = {**d1, **d2}
print(merged)
```

---

# Week 1 Revision

| Day | Topics |
|-----|--------|
| Day 1 | Variables, Data Types, Input/Output |
| Day 2 | Operators, Type Casting, if/elif/else |
| Day 3 | Loops: for, while, break, continue |
| Day 4 | Functions, Parameters, Return, Scope |
| Day 5 | Lists, List Methods |
| Day 6 | Tuples, Sets, Dictionary Basics |
| Day 7 | Dictionary Methods, Nested Dicts |

---

# Practice Questions

## Basic

1. Print all keys, values, and items of a dictionary.
2. Use `setdefault()` to add a key only if it is missing.
3. Sort a dictionary by value in descending order.
4. Merge two dictionaries.
5. Invert a dictionary (swap keys and values).
6. Find the key with the highest value.
7. Count word frequency in a sentence.
8. Create a nested dictionary for 3 students.
9. Access and update a value inside a nested dictionary.
10. Delete a key from a nested dictionary.

---

## Intermediate

11. Group words by their length using a dictionary.
12. Find keys common to two dictionaries.
13. Create a dictionary from a list of tuples.
14. Build a frequency counter without using `collections`.
15. Convert a nested list into a dictionary.

---

# Mini Project – Student Management System

```python
students = {}

def add_student():
    roll = input("Roll Number: ")
    name = input("Name: ")
    age = int(input("Age: "))
    marks = float(input("Marks: "))
    students[roll] = {"name": name, "age": age, "marks": marks}
    print(f"Student '{name}' added.")

def view_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        s = students[roll]
        print(f"\nRoll: {roll}")
        for k, v in s.items():
            print(f"  {k}: {v}")
    else:
        print("Student not found.")

def update_marks():
    roll = input("Enter Roll Number: ")
    if roll in students:
        marks = float(input("New Marks: "))
        students[roll]["marks"] = marks
        print("Marks updated.")
    else:
        print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        del students[roll]
        print("Student deleted.")
    else:
        print("Student not found.")

def show_all():
    if not students:
        print("No students found.")
    else:
        print(f"\n{'Roll':<10} {'Name':<15} {'Age':<5} {'Marks'}")
        print("-" * 40)
        for roll, s in students.items():
            print(f"{roll:<10} {s['name']:<15} {s['age']:<5} {s['marks']}")

while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Marks")
    print("4. Delete Student")
    print("5. Show All Students")
    print("6. Exit")
    choice = input("Choice: ")

    if choice == "1":   add_student()
    elif choice == "2": view_student()
    elif choice == "3": update_marks()
    elif choice == "4": delete_student()
    elif choice == "5": show_all()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")
```

---

# Day 7 Summary

After completing Day 7, you should be able to:

- Use all dictionary methods confidently.
- Work with and iterate nested dictionaries.
- Sort dictionaries by key or value.
- Use dictionary comprehensions.
- Apply Week 1 knowledge in a complete program.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Revision | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 45 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
