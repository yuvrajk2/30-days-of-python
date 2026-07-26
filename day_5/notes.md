# Python Notes – Day 5
## Lists – Creating, Indexing, Slicing, and Methods

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Create and access lists.
- Use indexing and slicing.
- Modify lists using built-in methods.
- Iterate over lists.
- Work with nested lists.

---

# What is a List?

A list is an **ordered, mutable** collection that can hold items of any data type.

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "Raj", 3.14, True]
```

---

# Creating a List

```python
empty = []
nums = [10, 20, 30]
nested = [[1, 2], [3, 4]]
```

---

# Accessing Elements – Indexing

| Index | 0 | 1 | 2 | 3 |
|-------|---|---|---|---|
| Value | 10 | 20 | 30 | 40 |

```python
nums = [10, 20, 30, 40]

print(nums[0])    # 10
print(nums[-1])   # 40 (last element)
```

---

# Slicing

```python
nums = [10, 20, 30, 40, 50]

print(nums[1:4])    # [20, 30, 40]
print(nums[:3])     # [10, 20, 30]
print(nums[2:])     # [30, 40, 50]
print(nums[::2])    # [10, 30, 50]
print(nums[::-1])   # [50, 40, 30, 20, 10]
```

---

# Modifying a List

```python
fruits = ["apple", "banana", "cherry"]
fruits[1] = "mango"
print(fruits)   # ['apple', 'mango', 'cherry']
```

---

# List Methods

| Method | Description |
|--------|-------------|
| `append(x)` | Add x to the end |
| `insert(i, x)` | Insert x at index i |
| `extend(lst)` | Add all items of lst |
| `remove(x)` | Remove first occurrence of x |
| `pop(i)` | Remove and return item at index i |
| `sort()` | Sort the list |
| `reverse()` | Reverse the list |
| `index(x)` | Return first index of x |
| `count(x)` | Count occurrences of x |
| `clear()` | Remove all items |
| `copy()` | Return a shallow copy |

---

### Examples

```python
nums = [3, 1, 4, 1, 5]

nums.append(9)
print(nums)   # [3, 1, 4, 1, 5, 9]

nums.insert(2, 99)
print(nums)   # [3, 1, 99, 4, 1, 5, 9]

nums.remove(1)
print(nums)   # [3, 99, 4, 1, 5, 9]

nums.sort()
print(nums)   # [1, 3, 4, 5, 9, 99]

nums.reverse()
print(nums)   # [99, 9, 5, 4, 3, 1]

print(nums.count(9))   # 1
print(len(nums))       # 6
```

---

# List Built-in Functions

```python
nums = [5, 2, 8, 1, 9]

print(len(nums))    # 5
print(min(nums))    # 1
print(max(nums))    # 9
print(sum(nums))    # 25
print(sorted(nums)) # [1, 2, 5, 8, 9]
```

---

# Iterating a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

---

# List Membership

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)       # True
print("mango" not in fruits)   # True
```

---

# Nested Lists

```python
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])      # [1, 2, 3]
print(matrix[1][2])   # 6
```

---

# List Unpacking

```python
a, b, c = [10, 20, 30]
print(a, b, c)
```

**Output**

```
10 20 30
```

---

# `zip()` with Lists

```python
names = ["Raj", "Priya", "Sam"]
marks = [85, 92, 78]

for name, mark in zip(names, marks):
    print(f"{name}: {mark}")
```

---

# Common Mistakes

## Index Out of Range

```python
nums = [1, 2, 3]
print(nums[5])   # IndexError
```

---

## Modifying While Iterating

```python
nums = [1, 2, 3, 4]
for n in nums:
    nums.remove(n)   # unpredictable behaviour
```

Fix: iterate over a copy — `for n in nums[:]`.

---

# Practice Questions

## Basic

1. Create a list of 5 fruits and print each.
2. Access the first and last element.
3. Reverse a list.
4. Sort a list of numbers.
5. Find the sum and average of a list.
6. Remove duplicates from a list.
7. Check if an element exists in a list.
8. Count occurrences of an element.
9. Merge two lists.
10. Find the second largest element.

---

## Intermediate

11. Find the common elements in two lists.
12. Flatten a nested list.
13. Rotate a list by k positions.
14. Find all pairs in a list that sum to a target.
15. Remove all negative numbers from a list.

---

# Mini Project – Student Marks Manager

```python
students = []
marks = []

n = int(input("How many students? "))
for i in range(n):
    name = input("Enter student name: ")
    mark = float(input(f"Enter marks for {name}: "))
    students.append(name)
    marks.append(mark)

highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)

print(f"\nHighest marks: {highest}")
print(f"Lowest marks:  {lowest}")
print(f"Average marks: {average:.2f}")

top_index = marks.index(highest)
print(f"Top student:   {students[top_index]}")
```

---

# Day 5 Summary

After completing Day 5, you should be able to:

- Create and access lists using indexing and slicing.
- Modify lists using built-in methods.
- Use `len()`, `min()`, `max()`, `sum()`, `sorted()`.
- Iterate lists and work with nested lists.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
