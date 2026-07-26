# Python Notes – Day 14
## List Comprehensions and Generator Expressions

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Write concise list comprehensions.
- Add conditions and nested comprehensions.
- Write dictionary and set comprehensions.
- Use generator expressions for memory-efficient processing.
- Understand the difference between lists and generators.

---

# List Comprehensions

A one-line shortcut for building lists.

### Without Comprehension

```python
squares = []
for x in range(1, 6):
    squares.append(x ** 2)
```

### With Comprehension

```python
squares = [x ** 2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]
```

---

# Syntax Forms

```python
# Basic
[expression for item in iterable]

# With filter
[expression for item in iterable if condition]

# With transformation
[expr_true if condition else expr_false for item in iterable]
```

---

# Examples

```python
# Even numbers
evens = [x for x in range(20) if x % 2 == 0]

# Uppercase strings
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]

# Label even/odd
labels = ["even" if x % 2 == 0 else "odd" for x in range(1, 6)]

# Lengths of words
lengths = [len(w) for w in words]

# Filtering and transforming together
result = [x**2 for x in range(1, 11) if x % 3 == 0]
```

---

# Nested List Comprehension

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]

# Transpose
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
```

---

# Dictionary Comprehension

```python
# Basic
squares = {x: x**2 for x in range(1, 6)}

# With condition
even_sq = {x: x**2 for x in range(1, 11) if x % 2 == 0}

# Invert keys and values
original = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in original.items()}

# Word lengths
words = ["apple", "banana", "cherry"]
lengths = {w: len(w) for w in words}
```

---

# Set Comprehension

```python
# Unique squares
unique = {x**2 for x in [-3, -2, -1, 0, 1, 2, 3]}
print(unique)   # {0, 1, 4, 9}

# Unique characters
chars = {c.lower() for c in "Hello World" if c != " "}
```

---

# Generator Expressions

Like list comprehensions but **lazy** — they produce values one at a time without building the full list.

```python
# List comprehension — builds entire list in memory
sq_list = [x**2 for x in range(1_000_000)]

# Generator expression — computes on demand
sq_gen = (x**2 for x in range(1_000_000))
```

---

## Using Generators

```python
gen = (x**2 for x in range(1, 6))

print(next(gen))   # 1
print(next(gen))   # 4

for val in gen:    # continues from where we left off
    print(val)     # 9, 16, 25
```

---

## Generators with Built-in Functions

```python
nums = (x for x in range(1, 101))

print(sum(nums))     # 5050
print(max(x**2 for x in range(1, 6)))   # 25
print(any(x > 90 for x in [80, 85, 95, 70]))   # True
print(all(x > 0 for x in [1, 2, 3, 4]))         # True
```

---

## Generator Functions (`yield`)

```python
def count_up(start, end):
    while start <= end:
        yield start
        start += 1

for n in count_up(1, 5):
    print(n)
```

---

## `yield from`

```python
def chain(*iterables):
    for it in iterables:
        yield from it

for x in chain([1, 2], [3, 4], [5]):
    print(x)
```

---

# Comparing List vs Generator

| Feature | List Comprehension | Generator Expression |
|---------|-------------------|---------------------|
| Syntax | `[ ]` | `( )` |
| Memory | Stores all at once | One item at a time |
| Speed | Faster for repeated access | Faster for single pass |
| Reusable | ✅ | ❌ (exhausted after one pass) |
| `len()` | ✅ | ❌ |

---

# When to Use Each

- **List** — you need all items, multiple passes, indexing, or `len()`.
- **Generator** — one-pass processing, large/infinite data streams.

---

# Practice Questions

## Basic

1. Create a list of cubes of numbers 1–10.
2. Filter only words longer than 5 characters from a list.
3. Replace all negative numbers in a list with 0.
4. Create a list of tuples `(index, value)` from a list.
5. Generate a list of multiples of 7 up to 100.
6. Create a dict mapping numbers to their cubes.
7. Generate a set of unique vowels from a string.
8. Flatten a 3×3 matrix.
9. Transpose a 3×3 matrix.
10. Label numbers 1–20 as "fizz" (div by 3), "buzz" (div by 5), or "fizzbuzz".

---

## Intermediate

11. Find all Pythagorean triples where a, b, c ≤ 20.
12. Create a generator that yields prime numbers indefinitely.
13. Generate a password list from all combinations of two characters.
14. Use a generator to process a large range without storing it.
15. Build a frequency dictionary from a list using comprehension.

---

# Mini Project – Password List Generator

```python
import string
import random

def generate_passwords(
    count,
    length,
    use_upper=True,
    use_digits=True,
    use_symbols=True
):
    """Generator that yields random passwords one at a time."""
    chars = string.ascii_lowercase
    if use_upper:   chars += string.ascii_uppercase
    if use_digits:  chars += string.digits
    if use_symbols: chars += "!@#$%^&*"

    for _ in range(count):
        yield "".join(random.choices(chars, k=length))

def strength(password):
    has_upper   = any(c.isupper() for c in password)
    has_digit   = any(c.isdigit() for c in password)
    has_symbol  = any(c in "!@#$%^&*" for c in password)
    score = sum([has_upper, has_digit, has_symbol])
    return ["Weak", "Fair", "Strong", "Very Strong"][score]

print("=== Password List Generator ===")
count  = int(input("How many passwords? "))
length = int(input("Password length? "))

passwords = list(generate_passwords(count, length))

# Use comprehension to pair with strength
report = [(p, strength(p)) for p in passwords]

print("\nGenerated Passwords:")
for i, (pwd, lvl) in enumerate(report, 1):
    print(f"  {i:>2}. {pwd}  [{lvl}]")

strong_count = sum(1 for _, lvl in report if lvl in ("Strong", "Very Strong"))
print(f"\nStrong passwords: {strong_count}/{count}")
```

---

# Day 14 Summary

After completing Day 14, you should be able to:

- Write list, dict, and set comprehensions.
- Add filtering conditions to comprehensions.
- Write nested comprehensions to process 2D data.
- Use generator expressions for memory-efficient processing.
- Write generator functions with `yield`.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 45 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **2.5–3 hours**
