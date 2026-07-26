# Python Notes – Day 6
## Tuples and Sets

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Create and use tuples.
- Understand why tuples are immutable.
- Create and use sets.
- Perform set operations (union, intersection, difference).
- Choose between lists, tuples, and sets.

---

# Tuples

A tuple is an **ordered, immutable** collection.

```python
coords = (10, 20)
person = ("Raj", 20, "Delhi")
single = (42,)   # single-element tuple needs a trailing comma
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

- When data should not change (coordinates, RGB values, database records).
- Tuples are **faster** than lists.
- Can be used as dictionary keys.

---

# Sets

A set is an **unordered, mutable** collection of **unique** elements.

```python
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
```

---

## Creating a Set

```python
s = set()           # empty set (NOT {}, that's a dict)
s = {1, 2, 3}
s = set([1, 2, 2, 3])   # duplicates removed
print(s)   # {1, 2, 3}
```

---

## Set is Unordered

Elements have no guaranteed order — you cannot index a set.

```python
s = {3, 1, 2}
print(s)   # {1, 2, 3} or any order
```

---

## Set Methods

| Method | Description |
|--------|-------------|
| `add(x)` | Add element x |
| `remove(x)` | Remove x (error if absent) |
| `discard(x)` | Remove x (no error if absent) |
| `pop()` | Remove a random element |
| `clear()` | Remove all elements |
| `copy()` | Return a copy |

```python
s = {1, 2, 3}
s.add(4)
print(s)   # {1, 2, 3, 4}

s.remove(2)
print(s)   # {1, 3, 4}

s.discard(99)  # no error
```

---

## Set Operations

| Operation | Operator | Method |
|-----------|----------|--------|
| Union | `\|` | `union()` |
| Intersection | `&` | `intersection()` |
| Difference | `-` | `difference()` |
| Symmetric Difference | `^` | `symmetric_difference()` |

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1, 2, 3, 4, 5, 6}
print(a & b)   # {3, 4}
print(a - b)   # {1, 2}
print(a ^ b)   # {1, 2, 5, 6}
```

---

## Set Membership

```python
s = {1, 2, 3}
print(2 in s)    # True
print(5 not in s)  # True
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

## Frozen Set

An immutable set — can be used as a dictionary key.

```python
fs = frozenset({1, 2, 3})
```

---

# Comparison: List vs Tuple vs Set

| Feature | List | Tuple | Set |
|---------|------|-------|-----|
| Ordered | ✅ | ✅ | ❌ |
| Mutable | ✅ | ❌ | ✅ |
| Duplicates | ✅ | ✅ | ❌ |
| Indexing | ✅ | ✅ | ❌ |

---

# Common Mistakes

## Empty Set

```python
s = {}   # This is a dict, NOT a set!
s = set()  # Correct empty set
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
2. Access the second element of a tuple.
3. Count how many times a value appears in a tuple.
4. Create a set and add/remove elements.
5. Remove duplicates from a list using a set.
6. Find the union of two sets.
7. Find the intersection of two sets.
8. Check if one set is a subset of another.
9. Create a frozenset.
10. Convert a list to a set and back to a list.

---

## Intermediate

11. Find common elements between two lists using sets.
12. Find unique words in a sentence.
13. Find elements in list A but not in list B.
14. Unpack a tuple into variables.
15. Return multiple values from a function as a tuple.

---

# Mini Project – Unique Visitor Counter

```python
visitors = set()

while True:
    name = input("Enter visitor name (or 'quit' to stop): ")
    if name.lower() == "quit":
        break
    if name in visitors:
        print(f"{name} has visited before.")
    else:
        visitors.add(name)
        print(f"Welcome, {name}!")

print(f"\nTotal unique visitors: {len(visitors)}")
print("Visitors:", visitors)
```

---

# Day 6 Summary

After completing Day 6, you should be able to:

- Create and use tuples (ordered, immutable).
- Create and use sets (unordered, unique elements).
- Perform union, intersection, difference, and symmetric difference.
- Choose the right data structure for the task.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 45 minutes |
| Practice Problems | 45 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **2.5 hours**
