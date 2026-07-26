# Python Notes – Day 8
## Strings – Methods, Formatting, and Slicing

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Work with string indexing and slicing.
- Use common string methods.
- Format strings with f-strings and `.format()`.
- Check string properties.

---

# What is a String?

A string is a **sequence of characters** enclosed in quotes.

```python
s1 = "Hello"
s2 = 'Python'
s3 = """Multi
line"""
```

---

# String Indexing

```python
name = "Python"

print(name[0])    # P
print(name[-1])   # n
print(name[2])    # t
```

---

# String Slicing

```python
name = "Python"

print(name[0:3])    # Pyt
print(name[2:])     # thon
print(name[:4])     # Pyth
print(name[::-1])   # nohtyP  (reversed)
print(name[::2])    # Pto
```

---

# String is Immutable

```python
name = "Python"
name[0] = "J"   # TypeError
```

Strings cannot be changed in place — create a new string instead.

---

# String Concatenation and Repetition

```python
s1 = "Hello"
s2 = "World"

print(s1 + " " + s2)   # Hello World
print(s1 * 3)           # HelloHelloHello
```

---

# String Methods

| Method | Description |
|--------|-------------|
| `upper()` | Convert to uppercase |
| `lower()` | Convert to lowercase |
| `title()` | Capitalise each word |
| `capitalize()` | Capitalise first letter |
| `strip()` | Remove leading/trailing whitespace |
| `lstrip()` | Remove leading whitespace |
| `rstrip()` | Remove trailing whitespace |
| `replace(old, new)` | Replace substring |
| `split(sep)` | Split into a list |
| `join(lst)` | Join list into a string |
| `find(sub)` | Return first index or -1 |
| `count(sub)` | Count occurrences |
| `startswith(sub)` | Check prefix |
| `endswith(sub)` | Check suffix |
| `isdigit()` | True if all digits |
| `isalpha()` | True if all letters |
| `isalnum()` | True if letters or digits |
| `isspace()` | True if all whitespace |
| `len()` | Length of string |

---

### Examples

```python
s = "  Hello, Python!  "

print(s.strip())           # "Hello, Python!"
print(s.upper())           # "  HELLO, PYTHON!  "
print(s.lower())           # "  hello, python!  "
print(s.replace("Python", "World"))

words = "apple,banana,cherry"
lst = words.split(",")
print(lst)   # ['apple', 'banana', 'cherry']

print("-".join(lst))   # apple-banana-cherry
```

---

# String Formatting

## f-Strings (Recommended)

```python
name = "Raj"
age = 20
print(f"My name is {name} and I am {age} years old.")
```

---

## `.format()` Method

```python
print("My name is {} and I am {} years old.".format("Raj", 20))
print("My name is {name}.".format(name="Raj"))
```

---

## Old-style `%` Formatting

```python
print("My name is %s and I am %d years old." % ("Raj", 20))
```

---

# Formatting Numbers

```python
pi = 3.14159
print(f"{pi:.2f}")      # 3.14
print(f"{1000000:,}")   # 1,000,000
print(f"{0.75:.0%}")    # 75%
```

---

# String Checking Methods

```python
print("Python".isalpha())    # True
print("123".isdigit())       # True
print("Raj20".isalnum())     # True
print("  ".isspace())        # True
print("hello".startswith("he"))  # True
print("hello".endswith("lo"))    # True
```

---

# `in` Operator

```python
print("Py" in "Python")       # True
print("java" in "Python")     # False
```

---

# Multiline Strings

```python
text = """
Line one
Line two
Line three
"""
print(text)
```

---

# Raw Strings

```python
path = r"C:\Users\Raj\Documents"
print(path)
```

---

# Common Mistakes

## Using `+` to Concatenate Non-Strings

```python
age = 20
print("Age: " + age)   # TypeError
```

Fix: `print("Age: " + str(age))` or use f-string.

---

## `find()` vs `index()`

```python
s = "Hello"
print(s.find("z"))    # -1 (safe)
print(s.index("z"))   # ValueError
```

---

# Practice Questions

## Basic

1. Reverse a string.
2. Count vowels in a string.
3. Check if a string is a palindrome.
4. Convert a string to uppercase and lowercase.
5. Replace all spaces in a string with underscores.
6. Split a sentence into words.
7. Join a list of words into a sentence.
8. Check if a string starts and ends with specific characters.
9. Count occurrences of a character in a string.
10. Remove leading and trailing whitespace.

---

## Intermediate

11. Find the most frequent character in a string.
12. Check if two strings are anagrams.
13. Capitalize the first letter of each word without `title()`.
14. Remove all punctuation from a string.
15. Count the number of words in a sentence.

---

# Mini Project – Caesar Cipher

```python
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

message = input("Enter message: ")
shift = int(input("Enter shift: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

---

# Day 8 Summary

After completing Day 8, you should be able to:

- Index and slice strings.
- Use common string methods.
- Format strings using f-strings and `.format()`.
- Check string properties with `isalpha()`, `isdigit()`, etc.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
