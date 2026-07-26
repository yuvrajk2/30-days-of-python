# Python Notes – Day 19
## Type Hints, mypy, and Pydantic Basics

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Add type hints to variables, functions, and classes.
- Use the `typing` module for complex types.
- Run static type checking with `mypy`.
- Validate data using Pydantic models.

---

# What are Type Hints?

Type hints (PEP 484) let you annotate variables and functions with expected types. Python does **not enforce** them at runtime — they are for documentation, IDE assistance, and static analysis tools.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

---

# Basic Type Hints

```python
# Variables
name: str = "Raj"
age: int = 20
height: float = 5.8
is_student: bool = True

# Functions
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> None:
    print(f"Hello, {name}!")
```

---

# The `typing` Module

For more complex types (before Python 3.9, use `typing`; from 3.9+ use built-ins directly).

| Type | Python 3.9+ | `typing` (older) |
|------|-------------|------------------|
| List | `list[int]` | `List[int]` |
| Dict | `dict[str, int]` | `Dict[str, int]` |
| Tuple | `tuple[int, str]` | `Tuple[int, str]` |
| Set | `set[str]` | `Set[str]` |
| Optional | `int \| None` | `Optional[int]` |
| Union | `int \| str` | `Union[int, str]` |
| Any | `Any` | `Any` |
| Callable | `Callable[[int], str]` | same |

---

## Examples

```python
from typing import Optional, Union, Any

def divide(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b

def process(value: Union[int, str]) -> str:
    return str(value)

# Python 3.10+ shorthand
def divide2(a: float, b: float) -> float | None:
    return a / b if b != 0 else None
```

---

## Collections

```python
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

def get_scores() -> dict[str, float]:
    return {"Raj": 85.5, "Priya": 92.0}

def get_coords() -> tuple[float, float]:
    return (28.6, 77.2)
```

---

## `TypeVar` — Generic Functions

```python
from typing import TypeVar

T = TypeVar("T")

def first(items: list[T]) -> T:
    return items[0]

print(first([1, 2, 3]))       # 1
print(first(["a", "b"]))      # 'a'
```

---

## `Callable`

```python
from typing import Callable

def apply(func: Callable[[int, int], int], a: int, b: int) -> int:
    return func(a, b)

print(apply(lambda x, y: x + y, 3, 5))   # 8
```

---

## `Literal`

```python
from typing import Literal

def set_direction(d: Literal["north", "south", "east", "west"]) -> None:
    print(f"Going {d}")
```

---

# Type Hints in Classes

```python
class Student:
    name: str
    age: int
    marks: list[float]

    def __init__(self, name: str, age: int, marks: list[float]) -> None:
        self.name = name
        self.age = age
        self.marks = marks

    def average(self) -> float:
        return sum(self.marks) / len(self.marks)

    def __str__(self) -> str:
        return f"Student({self.name}, avg={self.average():.1f})"
```

---

# mypy — Static Type Checker

`mypy` reads your code and reports type errors **without running it**.

```bash
pip install mypy
mypy script.py
```

### Example

```python
# bad_types.py
def add(a: int, b: int) -> int:
    return a + b

result = add("hello", 5)   # Type error!
```

```bash
mypy bad_types.py
# error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

---

## `mypy` Configuration in `pyproject.toml`

```toml
[tool.mypy]
python_version = "3.11"
strict = true
ignore_missing_imports = true
```

---

# Pydantic – Data Validation

Pydantic models validate data at runtime using type hints.

```bash
pip install pydantic
```

---

## Basic Model

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# Valid
user = User(name="Raj", age=20, email="raj@example.com")
print(user)
print(user.name)   # Raj

# Invalid — Pydantic raises ValidationError
try:
    bad = User(name="Raj", age="twenty", email="not-an-email")
except Exception as e:
    print(e)
```

---

## Optional Fields and Defaults

```python
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    in_stock: bool = True

p = Product(name="Laptop", price=999.99)
print(p.in_stock)    # True
print(p.description) # None
```

---

## Validators

```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("age")
    @classmethod
    def age_must_be_positive(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Age must be positive")
        return v

    @field_validator("email")
    @classmethod
    def email_must_have_at(cls, v: str) -> str:
        if "@" not in v:
            raise ValueError("Invalid email")
        return v.lower()
```

---

## Nested Models

```python
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    pincode: str

class Person(BaseModel):
    name: str
    age: int
    address: Address

data = {
    "name": "Raj",
    "age": 20,
    "address": {"street": "123 Main St", "city": "Delhi", "pincode": "110001"}
}

person = Person(**data)
print(person.address.city)   # Delhi
```

---

## JSON Serialization

```python
print(person.model_dump())          # dict
print(person.model_dump_json())     # JSON string
```

---

# Practice Questions

## Basic

1. Add type hints to a function that takes a name and age and returns a greeting.
2. Annotate a function that returns a list of integers.
3. Use `Optional` for a function that may return `None`.
4. Use `Union` for a function that accepts `int` or `str`.
5. Create a typed `Student` class.
6. Run `mypy` on a script and fix all type errors.
7. Create a basic Pydantic model for a `Book`.
8. Add a default value to a Pydantic field.
9. Validate data with a Pydantic `field_validator`.
10. Serialize a Pydantic model to a dictionary.

---

## Intermediate

11. Create a Pydantic model for a `Product` with nested `Category`.
12. Write a function typed with `Callable` and `TypeVar`.
13. Use `Literal` to restrict a function argument.
14. Configure `mypy` in `pyproject.toml`.
15. Parse JSON data directly into a Pydantic model.

---

# Mini Project – User Data Validator

```python
from pydantic import BaseModel, field_validator, EmailStr
from typing import Optional
import re

try:
    from pydantic import EmailStr
except ImportError:
    EmailStr = str   # fallback if email-validator not installed

class Address(BaseModel):
    street: str
    city: str
    pincode: str

    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, v: str) -> str:
        if not re.fullmatch(r"\d{6}", v):
            raise ValueError("Pincode must be 6 digits")
        return v

class UserRegistration(BaseModel):
    username: str
    email: str
    age: int
    phone: str
    address: Address
    bio: Optional[str] = None

    @field_validator("username")
    @classmethod
    def username_alphanumeric(cls, v: str) -> str:
        if not re.fullmatch(r"[a-zA-Z0-9_]{3,20}", v):
            raise ValueError("Username must be 3-20 alphanumeric chars or underscores")
        return v

    @field_validator("age")
    @classmethod
    def validate_age(cls, v: int) -> int:
        if not (0 < v < 120):
            raise ValueError("Age must be between 1 and 119")
        return v

    @field_validator("phone")
    @classmethod
    def validate_phone(cls, v: str) -> str:
        if not re.fullmatch(r"\+?\d{10,13}", v.replace(" ", "")):
            raise ValueError("Invalid phone number")
        return v

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        if not re.fullmatch(r"[\w\.-]+@[\w\.-]+\.[a-zA-Z]{2,}", v):
            raise ValueError("Invalid email address")
        return v.lower()

# Test data
valid_data = {
    "username": "raj_20",
    "email": "Raj@Example.COM",
    "age": 20,
    "phone": "+919876543210",
    "address": {"street": "123 MG Road", "city": "Delhi", "pincode": "110001"},
    "bio": "Python learner"
}

invalid_data = {
    "username": "r",            # too short
    "email": "not-an-email",
    "age": -5,
    "phone": "123",
    "address": {"street": "X", "city": "Y", "pincode": "12345"},  # 5 digits
}

from pydantic import ValidationError

print("=== Valid Data ===")
try:
    user = UserRegistration(**valid_data)
    print(user.model_dump())
except ValidationError as e:
    print(e)

print("\n=== Invalid Data ===")
try:
    user = UserRegistration(**invalid_data)
except ValidationError as e:
    for err in e.errors():
        print(f"  Field: {err['loc']} | Error: {err['msg']}")
```

---

# Day 19 Summary

After completing Day 19, you should be able to:

- Add type hints to functions, variables, and classes.
- Use `Optional`, `Union`, `list`, `dict`, `Callable`, and `TypeVar`.
- Run `mypy` to catch type errors before runtime.
- Create Pydantic models for data validation and serialisation.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 30 minutes |

**Total:** Approximately **3 hours**
