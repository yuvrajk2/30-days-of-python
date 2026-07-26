# Python Notes – Day 3
## Loops – for, while, break, continue, pass, range()

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Use `for` loops to iterate over sequences.
- Use `while` loops for condition-based repetition.
- Control loop flow with `break`, `continue`, and `pass`.
- Generate number sequences with `range()`.
- Write nested loops.

---

# Why Loops?

Loops allow you to repeat a block of code multiple times without writing it over and over.

```python
# Without loop
print(1)
print(2)
print(3)

# With loop
for i in range(1, 4):
    print(i)
```

---

# The `for` Loop

Used to iterate over a sequence (list, string, range, etc.).

### Syntax

```python
for variable in sequence:
    # body
```

### Example – Iterating a List

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

**Output**

```
apple
banana
cherry
```

---

### Example – Iterating a String

```python
for char in "Python":
    print(char)
```

**Output**

```
P
y
t
h
o
n
```

---

# The `range()` Function

`range()` generates a sequence of numbers.

| Syntax | Description |
|--------|-------------|
| `range(stop)` | 0 to stop-1 |
| `range(start, stop)` | start to stop-1 |
| `range(start, stop, step)` | start to stop-1 with step |

### Example

```python
for i in range(5):
    print(i)
```

**Output**

```
0
1
2
3
4
```

---

```python
for i in range(1, 6):
    print(i)
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

```python
for i in range(0, 11, 2):
    print(i)
```

**Output**

```
0
2
4
6
8
10
```

---

# The `while` Loop

Runs as long as the condition is `True`.

### Syntax

```python
while condition:
    # body
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
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

# Infinite Loop

A `while` loop without a proper exit condition runs forever.

```python
while True:
    print("Running...")
    break   # use break to exit
```

---

# `break` Statement

Exits the loop immediately.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

**Output**

```
1
2
3
4
```

---

# `continue` Statement

Skips the current iteration and moves to the next.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

**Output**

```
1
2
4
5
```

---

# `pass` Statement

A placeholder that does nothing — useful when a body is required but you have nothing to write yet.

```python
for i in range(5):
    pass   # will be implemented later
```

---

# `else` with Loops

The `else` block runs when the loop finishes normally (without `break`).

```python
for i in range(1, 4):
    print(i)
else:
    print("Loop finished")
```

**Output**

```
1
2
3
Loop finished
```

---

# Nested Loops

A loop inside another loop.

```python
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
```

**Output**

```
1 1
1 2
1 3
2 1
...
```

---

### Multiplication Table Using Nested Loops

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
```

---

# `enumerate()`

Returns both the index and the value while looping.

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

**Output**

```
0 apple
1 banana
2 cherry
```

---

# Common Mistakes

## Forgetting to Increment in `while`

```python
# Infinite loop — count never changes
count = 1
while count <= 5:
    print(count)
```

Fix:

```python
while count <= 5:
    print(count)
    count += 1
```

---

## Off-by-One with `range()`

```python
# prints 0-4, not 0-5
for i in range(5):
    print(i)

# to include 5
for i in range(6):
    print(i)
```

---

# Practice Questions

## Basic

1. Print numbers from 1 to 10 using a `for` loop.
2. Print numbers from 10 to 1 using a `while` loop.
3. Print all even numbers from 1 to 20.
4. Print all odd numbers from 1 to 20.
5. Calculate the sum of numbers from 1 to 100.
6. Print the multiplication table of 5.
7. Print each character of a string on a separate line.
8. Count the number of vowels in a string.
9. Print a pattern of stars using nested loops.
10. Find the factorial of a number.

---

## Intermediate

11. Print the Fibonacci series up to n terms.
12. Check whether a number is prime.
13. Find all prime numbers between 1 and 100.
14. Reverse a string using a loop.
15. Find the sum of digits of a number.

---

# Mini Project – Multiplication Table Generator

The roadmap project for Day 3 is a multiplication table generator. It
provides practice with `for`, `range()`, and formatted output.

```python
number = int(input("Enter a number: "))
limit = int(input("How many multiples should be shown? "))

for multiplier in range(1, limit + 1):
    print(f"{number} × {multiplier} = {number * multiplier}")
```

### Improvements to Try

1. Print tables from 1 through 10 using a nested loop.
2. Format several tables as aligned columns.
3. Validate that the limit is positive.
4. Add a `while` loop so the user can generate another table.

The number guessing game above is useful loop practice, but the
multiplication table generator is the roadmap mini-project for this day.

---

# Day 3 Summary

After completing Day 3, you should be able to:

- Write `for` and `while` loops.
- Use `range()` to generate sequences.
- Control loops with `break`, `continue`, and `pass`.
- Write nested loops and multiplication tables.
- Use `else` with loops.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
