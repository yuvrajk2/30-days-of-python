# Python Notes – Day 24
## Recursion

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand recursion and the call stack.
- Write recursive functions with a base case and recursive case.
- Analyse the time and space complexity of recursive solutions.
- Apply recursion to classic problems.
- Understand memoisation to optimise recursion.

---

# What is Recursion?

Recursion is when a function **calls itself** to solve a smaller version of the same problem.

Every recursive function needs:
1. **Base case** — the simplest case that stops the recursion.
2. **Recursive case** — breaks the problem into a smaller sub-problem.

---

# Simple Example – Countdown

```python
def countdown(n):
    if n <= 0:         # base case
        print("Go!")
    else:
        print(n)
        countdown(n - 1)  # recursive case

countdown(5)
```

**Output**

```
5
4
3
2
1
Go!
```

---

# The Call Stack

Each recursive call adds a new **frame** to the call stack.

```
countdown(3)
  countdown(2)
    countdown(1)
      countdown(0) → "Go!"
    ← returns
  ← returns
← returns
```

Python's default recursion limit is 1000. Check with `sys.getrecursionlimit()`.

---

# Classic Recursive Problems

## Factorial

```python
def factorial(n: int) -> int:
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

**Call trace:**
```
factorial(5) = 5 * factorial(4)
             = 5 * 4 * factorial(3)
             = 5 * 4 * 3 * 2 * 1
             = 120
```

---

## Fibonacci

```python
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

for i in range(8):
    print(fib(i), end=" ")   # 0 1 1 2 3 5 8 13
```

**Warning:** this is O(2ⁿ) — exponential! Use memoisation.

---

## Sum of List

```python
def recursive_sum(lst: list[int]) -> int:
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([1, 2, 3, 4, 5]))   # 15
```

---

## Power

```python
def power(base: float, exp: int) -> float:
    if exp == 0:
        return 1
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half           # O(log n)
    return base * power(base, exp - 1)

print(power(2, 10))   # 1024
```

---

## Reverse a String

```python
def reverse(s: str) -> str:
    if len(s) <= 1:
        return s
    return reverse(s[1:]) + s[0]

print(reverse("Python"))   # nohtyP
```

---

## Palindrome Check

```python
def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(is_palindrome("racecar"))   # True
print(is_palindrome("python"))    # False
```

---

## Binary Search (Recursive)

```python
def binary_search(arr: list, target: int, low: int, high: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)
    else:
        return binary_search(arr, target, low, mid - 1)

nums = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(nums, 7, 0, len(nums)-1))   # 3
```

---

## Tower of Hanoi

```python
def hanoi(n: int, source: str, target: str, auxiliary: str) -> None:
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

hanoi(3, "A", "C", "B")
```

---

## Flatten a Nested List

```python
def flatten(lst: list) -> list:
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, [4]], 5]]))   # [1, 2, 3, 4, 5]
```

---

# Memoisation

Cache results of expensive recursive calls.

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(50))   # 12586269025 (instant)
```

Without `lru_cache`, `fib(50)` would take hours.

---

## Manual Memo Dict

```python
memo = {}

def fib(n: int) -> int:
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

---

# Recursion vs Iteration

| Aspect | Recursion | Iteration |
|--------|-----------|-----------|
| Readability | Often cleaner | Can be verbose |
| Stack usage | O(n) stack space | O(1) |
| Speed | Slower (function call overhead) | Faster |
| Risk | Stack overflow | None |
| Best for | Trees, graphs, divide & conquer | Simple loops |

---

# Time Complexity

| Function | Time |
|----------|------|
| `factorial(n)` | O(n) |
| `fib(n)` naive | O(2ⁿ) |
| `fib(n)` memoised | O(n) |
| `binary_search` | O(log n) |
| `power(n)` fast | O(log n) |
| `hanoi(n)` | O(2ⁿ) |

---

# Practice Questions

## Basic

1. Write a recursive function to sum numbers from 1 to n.
2. Write a recursive factorial.
3. Write a recursive Fibonacci (naive).
4. Reverse a string recursively.
5. Check if a string is a palindrome recursively.
6. Count occurrences of an item in a list recursively.
7. Find the maximum element in a list recursively.
8. Compute xⁿ recursively.
9. Print all elements of a list recursively.
10. Flatten a nested list recursively.

---

## Intermediate

11. Write a memoised Fibonacci.
12. Implement binary search recursively.
13. Solve Tower of Hanoi for n disks.
14. Generate all permutations of a string.
15. Calculate the GCD of two numbers using recursion.

---

# Mini Project – Recursive Calculator Collection

```python
from functools import lru_cache
import math

def factorial(n: int) -> int:
    """n! using recursion."""
    if n < 0: raise ValueError("n must be non-negative")
    if n <= 1: return 1
    return n * factorial(n - 1)

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    """nth Fibonacci number (memoised)."""
    if n < 0: raise ValueError("n must be non-negative")
    if n <= 1: return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def power(base: float, exp: int) -> float:
    """base^exp using fast recursion (O log n)."""
    if exp == 0: return 1
    if exp < 0: return 1 / power(base, -exp)
    if exp % 2 == 0:
        half = power(base, exp // 2)
        return half * half
    return base * power(base, exp - 1)

def gcd(a: int, b: int) -> int:
    """GCD via Euclidean algorithm."""
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a: int, b: int) -> int:
    """LCM using GCD."""
    return a * b // gcd(a, b)

def digit_sum(n: int) -> int:
    """Sum of digits of n."""
    n = abs(n)
    if n < 10: return n
    return n % 10 + digit_sum(n // 10)

def is_palindrome(s: str) -> bool:
    """Check palindrome recursively."""
    s = s.lower()
    if len(s) <= 1: return True
    if s[0] != s[-1]: return False
    return is_palindrome(s[1:-1])

MENU = """
=== Recursive Calculator Collection ===
1.  Factorial (n!)
2.  Fibonacci (nth term)
3.  Power (base^exp)
4.  GCD
5.  LCM
6.  Digit Sum
7.  Palindrome Check
8.  Fibonacci Series (first n terms)
0.  Exit
"""

while True:
    print(MENU)
    choice = input("Choice: ").strip()
    try:
        if choice == "1":
            n = int(input("n: "))
            print(f"{n}! = {factorial(n)}")
        elif choice == "2":
            n = int(input("n: "))
            print(f"Fibonacci({n}) = {fibonacci(n)}")
        elif choice == "3":
            b = float(input("Base: "))
            e = int(input("Exponent: "))
            print(f"{b}^{e} = {power(b, e)}")
        elif choice == "4":
            a, b = int(input("a: ")), int(input("b: "))
            print(f"GCD({a}, {b}) = {gcd(a, b)}")
        elif choice == "5":
            a, b = int(input("a: ")), int(input("b: "))
            print(f"LCM({a}, {b}) = {lcm(a, b)}")
        elif choice == "6":
            n = int(input("n: "))
            print(f"Digit sum of {n} = {digit_sum(n)}")
        elif choice == "7":
            s = input("String: ")
            print(f"'{s}' is palindrome: {is_palindrome(s)}")
        elif choice == "8":
            n = int(input("How many terms: "))
            series = [fibonacci(i) for i in range(n)]
            print(f"Fibonacci series: {series}")
        elif choice == "0":
            print("Goodbye!"); break
        else:
            print("Invalid choice.")
    except (ValueError, RecursionError) as e:
        print(f"Error: {e}")
```

---

# Day 24 Summary

After completing Day 24, you should be able to:

- Write recursive functions with correct base and recursive cases.
- Trace the call stack of a recursive function.
- Apply memoisation with `@lru_cache`.
- Implement factorial, Fibonacci, binary search, Hanoi, and more recursively.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
