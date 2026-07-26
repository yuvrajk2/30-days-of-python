# Python Notes – Day 15
## Decorators and Context Managers

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand and write decorators.
- Chain multiple decorators.
- Use built-in decorators (`@property`, `@staticmethod`, `@classmethod`).
- Write and use context managers with `with`.
- Create custom context managers.

---

# Decorators

A decorator is a function that **wraps another function** to extend its behaviour without modifying its source code.

---

## Functions as First-Class Objects

Before decorators, understand that functions can be:

```python
# Assigned to a variable
def greet():
    print("Hello!")

say_hi = greet
say_hi()   # Hello!

# Passed as an argument
def run(func):
    func()

run(greet)

# Returned from a function
def make_greeter():
    def inner():
        print("Hi!")
    return inner

fn = make_greeter()
fn()   # Hi!
```

---

## Closures

A closure is an inner function that remembers variables from the outer function's scope.

```python
def multiplier(factor):
    def multiply(x):
        return x * factor   # 'factor' from outer scope
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
```

---

## Writing a Decorator

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function")
        result = func(*args, **kwargs)
        print("After the function")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Raj")
```

**Output**

```
Before the function
Hello, Raj!
After the function
```

The `@my_decorator` syntax is shorthand for `greet = my_decorator(greet)`.

---

## Preserving Function Metadata with `functools.wraps`

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

Without `@wraps`, `func.__name__` would show `wrapper` instead of the original name.

---

## Practical Decorators

### Timer

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    print("Done")

slow_function()
```

---

### Logger

```python
from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b

add(3, 5)
```

---

### Decorator with Arguments

```python
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("Hello!")

say_hello()
```

---

## Stacking Decorators

```python
@timer
@logger
def multiply(a, b):
    return a * b

multiply(4, 5)
```

Applied bottom-up: `logger` first, then `timer`.

---

# Context Managers

A context manager handles setup and teardown automatically using the `with` statement.

```python
with open("file.txt", "r") as f:
    content = f.read()
# file is closed here — even if an error occurred
```

---

## Writing a Context Manager with a Class

Implement `__enter__` and `__exit__`.

```python
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        if exc_type:
            print(f"Exception: {exc_val}")
        return False   # don't suppress exceptions

with ManagedFile("output.txt", "w") as f:
    f.write("Hello!")
```

---

## Writing a Context Manager with `contextlib`

```python
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with managed_file("output.txt", "w") as f:
    f.write("Hello!")
```

---

## Practical Context Manager – Timer

```python
from contextlib import contextmanager
import time

@contextmanager
def timer_block(label="Block"):
    start = time.time()
    try:
        yield
    finally:
        elapsed = time.time() - start
        print(f"{label} took {elapsed:.4f}s")

with timer_block("My computation"):
    total = sum(range(1_000_000))
    print(f"Sum = {total}")
```

---

# Practice Questions

## Basic

1. Write a decorator that prints "Start" and "End" around a function call.
2. Write a decorator that converts the return value to uppercase.
3. Write a decorator that counts how many times a function is called.
4. Write a `timer` decorator that measures execution time.
5. Apply two decorators to the same function.
6. Write a decorator that accepts an argument (e.g., `@repeat(3)`).
7. Use `@property` to create a read-only attribute.
8. Use `with open()` to read a file safely.
9. Create a class-based context manager for a database connection (mock).
10. Create a `contextmanager`-based timer.

---

## Intermediate

11. Write a `cache` decorator that memoises function results.
12. Write an authentication decorator that checks a user role.
13. Write a retry decorator that retries a function up to n times on failure.
14. Create a context manager that changes to a directory and restores on exit.
15. Write a logging context manager that writes to a file.

---

# Mini Project – File Logger

```python
import os
import time
from functools import wraps
from contextlib import contextmanager

LOG_FILE = "app.log"

# --- Context Manager ---
@contextmanager
def log_block(label):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] START: {label}\n")
    try:
        yield
    except Exception as e:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] ERROR in {label}: {e}\n")
        raise
    else:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] END:   {label}\n")

# --- Decorator ---
def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] CALL: {func.__name__}(args={args})\n")
        result = func(*args, **kwargs)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] RETURN: {func.__name__} -> {result}\n")
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b

@log_call
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# --- Usage ---
with log_block("Main Program"):
    print(add(10, 5))
    print(divide(20, 4))
    try:
        print(divide(10, 0))
    except ZeroDivisionError:
        pass

print(f"\nLog written to {LOG_FILE}")
print(open(LOG_FILE).read())
```

---

# Day 15 Summary

After completing Day 15, you should be able to:

- Write decorator functions using closures.
- Preserve function metadata with `functools.wraps`.
- Stack and parameterize decorators.
- Use context managers with `with`.
- Create context managers using classes and `@contextmanager`.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 45 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3.5 hours**
