# Python Notes – Day 1
## Python Basics, Syntax, Variables, Data Types, and Input/Output

---

# What is Python?

Python is a **high-level, interpreted, general-purpose programming language** known for its simple syntax and readability.

It is widely used in:

- Web Development
- Artificial Intelligence
- Machine Learning
- Data Science
- Cybersecurity
- Automation
- Cloud Computing
- Software Development

---

# Features of Python

- Simple and easy to learn
- Readable syntax
- Cross-platform
- Open source
- Large standard library
- Object-oriented
- Supports multiple programming paradigms

---

# Installing Python

1. Download Python from the official website.
2. Run the installer.
3. Check **Add Python to PATH**.
4. Click **Install Now**.

Verify the installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

# Installing Visual Studio Code

Install:

- Visual Studio Code
- Python Extension (Microsoft)

Useful shortcuts:

| Shortcut | Function |
|----------|----------|
| `Ctrl + S` | Save File |
| `Ctrl + Shift + P` | Command Palette |
| `Ctrl + \`` | Open Terminal |
| `Ctrl + /` | Toggle Comment |

---

# First Python Program

```python
print("Hello, World!")
```

**Output**

```
Hello, World!
```

`print()` is a built-in function used to display output on the screen.

---

# Python Syntax

Python uses **indentation** instead of braces (`{}`) to define code blocks.

### Correct

```python
if True:
    print("Hello")
```

### Incorrect

```python
if True:
print("Hello")
```

---

# Comments

Comments make code easier to understand.

## Single-line Comment

```python
# This is a comment
print("Python")
```

## Multi-line Comment

```python
"""
This is a
multi-line comment.
"""
```

---

# Variables

Variables store data.

### Syntax

```python
variable_name = value
```

### Example

```python
name = "Raj"
age = 20
height = 5.8

print(name)
print(age)
print(height)
```

**Output**

```
Raj
20
5.8
```

---

# Variable Naming Rules

## Valid

```python
student_name = "Raj"
_age = 20
marks1 = 90
```

## Invalid

```python
1name = "Raj"
student-name = "Raj"
class = "Python"
```

---

# Naming Convention

Use **snake_case**.

### Good

```python
student_name = "Raj"
total_marks = 450
```

### Avoid

```python
StudentName
studentName
```

---

# Data Types

Python has several built-in data types.

## Integer (`int`)

```python
age = 20
```

---

## Float (`float`)

```python
price = 99.99
```

---

## String (`str`)

```python
name = "Raj"
```

or

```python
name = 'Raj'
```

---

## Boolean (`bool`)

```python
is_student = True
```

Possible values:

```python
True
False
```

---

# Checking Data Types

Use the `type()` function.

```python
age = 20

print(type(age))
```

**Output**

```
<class 'int'>
```

Another example:

```python
print(type(10))
print(type(3.14))
print(type("Python"))
print(type(True))
```

---

# Multiple Variable Assignment

```python
a, b, c = 10, 20, 30

print(a, b, c)
```

---

# Constants

Python does not have true constants.

By convention, write constants in uppercase.

```python
PI = 3.14159
MAX_USERS = 100
```

---

# Input

Use `input()` to receive data from the user.

```python
name = input("Enter your name: ")

print(name)
```

**Output**

```
Enter your name: Raj
Raj
```

---

# Important Note

`input()` always returns a **string**.

```python
age = input("Enter age: ")

print(type(age))
```

**Output**

```
<class 'str'>
```

---

# Output

Display information using `print()`.

```python
print("Hello")
print(10)
print(True)
```

---

# Printing Multiple Values

```python
name = "Raj"
age = 20

print(name, age)
```

**Output**

```
Raj 20
```

---

# Formatted Strings (f-Strings)

```python
name = "Raj"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

**Output**

```
My name is Raj and I am 20 years old.
```

---

# Escape Characters

| Escape | Meaning |
|---------|---------|
| `\n` | New Line |
| `\t` | Tab |
| `\\` | Backslash |
| `\"` | Double Quote |
| `\'` | Single Quote |

Example:

```python
print("Hello\nWorld")
```

**Output**

```
Hello
World
```

---

# Mini Project – Simple Calculator

```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero.")
```

---

# Common Beginner Mistakes

## 1. Missing Quotes

### Incorrect

```python
name = Raj
```

### Correct

```python
name = "Raj"
```

---

## 2. Missing Parentheses

### Incorrect

```python
print
```

### Correct

```python
print("Hello")
```

---

## 3. Incorrect Indentation

### Incorrect

```python
if True:
print("Hello")
```

### Correct

```python
if True:
    print("Hello")
```

---

## 4. Mixing Strings and Numbers

### Incorrect

```python
age = 20
print("Age: " + age)
```

### Correct

```python
print("Age:", age)
```

or

```python
print(f"Age: {age}")
```

---

# Practice Questions

1. Print your name.
2. Print your age.
3. Store your city in a variable and print it.
4. Take the user's name as input and greet them.
5. Take two numbers as input and print their sum.
6. Display the data type of different variables.
7. Swap two variables.
8. Calculate the area of a rectangle.
9. Convert Celsius to Fahrenheit.
10. Build a simple calculator.

---

# Day 1 Summary

After completing Day 1, you should be able to:

- Install Python and Visual Studio Code.
- Write and execute Python programs.
- Understand Python syntax and indentation.
- Use comments effectively.
- Create and use variables.
- Work with the basic data types (`int`, `float`, `str`, and `bool`).
- Accept user input and display output.
- Format output using f-strings.
- Build a simple calculator.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 45 minutes |
| Practice Questions | 45 minutes |
| Mini Project | 30–45 minutes |

**Total:** Approximately **2.5–3 hours**