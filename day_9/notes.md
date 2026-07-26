# Python Notes – Day 9
## List Comprehensions and Dictionary Comprehensions

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Write list comprehensions as a concise alternative to loops.
- Add conditions to comprehensions.
- Write nested list comprehensions.
- Write dictionary and set comprehensions.

---

# What is a List Comprehension?

A list comprehension creates a new list in a single, readable line.

### Without Comprehension

```python
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
print(squares)
```

### With Comprehension

```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)
```

**Output**

```
[1, 4, 9, 16, 25]
```

---

# Syntax

```python
[expression for item in iterable]
```

---

# With a Condition (Filtering)

```python
[expression for item in iterable if condition]
```

### Example – Even Numbers Only

```python
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)   # [2, 4, 6, 8, 10]
```

---

### Example – Filter Positive Numbers

```python
nums = [-3, -1, 0, 2, 5, -7, 8]
positives = [n for n in nums if n > 0]
print(positives)   # [2, 5, 8]
```

---

# With `if-else` (Transformation)

```python
[expr_true if condition else expr_false for item in iterable]
```

```python
result = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]
print(result)   # ['odd', 'even', 'odd', 'even', 'odd']
```

---

# String Operations in Comprehensions

```python
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
print(upper)   # ['HELLO', 'WORLD', 'PYTHON']
```

---

# Nested List Comprehension

```python
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)
```

**Output**

```
[[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

---

# Flatten a Nested List

```python
nested = [[1, 2], [3, 4], [5, 6]]
flat = [x for row in nested for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6]
```

---

# Dictionary Comprehension

```python
{key_expr: value_expr for item in iterable}
```

### Example

```python
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

---

### With Condition

```python
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(even_squares)   # {2: 4, 4: 16, 6: 36, 8: 64, 10: 100}
```

---

### Swapping Keys and Values

```python
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}
print(inverted)   # {1: 'a', 2: 'b', 3: 'c'}
```

---

# Set Comprehension

```python
unique_squares = {x**2 for x in [-2, -1, 0, 1, 2]}
print(unique_squares)   # {0, 1, 4}
```

---

# Generator Expression

Similar to a list comprehension but uses `()` and is **lazy** (does not build the whole list in memory).

```python
gen = (x**2 for x in range(1, 6))
print(next(gen))   # 1
print(next(gen))   # 4
print(list(gen))   # [9, 16, 25]
```

Use generators when working with large datasets.

---

# When to Use Comprehensions

| Use | When |
|-----|------|
| List comprehension | You need the full list in memory |
| Generator expression | You iterate once over large data |
| Dict comprehension | You need key-value pairs |
| Set comprehension | You need unique values |

---

# Common Mistakes

## Overly Complex Comprehensions

```python
# Hard to read
result = [x**2 for x in range(100) if x % 2 == 0 if x % 3 == 0]
```

Fix: use a regular loop when logic gets complex.

---

## Confusing Generator with List

```python
gen = (x for x in range(5))
print(gen)   # <generator object ...>  NOT a list
```

---

# Practice Questions

## Basic

1. Create a list of squares of numbers from 1 to 10.
2. Create a list of even numbers from 1 to 20.
3. Convert all strings in a list to uppercase.
4. Filter out all negative numbers from a list.
5. Create a list of lengths of words in a sentence.
6. Create a list of tuples `(number, square)` for 1–5.
7. Replace negative numbers with 0 in a list.
8. Extract all vowels from a string into a list.
9. Create a list of the first letter of each word.
10. Generate a list of multiples of 3 up to 30.

---

## Intermediate

11. Flatten a 3×3 matrix using a list comprehension.
12. Create a dictionary mapping words to their lengths.
13. Find all numbers divisible by both 3 and 5 from 1–100.
14. Create a set of unique characters in a string.
15. Transpose a matrix using list comprehension.

---

# Mini Project – Grade Report

```python
students = {
    "Raj": 85,
    "Priya": 92,
    "Sam": 67,
    "Anita": 78,
    "Karan": 55
}

grades = {
    name: "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "F"
    for name, score in students.items()
}

passed = [name for name, score in students.items() if score >= 60]
failed = [name for name, score in students.items() if score < 60]

print("Grades:", grades)
print("Passed:", passed)
print("Failed:", failed)
print("Average:", sum(students.values()) / len(students))
```

---

# Day 9 Summary

After completing Day 9, you should be able to:

- Write list comprehensions with and without conditions.
- Use `if-else` inside comprehensions.
- Write dictionary and set comprehensions.
- Use generator expressions for memory efficiency.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 20 minutes |
| Coding Along | 45 minutes |
| Practice Problems | 45 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **2.5 hours**
