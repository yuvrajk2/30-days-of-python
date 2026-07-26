# Python Notes – Day 28
## Testing with `unittest` and `pytest`

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Explain why automated tests are valuable.
- Write test cases with Python's built-in `unittest`.
- Use assertions to describe expected behavior.
- Organize setup and teardown code.
- Understand the basic `pytest` workflow.

---

# Why Test Code?

A test is a small program that checks whether another program behaves as
expected. Tests help you:

- Catch regressions after changes.
- Document how a function should behave.
- Check edge cases consistently.
- Refactor with confidence.

Good tests are focused, repeatable, and independent of one another.

---

# Testing a Small Function

First write a function with a clear contract:

```python
def add(a, b):
    return a + b
```

A test should state an expected result:

```python
assert add(2, 3) == 5
assert add(-2, 2) == 0
```

The built-in `assert` is useful for quick checks. For a test suite, use a
testing framework so tests can be discovered and reported together.

---

# 1. `unittest`

`unittest` is included with Python, so no package installation is required.

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_number(self):
        self.assertEqual(add(-2, 2), 0)

    def test_result_is_not_a_string(self):
        self.assertIsInstance(add(1, 2), int)

if __name__ == "__main__":
    unittest.main()
```

Save this as `test_calculator.py` and run:

```bash
python -m unittest test_calculator.py
```

Common assertions include:

| Assertion | Meaning |
|-----------|---------|
| `assertEqual(a, b)` | Values are equal |
| `assertNotEqual(a, b)` | Values differ |
| `assertTrue(value)` | Value is truthy |
| `assertFalse(value)` | Value is falsy |
| `assertIsNone(value)` | Value is `None` |
| `assertRaises(Error)` | Code raises the expected error |

---

# Testing Exceptions

An exception is part of a function's behavior and should be tested:

```python
def divide(a, b):
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b

class TestDivide(unittest.TestCase):
    def test_division(self):
        self.assertEqual(divide(8, 2), 4)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            divide(8, 0)
```

---

# Setup and Teardown

`setUp()` runs before each test. `tearDown()` runs after each test. Use
these methods for common preparation and cleanup, not for hiding test logic.

```python
class TestListOperations(unittest.TestCase):
    def setUp(self):
        self.values = [3, 1, 2]

    def test_sorting(self):
        self.assertEqual(sorted(self.values), [1, 2, 3])

    def test_original_list_is_unchanged(self):
        sorted(self.values)
        self.assertEqual(self.values, [3, 1, 2])
```

---

# 2. `pytest`

`pytest` is a popular third-party test runner with simple test syntax.
Install it in a virtual environment:

```bash
python -m pip install pytest
```

Create a file named `test_calculator.py`:

```python
import pytest

from calculator import divide

def test_divide():
    assert divide(8, 2) == 4

def test_zero_divisor():
    with pytest.raises(ValueError):
        divide(8, 0)
```

Run all discovered tests:

```bash
pytest
```

By convention, `pytest` discovers files named `test_*.py` or `*_test.py`
and functions whose names begin with `test_`.

## Parametrized Tests

Parametrization avoids repeating the same test structure:

```python
import pytest

@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (-1, 1, 0), (0, 0, 0)],
)
def test_add(a, b, expected):
    assert a + b == expected
```

---

# Testing Principles

### Arrange, Act, Assert

1. **Arrange** the input and initial state.
2. **Act** by calling the function.
3. **Assert** the expected result.

### Test Edge Cases

Consider empty input, zero, negative values, duplicates, very large values,
invalid types, and expected exceptions.

### Avoid Test Coupling

Each test should work when run alone and in any order. A test should not
depend on a previous test changing shared state.

### Test Behavior, Not Implementation

Prefer checking the public result or error rather than private variables or
the exact internal steps used to calculate it.

---

# Practice Questions

## Basic

1. Write tests for a Celsius-to-Fahrenheit converter.
2. Test a function that returns the largest item in a list.
3. Test an empty-list edge case.
4. Test a password validator's valid and invalid inputs.
5. Use `assertRaises` for invalid marks in a grade calculator.

## Intermediate

6. Convert a `unittest` suite to `pytest`.
7. Add parametrized tests for several grading boundaries.
8. Test a file-writing function using a temporary directory.
9. Test that a search utility returns `-1` for a missing value.
10. Run tests after refactoring a calculator.

---

# Mini Project – Test Your Calculator

Create a small calculator module with `add`, `subtract`, `multiply`, and
`divide`, then write tests for:

- Positive, negative, and zero values.
- Decimal division.
- Division by zero.
- Several operations in a `pytest` parametrized test.
- The calculator's behavior when given invalid input.

Example module:

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("cannot divide by zero")
    return a / b
```

Example test file:

```python
import unittest

from calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_divide(self):
        self.assertAlmostEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(7, 0)

if __name__ == "__main__":
    unittest.main()
```

---

# Day 28 Summary

After completing Day 28, you should be able to:

- Write focused tests with `unittest`.
- Use assertions and test expected exceptions.
- Run tests with `python -m unittest`.
- Understand `pytest` discovery and parametrization.
- Test edge cases without depending on test order.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3–3.5 hours**