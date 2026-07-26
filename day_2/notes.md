# Python Notes – Day 2
## Operators, Type Casting, and Conditional Statements

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand different types of operators in Python.
- Perform arithmetic and logical operations.
- Compare values using comparison operators.
- Convert one data type to another.
- Take user input and convert it into the required data type.
- Write decision-making programs using `if`, `elif`, and `else`.

---

# Operators

Operators are special symbols used to perform operations on variables and values.

## Types of Operators

1. Arithmetic Operators
2. Comparison Operators
3. Assignment Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators

---

# 1. Arithmetic Operators

Arithmetic operators perform mathematical operations.

| Operator | Description | Example |
|----------|-------------|---------|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `/` | Division | `5 / 3` |
| `//` | Floor Division | `5 // 3` |
| `%` | Modulus (Remainder) | `5 % 3` |
| `**` | Exponent | `2 ** 4` |

### Example

```python
a = 15
b = 4

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)
```

**Output**

```
Addition: 19
Subtraction: 11
Multiplication: 60
Division: 3.75
Floor Division: 3
Remainder: 3
Power: 50625
```

---

# 2. Comparison Operators

Comparison operators compare two values and return either `True` or `False`.

| Operator | Description |
|----------|-------------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

### Example

```python
x = 10
y = 20

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= 10)
print(y <= 20)
```

**Output**

```
False
True
False
True
True
True
```

---

# 3. Assignment Operators

Assignment operators assign values to variables.

| Operator | Equivalent |
|----------|------------|
| `=` | Assign value |
| `+=` | `x = x + value` |
| `-=` | `x = x - value` |
| `*=` | `x = x * value` |
| `/=` | `x = x / value` |
| `%=` | `x = x % value` |
| `//=` | `x = x // value` |
| `**=` | `x = x ** value` |

### Example

```python
x = 10

x += 5
print(x)

x *= 2
print(x)

x -= 10
print(x)
```

**Output**

```
15
30
20
```

---

# 4. Logical Operators

Logical operators combine multiple conditions.

| Operator | Description |
|----------|-------------|
| `and` | Returns True if both conditions are True |
| `or` | Returns True if at least one condition is True |
| `not` | Reverses the result |

### Example

```python
age = 20

print(age > 18 and age < 30)
print(age < 18 or age > 30)
print(not(age > 18))
```

**Output**

```
True
False
False
```

---

# 5. Identity Operators

Identity operators check whether two variables refer to the same object.

| Operator | Description |
|----------|-------------|
| `is` | Same object |
| `is not` | Different object |

### Example

```python
a = [1, 2]
b = a
c = [1, 2]

print(a is b)
print(a is c)
print(a is not c)
```

**Output**

```
True
False
True
```

---

# 6. Membership Operators

Membership operators check whether a value exists inside a sequence.

| Operator | Description |
|----------|-------------|
| `in` | Exists |
| `not in` | Does not exist |

### Example

```python
languages = ["Python", "Java", "C++"]

print("Python" in languages)
print("JavaScript" in languages)
print("C++" not in languages)
```

**Output**

```
True
False
False
```

---

# Type Casting

Type casting converts one data type into another.

---

## Integer Conversion

```python
num = "25"

number = int(num)

print(number)
print(type(number))
```

---

## Float Conversion

```python
price = "19.99"

price = float(price)

print(price)
```

---

## String Conversion

```python
age = 20

text = str(age)

print(text)
print(type(text))
```

---

## Boolean Conversion

Python treats the following values as `False`:

```python
0
0.0
''
[]
{}
None
False
```

Everything else is considered `True`.

### Example

```python
print(bool(100))
print(bool(0))
print(bool(""))
print(bool("Python"))
```

**Output**

```
True
False
False
True
```

---

# User Input and Type Casting

The `input()` function always returns a string.

```python
age = input("Enter your age: ")

print(type(age))
```

**Output**

```
<class 'str'>
```

Convert it before performing calculations.

```python
age = int(input("Enter your age: "))

print(age + 5)
```

---

# Conditional Statements

Conditional statements allow a program to make decisions.

---

# if Statement

```python
age = 20

if age >= 18:
    print("Adult")
```

---

# if...else Statement

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

---

# if...elif...else Statement

```python
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Fail")
```

---

# Nested if Statement

```python
age = 22
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
```

---

# Ternary Operator

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
```

---

# Common Mistakes

## Using `=` instead of `==`

Incorrect

```python
if age = 18:
    print("Adult")
```

Correct

```python
if age == 18:
    print("Adult")
```

---

## Forgetting Indentation

Incorrect

```python
if age >= 18:
print("Adult")
```

Correct

```python
if age >= 18:
    print("Adult")
```

---

## Forgetting Type Conversion

Incorrect

```python
age = input("Enter age: ")

if age > 18:
    print("Adult")
```

Correct

```python
age = int(input("Enter age: "))

if age > 18:
    print("Adult")
```

---

# Practice Questions

## Basic

1. Check whether a number is even or odd.
2. Check whether a number is positive, negative, or zero.
3. Find the larger of two numbers.
4. Find the largest of three numbers.
5. Check whether a year is a leap year.
6. Check whether a person is eligible to vote.
7. Check whether a number is divisible by 5 and 11.
8. Check whether a character is a vowel or consonant.
9. Find the absolute value of a number.
10. Build a simple grade calculator.

---

## Intermediate

11. Build a BMI calculator.
12. Create a basic electricity bill calculator.
13. Calculate discounts based on purchase amount.
14. Create a password validator.
15. Build a menu-driven calculator.

---

# Mini Project – Grade Calculator

The roadmap project for Day 2 is a grade calculator. It combines input,
type conversion, comparison operators, and an `if`/`elif`/`else` chain.

```python
marks = float(input("Enter marks (0–100): "))

if marks < 0 or marks > 100:
    print("Marks must be between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

### Improvements to Try

1. Reject non-numeric input with `try`/`except`.
2. Display whether the student passed.
3. Calculate the average of several subjects.
4. Turn the grading logic into a reusable function.

The number guessing game is useful additional practice for conditionals,
but the grade calculator is the roadmap mini-project for this day.

---

# Day 2 Summary

After completing Day 2, you should be able to:

- Use all basic Python operators.
- Convert between different data types.
- Accept and process user input.
- Write programs using conditional statements.
- Solve beginner-level logical problems.
- Build small interactive console applications.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45–60 minutes |

**Total:** Approximately **3–3.5 hours**