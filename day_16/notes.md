# Python Notes – Day 16
## Regular Expressions (Regex)

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand regex patterns and metacharacters.
- Use `re` module functions: `match`, `search`, `findall`, `sub`, `split`.
- Write patterns for common validation tasks.
- Use groups, quantifiers, and character classes.

---

# What is Regex?

A **regular expression** is a sequence of characters that defines a search pattern. Used for:

- Validating input (email, phone, password).
- Searching and replacing text.
- Parsing structured data.

```python
import re

pattern = r"\d+"
text = "I have 3 cats and 12 dogs"

matches = re.findall(pattern, text)
print(matches)   # ['3', '12']
```

---

# The `re` Module Functions

| Function | Description |
|----------|-------------|
| `re.match(pattern, string)` | Match at the **beginning** |
| `re.search(pattern, string)` | First match **anywhere** |
| `re.findall(pattern, string)` | All non-overlapping matches |
| `re.finditer(pattern, string)` | Iterator of match objects |
| `re.sub(pattern, repl, string)` | Replace matches |
| `re.split(pattern, string)` | Split by pattern |
| `re.compile(pattern)` | Pre-compile a pattern |
| `re.fullmatch(pattern, string)` | Match the **entire** string |

---

# Metacharacters

| Symbol | Meaning |
|--------|---------|
| `.` | Any character except newline |
| `^` | Start of string |
| `$` | End of string |
| `*` | 0 or more |
| `+` | 1 or more |
| `?` | 0 or 1 (optional) |
| `{n}` | Exactly n times |
| `{n,m}` | Between n and m times |
| `\|` | OR |
| `()` | Group |
| `[]` | Character class |
| `\` | Escape |

---

# Special Sequences

| Sequence | Meaning |
|----------|---------|
| `\d` | Digit (0–9) |
| `\D` | Non-digit |
| `\w` | Word character (a-z, A-Z, 0-9, _) |
| `\W` | Non-word character |
| `\s` | Whitespace |
| `\S` | Non-whitespace |
| `\b` | Word boundary |
| `\B` | Non-word boundary |

---

# Character Classes `[]`

```python
[aeiou]      # any vowel
[a-z]        # any lowercase letter
[A-Z]        # any uppercase letter
[0-9]        # any digit (same as \d)
[a-zA-Z0-9]  # alphanumeric
[^aeiou]     # any character that is NOT a vowel
```

---

# `re.match()` vs `re.search()`

```python
import re

text = "Hello, Python 3!"

# match — only checks the start
print(re.match(r"\d", text))   # None

# search — finds anywhere
m = re.search(r"\d", text)
print(m.group())   # 3
```

---

# `re.findall()`

```python
text = "Prices: $10, $25, $100"
prices = re.findall(r"\$\d+", text)
print(prices)   # ['$10', '$25', '$100']
```

---

# `re.sub()`

```python
text = "Hello   World   Python"
clean = re.sub(r"\s+", " ", text)
print(clean)   # Hello World Python

# Remove all digits
no_digits = re.sub(r"\d", "", "abc123def456")
print(no_digits)   # abcdef
```

---

# `re.split()`

```python
text = "one, two; three four"
parts = re.split(r"[,;\s]+", text)
print(parts)   # ['one', 'two', 'three', 'four']
```

---

# Groups `()`

```python
text = "2025-07-26"
m = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)
if m:
    print(m.group(0))   # 2025-07-26  (whole match)
    print(m.group(1))   # 2025
    print(m.group(2))   # 07
    print(m.group(3))   # 26
```

---

## Named Groups

```python
m = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "2025-07-26")
print(m.group("year"))    # 2025
print(m.group("month"))   # 07
```

---

# Flags

| Flag | Meaning |
|------|---------|
| `re.IGNORECASE` / `re.I` | Case-insensitive |
| `re.MULTILINE` / `re.M` | `^` and `$` match each line |
| `re.DOTALL` / `re.S` | `.` matches newline too |

```python
re.findall(r"python", "Python is fun", re.I)   # ['Python']
```

---

# Pre-compiling Patterns

```python
pattern = re.compile(r"\d{3}-\d{4}")

print(pattern.search("Call 555-1234 now"))
print(pattern.findall("555-1111 and 555-2222"))
```

---

# Common Patterns

```python
email_pattern    = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
phone_pattern    = r"^\+?[\d\s\-]{10,15}$"
url_pattern      = r"https?://[\w\-\.]+\.[a-z]{2,}(/\S*)?"
password_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%]).{8,}$"
date_pattern     = r"\d{2}/\d{2}/\d{4}"
ip_pattern       = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
```

---

# Practice Questions

## Basic

1. Check if a string contains only digits.
2. Extract all email addresses from a text.
3. Extract all phone numbers from a text.
4. Replace all whitespace sequences with a single space.
5. Split a string by multiple delimiters.
6. Check if a string starts with "http".
7. Extract all words that start with a capital letter.
8. Count the number of digits in a string.
9. Find all words of exactly 5 characters.
10. Remove all punctuation from a string.

---

## Intermediate

11. Validate an email address.
12. Validate a phone number (10 digits, optional country code).
13. Extract date in DD/MM/YYYY format from a paragraph.
14. Check if a password meets complexity requirements.
15. Find and replace all occurrences of a word (case-insensitive).

---

# Mini Project – Email & Input Validator

```python
import re

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))

def validate_phone(phone):
    pattern = r"^\+?[\d\s\-]{10,15}$"
    return bool(re.fullmatch(pattern, phone.strip()))

def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("At least 8 characters")
    if not re.search(r"[A-Z]", password):
        errors.append("At least one uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("At least one lowercase letter")
    if not re.search(r"\d", password):
        errors.append("At least one digit")
    if not re.search(r"[!@#$%^&*]", password):
        errors.append("At least one special character (!@#$%^&*)")
    return errors

def extract_emails(text):
    return re.findall(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}", text)

print("=== Input Validator ===\n")

email = input("Enter email: ")
print("Email valid:", validate_email(email))

phone = input("Enter phone: ")
print("Phone valid:", validate_phone(phone))

pwd = input("Enter password: ")
errors = validate_password(pwd)
if errors:
    print("Password issues:")
    for e in errors:
        print(f"  - {e}")
else:
    print("Password: Strong ✓")

text = input("\nPaste text to extract emails from:\n")
found = extract_emails(text)
print(f"\nEmails found: {found}")
```

---

# Day 16 Summary

After completing Day 16, you should be able to:

- Use `re.match()`, `re.search()`, `re.findall()`, `re.sub()`, and `re.split()`.
- Write patterns using metacharacters, quantifiers, and character classes.
- Use groups to extract specific parts of a match.
- Apply regex to real-world validation tasks.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
