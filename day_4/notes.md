# Python Notes – Day 4
## Functions – Defining, Parameters, Return Values, and Scope

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Define and call functions.
- Use positional, keyword, default, and variable-length arguments.
- Return values from functions.
- Understand local and global scope.
- Write recursive functions.

---

# What is a Function?

A function is a reusable block of code that performs a specific task.

### Benefits

- Avoids code repetition (DRY – Don't Repeat Yourself).
- Makes programs easier to read and maintain.
- Breaks a big problem into smaller pieces.

---

# Defining a Function

### Syntax

```python
def function_name():
    # body
```

### Example

```python
def greet():
    print("Hello, World!")

greet()   # calling the function
```

**Output**

```
Hello, World!
```

---

# Functions with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Raj")
greet("Priya")
```

**Output**

```
Hello, Raj!
Hello, Priya!
```

---

# Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(3, 5)
```

**Output**

```
8
```

---

# Return Values

Use `return` to send a value back to the caller.

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
```

**Output**

```
8
```

---

# Returning Multiple Values

```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 9, 5])
print(low, high)
```

**Output**

```
1 9
```

---

# Default Parameters

A default value is used when the argument is not provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Raj")
```

**Output**

```
Hello, Guest!
Hello, Raj!
```

---

# Keyword Arguments

Pass arguments by name — order does not matter.

```python
def student(name, age, city):
    print(f"{name}, {age}, {city}")

student(age=20, city="Delhi", name="Raj")
```

**Output**

```
Raj, 20, Delhi
```

---

# Variable-Length Arguments

## `*args` — accepts any number of positional arguments

```python
def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)
total(10, 20)
```

**Output**

```
6
30
```

---

## `**kwargs` — accepts any number of keyword arguments

```python
def display(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

display(name="Raj", age=20, city="Delhi")
```

**Output**

```
name: Raj
age: 20
city: Delhi
```

---

# Scope – Local and Global

## Local Variable

Defined inside a function — accessible only within it.

```python
def greet():
    message = "Hello"   # local
    print(message)

greet()
# print(message)   # Error
```

---

## Global Variable

Defined outside functions — accessible everywhere.

```python
name = "Raj"   # global

def greet():
    print(name)

greet()
```

---

## `global` Keyword

Modify a global variable inside a function.

```python
count = 0

def increment():
    global count
    count += 1

increment()
increment()
print(count)
```

**Output**

```
2
```

---

# Recursion

A function that calls itself.

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

**Output**

```
120
```

---

# Docstrings

Document what a function does.

```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b

print(add.__doc__)
```

---

# Common Mistakes

## Forgetting `return`

```python
def add(a, b):
    a + b   # result is lost

result = add(3, 5)
print(result)   # None
```

Fix: add `return a + b`.

---

## Calling Before Defining

```python
greet()   # Error

def greet():
    print("Hello")
```

---

# Practice Questions

## Basic

1. Write a function that prints "Hello, Python!".
2. Write a function that takes a name and prints a greeting.
3. Write a function that returns the square of a number.
4. Write a function that returns the larger of two numbers.
5. Write a function with a default parameter.
6. Write a function that calculates the area of a rectangle.
7. Write a function that converts Celsius to Fahrenheit.
8. Write a function that checks if a number is even or odd.
9. Write a function using `*args` that returns the sum.
10. Write a function that returns the reverse of a string.

---

## Intermediate

11. Write a recursive function to compute the Fibonacci sequence.
12. Write a function that checks if a number is prime.
13. Write a function using `**kwargs` to display student details.
14. Write a function that counts vowels in a string.
15. Write a function that returns the factorial of a number.

---

# Mini Project – Simple ATM

```python
balance = 10000

def check_balance():
    print(f"Balance: ₹{balance}")

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. New Balance: ₹{balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrawn ₹{amount}. New Balance: ₹{balance}")

check_balance()
deposit(5000)
withdraw(3000)
check_balance()
```

---

# Day 4 Summary

After completing Day 4, you should be able to:

- Define and call functions.
- Use positional, keyword, default, `*args`, and `**kwargs`.
- Return single and multiple values.
- Understand local vs global scope.
- Write recursive functions.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
