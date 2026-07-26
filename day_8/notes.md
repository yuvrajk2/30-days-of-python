# Python Notes – Day 8
## Modules – math, random, datetime, os

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Import and use standard library modules.
- Use `math` for mathematical operations.
- Use `random` to generate random numbers and selections.
- Use `datetime` to work with dates and times.
- Use `os` to interact with the operating system.

---

# What is a Module?

A module is a file containing Python code (functions, variables, classes) that you can import and reuse.

```python
import math
print(math.pi)   # 3.141592653589793
```

---

# Ways to Import

```python
import math                    # import the whole module
from math import sqrt          # import one function
from math import sqrt, pi      # import multiple
from math import *             # import everything (avoid)
import math as m               # alias
```

---

# The `math` Module

| Function/Constant | Description |
|-------------------|-------------|
| `math.pi` | π ≈ 3.14159 |
| `math.e` | Euler's number ≈ 2.718 |
| `math.sqrt(x)` | Square root |
| `math.pow(x, y)` | x to the power y |
| `math.floor(x)` | Round down |
| `math.ceil(x)` | Round up |
| `math.fabs(x)` | Absolute value |
| `math.factorial(n)` | n! |
| `math.log(x)` | Natural log |
| `math.log10(x)` | Log base 10 |
| `math.sin(x)` | Sine (radians) |
| `math.cos(x)` | Cosine |

### Example

```python
import math

print(math.sqrt(16))        # 4.0
print(math.factorial(5))    # 120
print(math.ceil(4.2))       # 5
print(math.floor(4.9))      # 4
print(round(math.pi, 4))    # 3.1416
```

---

# The `random` Module

| Function | Description |
|----------|-------------|
| `random.random()` | Float between 0.0 and 1.0 |
| `random.randint(a, b)` | Integer between a and b (inclusive) |
| `random.randrange(start, stop, step)` | Random from range |
| `random.choice(seq)` | Random element from sequence |
| `random.choices(seq, k=n)` | n random elements (with replacement) |
| `random.sample(seq, k)` | k unique elements (no replacement) |
| `random.shuffle(lst)` | Shuffle list in place |
| `random.uniform(a, b)` | Float between a and b |
| `random.seed(n)` | Set seed for reproducibility |

### Example

```python
import random

print(random.random())           # e.g. 0.4732
print(random.randint(1, 10))     # e.g. 7
print(random.choice(["a","b","c"]))   # e.g. 'b'

cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)

print(random.sample(range(1, 50), 6))  # Lottery numbers
```

---

# The `datetime` Module

```python
from datetime import datetime, date, timedelta
```

| Class/Method | Description |
|--------------|-------------|
| `datetime.now()` | Current date and time |
| `date.today()` | Today's date |
| `datetime(y, m, d, H, M, S)` | Specific datetime |
| `strftime(format)` | Format datetime as string |
| `strptime(str, format)` | Parse string to datetime |
| `timedelta(days=n)` | Represent a time duration |

### Example

```python
from datetime import datetime, date, timedelta

now = datetime.now()
print(now)
print(now.year, now.month, now.day)
print(now.strftime("%d/%m/%Y %H:%M:%S"))

today = date.today()
print(today)

# Arithmetic
future = today + timedelta(days=30)
print(f"30 days from now: {future}")

# Difference
birthday = date(2006, 5, 15)
age_days = (today - birthday).days
print(f"Days since birthday: {age_days}")
```

### Format Codes

| Code | Meaning | Example |
|------|---------|---------|
| `%Y` | 4-digit year | 2025 |
| `%m` | Month (01–12) | 07 |
| `%d` | Day (01–31) | 26 |
| `%H` | Hour 24h | 14 |
| `%M` | Minute | 30 |
| `%S` | Second | 05 |
| `%A` | Weekday name | Saturday |
| `%B` | Month name | July |

---

# The `os` Module

| Function | Description |
|----------|-------------|
| `os.getcwd()` | Current working directory |
| `os.listdir(path)` | List files in directory |
| `os.mkdir(name)` | Create a directory |
| `os.makedirs(path)` | Create nested directories |
| `os.remove(file)` | Delete a file |
| `os.rmdir(dir)` | Remove a directory |
| `os.rename(old, new)` | Rename a file/directory |
| `os.path.exists(path)` | Check if path exists |
| `os.path.isfile(path)` | Check if it's a file |
| `os.path.isdir(path)` | Check if it's a directory |
| `os.path.join(a, b)` | Join paths safely |
| `os.path.basename(path)` | Filename from path |
| `os.environ` | Environment variables dict |

### Example

```python
import os

print(os.getcwd())
print(os.listdir("."))

path = os.path.join("folder", "file.txt")
print(path)   # folder/file.txt  or  folder\file.txt

if os.path.exists("data.txt"):
    print("File exists")
```

---

# The `sys` Module (Bonus)

```python
import sys

print(sys.version)      # Python version
print(sys.platform)     # OS name
print(sys.argv)         # Command-line arguments
sys.exit()              # Exit the program
```

---

# Common Mistakes

## Forgetting to Import

```python
print(sqrt(16))   # NameError
```

Fix: `from math import sqrt`.

---

## Wrong Argument Type

```python
import math
math.sqrt("16")   # TypeError
```

---

# Practice Questions

## Basic

1. Print the value of π to 5 decimal places.
2. Find the square root of 144.
3. Generate a random integer between 1 and 100.
4. Pick a random item from a list.
5. Shuffle a deck of cards represented as a list.
6. Print today's date.
7. Print the current time in `HH:MM:SS` format.
8. Calculate the date 100 days from today.
9. List all files in the current directory.
10. Check whether a given file path exists.

---

## Intermediate

11. Generate 6 unique lottery numbers between 1 and 49.
12. Compute the number of days between two dates.
13. Calculate the factorial and log of a number.
14. Build a countdown timer that prints days until an event.
15. Rename all `.txt` files in a folder by adding a prefix.

---

# Mini Project – Random Password Generator

```python
import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:   chars += string.ascii_uppercase
    if use_digits:  chars += string.digits
    if use_symbols: chars += string.punctuation

    password = "".join(random.choices(chars, k=length))
    return password

print("=== Random Password Generator ===")
length = int(input("Password length: "))
use_upper   = input("Include uppercase? (y/n): ").lower() == "y"
use_digits  = input("Include digits? (y/n): ").lower() == "y"
use_symbols = input("Include symbols? (y/n): ").lower() == "y"

how_many = int(input("How many passwords to generate? "))

print("\nGenerated Passwords:")
for i in range(1, how_many + 1):
    print(f"  {i}. {generate_password(length, use_upper, use_digits, use_symbols)}")
```

---

# Day 8 Summary

After completing Day 8, you should be able to:

- Use `math` for mathematical functions and constants.
- Use `random` to generate numbers and make selections.
- Use `datetime` to work with dates, times, and durations.
- Use `os` to interact with the file system.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
