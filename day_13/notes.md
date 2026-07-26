# Python Notes – Day 13
## Lambda Functions, map(), filter(), reduce(), and Iterators

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Write and use lambda (anonymous) functions.
- Apply `map()`, `filter()`, and `reduce()`.
- Understand iterators and the iterator protocol.
- Create custom iterators.

---

# Lambda Functions

A lambda is a small, anonymous function defined in a single line.

### Syntax

```python
lambda parameters: expression
```

### Example

```python
square = lambda x: x ** 2
print(square(5))   # 25

add = lambda a, b: a + b
print(add(3, 4))   # 7
```

---

## Lambda with Conditions

```python
is_even = lambda x: "even" if x % 2 == 0 else "odd"
print(is_even(4))   # even
print(is_even(7))   # odd
```

---

## Lambda as Argument (Sort)

```python
students = [("Raj", 85), ("Priya", 92), ("Sam", 78)]
students.sort(key=lambda s: s[1])          # sort by marks
print(students)

students.sort(key=lambda s: s[1], reverse=True)  # descending
print(students)
```

---

# `map()`

Applies a function to **every item** in an iterable. Returns a map object.

```python
map(function, iterable)
```

### Example

```python
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))
print(squares)   # [1, 4, 9, 16, 25]
```

---

### With a Named Function

```python
def double(x):
    return x * 2

result = list(map(double, [1, 2, 3, 4]))
print(result)   # [2, 4, 6, 8]
```

---

### `map()` with Multiple Iterables

```python
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)   # [11, 22, 33]
```

---

# `filter()`

Keeps only items where the function returns `True`.

```python
filter(function, iterable)
```

### Example

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6, 8, 10]
```

---

### Filter Strings

```python
words = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words = list(filter(lambda w: w.startswith("a"), words))
print(a_words)   # ['apple', 'avocado', 'apricot']
```

---

# `reduce()`

Reduces a sequence to a **single value** by applying a function cumulatively.

```python
from functools import reduce

reduce(function, iterable)
```

### Example – Sum

```python
from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, nums)
print(total)   # 15
```

### Example – Product

```python
product = reduce(lambda a, b: a * b, [1, 2, 3, 4, 5])
print(product)   # 120
```

### Example – Maximum

```python
maximum = reduce(lambda a, b: a if a > b else b, [3, 1, 7, 4, 2])
print(maximum)   # 7
```

---

# Combining `map`, `filter`, `reduce`

```python
from functools import reduce

nums = range(1, 11)
result = reduce(
    lambda a, b: a + b,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums))
)
print(result)   # 220  (4+16+36+64+100)
```

---

# Iterators

An **iterator** is an object that returns values one at a time using `next()`.

## `iter()` and `next()`

```python
nums = [1, 2, 3]
it = iter(nums)

print(next(it))   # 1
print(next(it))   # 2
print(next(it))   # 3
# print(next(it)) # StopIteration
```

---

## How `for` Loops Work Internally

```python
for x in [1, 2, 3]:
    print(x)

# is equivalent to:
it = iter([1, 2, 3])
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break
```

---

## Custom Iterator

Implement `__iter__()` and `__next__()`.

```python
class CountUp:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value

for num in CountUp(1, 5):
    print(num)
```

**Output**

```
1
2
3
4
5
```

---

# `zip()` and `enumerate()`

```python
names = ["Raj", "Priya", "Sam"]
marks = [85, 92, 78]

for i, (name, mark) in enumerate(zip(names, marks), 1):
    print(f"{i}. {name}: {mark}")
```

---

# `sorted()` with `key`

```python
words = ["banana", "apple", "cherry", "date"]

# Sort by length
print(sorted(words, key=len))

# Sort by last character
print(sorted(words, key=lambda w: w[-1]))
```

---

# Practice Questions

## Basic

1. Write a lambda to compute the cube of a number.
2. Sort a list of strings by their length using a lambda.
3. Use `map()` to convert a list of strings to integers.
4. Use `filter()` to keep only positive numbers.
5. Use `reduce()` to find the product of a list.
6. Use `map()` to square all numbers in a list.
7. Use `filter()` to extract words longer than 4 characters.
8. Use `sorted()` with a lambda as the key.
9. Create an iterator that generates even numbers up to n.
10. Use `zip()` to pair two lists.

---

## Intermediate

11. Use `map()` and `filter()` together to get squares of even numbers.
12. Use `reduce()` to find the maximum in a list without `max()`.
13. Create a `FibonacciIterator` class.
14. Use `map()` to convert temperatures from Celsius to Fahrenheit.
15. Build a pipeline: filter → map → reduce on a dataset.

---

# Mini Project – Data Processing Program

```python
from functools import reduce

students = [
    {"name": "Raj",   "marks": 85, "subject": "Math"},
    {"name": "Priya", "marks": 92, "subject": "Science"},
    {"name": "Sam",   "marks": 58, "subject": "Math"},
    {"name": "Anita", "marks": 76, "subject": "Science"},
    {"name": "Karan", "marks": 45, "subject": "Math"},
    {"name": "Neha",  "marks": 88, "subject": "Science"},
]

# Filter: only passed students (marks >= 60)
passed = list(filter(lambda s: s["marks"] >= 60, students))

# Map: add grade to each student
def assign_grade(s):
    grade = "A" if s["marks"] >= 90 else "B" if s["marks"] >= 75 else "C"
    return {**s, "grade": grade}

graded = list(map(assign_grade, passed))

# Reduce: total marks of passed students
total = reduce(lambda acc, s: acc + s["marks"], passed, 0)
average = total / len(passed)

# Sort by marks descending
top_students = sorted(graded, key=lambda s: s["marks"], reverse=True)

print("=== Passed Students with Grades ===")
for s in top_students:
    print(f"  {s['name']:<10} Marks: {s['marks']}  Grade: {s['grade']}")

print(f"\nTotal passed:   {len(passed)}")
print(f"Average marks:  {average:.2f}")
print(f"Top student:    {top_students[0]['name']} ({top_students[0]['marks']})")
```

---

# Day 13 Summary

After completing Day 13, you should be able to:

- Write lambda functions for simple one-line operations.
- Use `map()` to transform data.
- Use `filter()` to select data.
- Use `reduce()` to aggregate data.
- Understand iterators and implement custom ones.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
