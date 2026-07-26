# Python Notes – Day 6
## Tuples, Sets, and Dictionary Basics

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Create and use tuples.
- Create and use sets and perform set operations.
- Understand the basics of dictionaries.
- Choose the right collection type for a task.

---

# Tuples

A tuple is an **ordered, immutable** collection.

```python
coords = (10, 20)
person = ("Raj", 20, "Delhi")
single = (42,)   # single-element tuple — trailing comma required
```

---

## Accessing Tuple Elements

```python
person = ("Raj", 20, "Delhi")
print(person[0])    # Raj
print(person[-1])   # Delhi
```

---

## Tuple Slicing

```python
nums = (10, 20, 30, 40, 50)
print(nums[1:4])    # (20, 30, 40)
```

---

## Tuple is Immutable

```python
person = ("Raj", 20)
person[0] = "Sam"   # TypeError
```

---

## Tuple Methods

| Method | Description |
|--------|-------------|
| `count(x)` | Count occurrences of x |
| `index(x)` | Return first index of x |

```python
t = (1, 2, 3, 2, 2)
print(t.count(2))   # 3
print(t.index(3))   # 2
```

---

## Tuple Unpacking

```python
name, age, city = ("Raj", 20, "Delhi")
print(name)   # Raj
```

---

## When to Use Tuples

- Data that must not change (coordinates, RGB values, records).
- Tuples are **faster** than lists.
- Can be used as dictionary keys.

---

# Sets

A set is an **unordered, mutable** collection of **unique** elements.

```python
fruits = {"apple", "banana", "cherry"}
s = set([1, 2, 2, 3])   # duplicates removed → {1, 2, 3}
s = set()               # empty set (NOT {})
```

---

## Set Methods

| Method | Description |
|--------|-------------|
| `add(x)` | Add element x |
| `remove(x)` | Remove x (error if absent) |
| `discard(x)` | Remove x (no error if absent) |
| `clear()` | Remove all elements |
| `copy()` | Return a copy |

```python
s = {1, 2, 3}
s.add(4)
s.discard(99)   # no error
```

---

## Set Operations

| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `\|` | `union()` |
| Intersection | `&` | `intersection()` |
| Difference | `-` | `difference()` |
| Symmetric Diff | `^` | `symmetric_difference()` |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}
print(a & b)   # {3, 4}
print(a - b)   # {1, 2}
print(a ^ b)   # {1, 2, 5, 6}
```

---

## Subset and Superset

```python
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))    # True
print(b.issuperset(a))  # True
```

---

# Dictionary Basics

A dictionary stores data as **key-value pairs**.

```python
student = {
    "name": "Raj",
    "age": 20,
    "city": "Delhi"
}
```

---

## Creating a Dictionary

```python
empty = {}
person = {"name": "Raj", "age": 20}
scores = dict(math=90, science=85)
```

---

## Accessing Values

```python
student = {"name": "Raj", "age": 20}
print(student["name"])              # Raj
print(student.get("age"))           # 20
print(student.get("grade", "N/A")) # N/A (default)
```

---

## Adding and Updating

```python
student["grade"] = "A"        # add new key
student["age"] = 21           # update existing key
```

---

## Deleting Items

```python
del student["city"]
popped = student.pop("age")
```

---

## Iterating a Dictionary

```python
for key, value in student.items():
    print(f"{key}: {value}")
```

---

## Checking Keys

```python
print("name" in student)       # True
print("grade" not in student)  # True
```

---

# Comparison: List vs Tuple vs Set vs Dict

| Feature | List | Tuple | Set | Dict |
|---------|------|-------|-----|------|
| Ordered | ✅ | ✅ | ❌ | ✅ (3.7+) |
| Mutable | ✅ | ❌ | ✅ | ✅ |
| Duplicates | ✅ | ✅ | ❌ | Keys: ❌ |
| Key-Value | ❌ | ❌ | ❌ | ✅ |

---

# Common Mistakes

## Empty Set vs Empty Dict

```python
s = {}      # This is a dict!
s = set()   # Correct empty set
```

---

## Modifying a Tuple

```python
t = (1, 2, 3)
t[0] = 99   # TypeError
```

---

# Practice Questions

## Basic

1. Create a tuple of 5 cities and print each.
2. Unpack a tuple into separate variables.
3. Count how many times a value appears in a tuple.
4. Create a set and add/remove elements.
5. Remove duplicates from a list using a set.
6. Find union and intersection of two sets.
7. Create a dictionary for a student and print all keys and values.
8. Add and update keys in a dictionary.
9. Check if a key exists in a dictionary.
10. Delete a key from a dictionary.

---

## Intermediate

11. Find common elements between two lists using sets.
12. Find unique words in a sentence using a set.
13. Count word frequency in a sentence using a dictionary.
14. Create a dictionary from two lists using `zip()`.
15. Find the key with the maximum value in a dictionary.

---

# Mini Project – Contact Book

```python
contacts = {}

while True:
    print("\n1. Add Contact\n2. Search\n3. Delete\n4. Show All\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact '{name}' added.")

    elif choice == "2":
        name = input("Search name: ")
        if name in contacts:
            info = contacts[name]
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
        else:
            print("Contact not found.")

    elif choice == "3":
        name = input("Delete name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    elif choice == "4":
        if contacts:
            for name, info in contacts.items():
                print(f"{name} | {info['phone']} | {info['email']}")
        else:
            print("No contacts saved.")

    elif choice == "5":
        print("Goodbye!")
        break
```

---

# Day 6 Summary

After completing Day 6, you should be able to:

- Create and use tuples (ordered, immutable).
- Create and use sets (unordered, unique elements).
- Perform union, intersection, difference on sets.
- Create and access dictionaries using key-value pairs.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 45 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **2.5–3 hours**
