# Python Notes – Day 7
## Dictionaries

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Create and access dictionaries.
- Add, update, and delete key-value pairs.
- Use dictionary methods.
- Iterate over dictionaries.
- Work with nested dictionaries.

---

# What is a Dictionary?

A dictionary stores data as **key-value pairs**.

- Keys are unique.
- Values can be any data type.
- Dictionaries are **ordered** (Python 3.7+) and **mutable**.

```python
student = {
    "name": "Raj",
    "age": 20,
    "city": "Delhi"
}
```

---

# Creating a Dictionary

```python
empty = {}
empty = dict()

person = {"name": "Raj", "age": 20}
scores = dict(math=90, science=85)
```

---

# Accessing Values

```python
student = {"name": "Raj", "age": 20}

print(student["name"])       # Raj
print(student.get("age"))    # 20
print(student.get("grade", "N/A"))  # N/A (default if key missing)
```

---

# Adding and Updating

```python
student = {"name": "Raj"}

student["age"] = 20          # add new key
student["name"] = "Rahul"   # update existing key
print(student)
```

**Output**

```
{'name': 'Rahul', 'age': 20}
```

---

# Deleting Items

```python
student = {"name": "Raj", "age": 20, "city": "Delhi"}

del student["city"]
print(student)

popped = student.pop("age")
print(popped)    # 20
print(student)
```

---

# Dictionary Methods

| Method | Description |
|--------|-------------|
| `keys()` | Return all keys |
| `values()` | Return all values |
| `items()` | Return all key-value pairs |
| `get(key, default)` | Return value or default |
| `update(dict)` | Merge another dict in |
| `pop(key)` | Remove and return value |
| `clear()` | Remove all items |
| `copy()` | Shallow copy |
| `setdefault(key, val)` | Set key if not present |

---

### Examples

```python
student = {"name": "Raj", "age": 20, "city": "Delhi"}

print(student.keys())    # dict_keys(['name', 'age', 'city'])
print(student.values())  # dict_values(['Raj', 20, 'Delhi'])
print(student.items())   # dict_items([...])

student.update({"grade": "A", "age": 21})
print(student)
```

---

# Iterating a Dictionary

```python
student = {"name": "Raj", "age": 20, "city": "Delhi"}

for key in student:
    print(key, ":", student[key])
```

---

```python
for key, value in student.items():
    print(f"{key} = {value}")
```

---

# Checking Keys

```python
student = {"name": "Raj", "age": 20}

print("name" in student)     # True
print("grade" not in student)  # True
```

---

# Nested Dictionaries

```python
school = {
    "student1": {"name": "Raj", "age": 20},
    "student2": {"name": "Priya", "age": 22}
}

print(school["student1"]["name"])   # Raj
```

---

# Dictionary Comprehension

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)
```

**Output**

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

# `len()` and `sorted()`

```python
d = {"b": 2, "a": 1, "c": 3}
print(len(d))          # 3
print(sorted(d))       # ['a', 'b', 'c']
```

---

# Common Mistakes

## KeyError

```python
student = {"name": "Raj"}
print(student["age"])   # KeyError
```

Fix: use `.get()`.

---

## Using Mutable Key

```python
d = {[1, 2]: "list"}   # TypeError — list is not hashable
```

Fix: use a tuple — `{(1, 2): "tuple"}`.

---

# Practice Questions

## Basic

1. Create a dictionary for a student with name, age, and marks.
2. Add and update a key in the dictionary.
3. Delete a key using `del` and `pop()`.
4. Iterate and print all keys and values.
5. Check if a key exists.
6. Merge two dictionaries.
7. Count word frequency in a sentence using a dictionary.
8. Create a dictionary from two lists using `zip()`.
9. Sort a dictionary by value.
10. Find the key with the maximum value.

---

## Intermediate

11. Invert a dictionary (swap keys and values).
12. Group a list of words by their first letter.
13. Count the frequency of characters in a string.
14. Find common keys in two dictionaries.
15. Create a nested dictionary for a class with students.

---

# Mini Project – Phone Book

```python
phone_book = {}

while True:
    print("\n1. Add Contact\n2. Search Contact\n3. Delete Contact\n4. Show All\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        number = input("Number: ")
        phone_book[name] = number
        print("Contact added.")
    elif choice == "2":
        name = input("Search name: ")
        print(phone_book.get(name, "Contact not found."))
    elif choice == "3":
        name = input("Delete name: ")
        if name in phone_book:
            del phone_book[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "4":
        for name, number in phone_book.items():
            print(f"{name}: {number}")
    elif choice == "5":
        break
```

---

# Day 7 Summary

After completing Day 7, you should be able to:

- Create and manipulate dictionaries.
- Use `.keys()`, `.values()`, `.items()`, `.get()`, `.update()`.
- Iterate over dictionaries.
- Work with nested dictionaries.
- Use dictionary comprehensions.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
