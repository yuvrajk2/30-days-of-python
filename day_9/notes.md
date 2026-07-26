# Python Notes – Day 9
## Exception Handling – try, except, else, finally, raise

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand what exceptions are and why they occur.
- Use `try`, `except`, `else`, and `finally` blocks.
- Catch specific exception types.
- Raise exceptions with `raise`.
- Create custom exceptions.

---

# What is an Exception?

An exception is a runtime error that stops program execution.

```python
print(10 / 0)        # ZeroDivisionError
print(int("abc"))    # ValueError
print(x)            # NameError
print([1,2][5])      # IndexError
```

Without handling, these crash the program.

---

# Common Built-in Exceptions

| Exception | Cause |
|-----------|-------|
| `ZeroDivisionError` | Division by zero |
| `ValueError` | Wrong value type |
| `TypeError` | Wrong data type |
| `NameError` | Variable not defined |
| `IndexError` | List index out of range |
| `KeyError` | Dict key not found |
| `FileNotFoundError` | File does not exist |
| `AttributeError` | Object has no attribute |
| `ImportError` | Module not found |
| `OverflowError` | Number too large |

---

# `try` and `except`

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

**Output**

```
Cannot divide by zero!
```

The program continues instead of crashing.

---

# Catching Multiple Exceptions

## Separate `except` Blocks

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("That is not a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

## Single Block for Multiple Types

```python
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
```

---

## Catch All Exceptions

```python
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

# `else` Block

Runs only when **no exception** occurred.

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
else:
    print(f"Result: {result}")
```

---

# `finally` Block

Always runs — whether an exception occurred or not.

```python
try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Execution complete.")
```

Use `finally` for cleanup (closing files, releasing resources).

---

# `raise` – Raising Exceptions

You can raise exceptions intentionally.

```python
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divider cannot be zero.")
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as e:
    print(f"Caught: {e}")
```

---

## Raising with Custom Message

```python
age = int(input("Enter age: "))
if age < 0:
    raise ValueError("Age cannot be negative.")
```

---

# Custom Exceptions

Create your own exception classes.

```python
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Cannot withdraw ₹{amount}. Balance: ₹{balance}.")

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    new_balance = withdraw(500, 1000)
except InsufficientFundsError as e:
    print(e)
```

---

# Nested `try-except`

```python
try:
    try:
        x = int("abc")
    except ValueError:
        print("Inner: invalid number")
        raise   # re-raise the exception
except ValueError:
    print("Outer: caught again")
```

---

# Exception Hierarchy

```
BaseException
 └── Exception
      ├── ArithmeticError
      │    └── ZeroDivisionError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── ValueError
      ├── TypeError
      └── OSError
           └── FileNotFoundError
```

---

# `assert` Statement

Used for debugging — raises `AssertionError` if condition is False.

```python
def square_root(n):
    assert n >= 0, "Number must be non-negative"
    return n ** 0.5

print(square_root(9))    # 3.0
print(square_root(-1))   # AssertionError
```

---

# Common Mistakes

## Bare `except` (Catches Everything Including System Exits)

```python
try:
    ...
except:   # avoid — too broad
    pass
```

Fix: always catch specific exception types.

---

## Silencing Errors with `pass`

```python
except ValueError:
    pass   # error is swallowed silently
```

Always at least log the error.

---

# Practice Questions

## Basic

1. Handle a `ZeroDivisionError` when dividing two numbers.
2. Handle a `ValueError` when converting user input to int.
3. Handle a `FileNotFoundError` when opening a file.
4. Use `else` to print the result only when no error occurs.
5. Use `finally` to print "Done" regardless of the outcome.
6. Raise a `ValueError` if a user enters a negative number.
7. Catch both `ValueError` and `ZeroDivisionError` in one block.
8. Create a safe division function that never crashes.
9. Handle an `IndexError` when accessing a list element.
10. Handle a `KeyError` when accessing a dictionary key.

---

## Intermediate

11. Create a custom `AgeError` exception for invalid ages.
12. Write a function that validates a password and raises exceptions for each rule broken.
13. Build a safe integer input function that keeps asking until valid.
14. Handle multiple exception types in a file reader.
15. Re-raise an exception after logging it.

---

# Mini Project – ATM Simulation

```python
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive.")
        self.balance += amount
        print(f"Deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Balance: ₹{self.balance}, Requested: ₹{amount}"
            )
        self.balance -= amount
        print(f"Withdrawn ₹{amount}. Balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

atm = ATM(balance=10000)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter choice: ")
    try:
        if choice == "1":
            amount = float(input("Amount to deposit: "))
            atm.deposit(amount)
        elif choice == "2":
            amount = float(input("Amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == "3":
            atm.check_balance()
        elif choice == "4":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice.")
    except InvalidAmountError as e:
        print(f"Invalid Amount: {e}")
    except InsufficientFundsError as e:
        print(f"Transaction Failed: {e}")
    except ValueError:
        print("Please enter a valid number.")
```

---

# Day 9 Summary

After completing Day 9, you should be able to:

- Use `try`, `except`, `else`, `finally` correctly.
- Catch specific and multiple exception types.
- Raise exceptions with custom messages.
- Create and use custom exception classes.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
