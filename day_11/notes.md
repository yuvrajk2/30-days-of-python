# Python Notes – Day 11
## Object-Oriented Programming – Classes, Objects, and Constructors

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Understand the principles of OOP.
- Define classes and create objects.
- Use `__init__` constructors and instance attributes.
- Define and call instance methods.
- Use `self` correctly.

---

# What is OOP?

Object-Oriented Programming organises code around **objects** — bundles of data (attributes) and behaviour (methods).

| Concept | Description |
|---------|-------------|
| Class | Blueprint for creating objects |
| Object | An instance of a class |
| Attribute | Data stored in an object |
| Method | Function that belongs to a class |

---

# The 4 Pillars of OOP

| Pillar | Description |
|--------|-------------|
| Encapsulation | Bundling data and methods together |
| Abstraction | Hiding complex details |
| Inheritance | Child class reuses parent class |
| Polymorphism | Same method, different behaviour |

---

# Defining a Class

```python
class Dog:
    pass
```

---

# Creating Objects

```python
dog1 = Dog()
dog2 = Dog()
```

---

# The `__init__` Constructor

Runs automatically when an object is created.

```python
class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

dog1 = Dog("Buddy", "Labrador", 3)
dog2 = Dog("Max", "Poodle", 5)

print(dog1.name)    # Buddy
print(dog2.breed)   # Poodle
```

---

# `self`

`self` refers to the **current instance** of the class. It is always the first parameter of instance methods.

```python
class Person:
    def __init__(self, name, age):
        self.name = name   # instance attribute
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

p = Person("Raj", 20)
p.greet()
```

---

# Instance Methods

Functions defined inside a class.

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def display(self):
        print(f"Width: {self.width}, Height: {self.height}")
        print(f"Area: {self.area()}, Perimeter: {self.perimeter()}")

r = Rectangle(5, 3)
r.display()
```

---

# Class Attributes vs Instance Attributes

```python
class Student:
    school = "ABC School"   # class attribute (shared by all)

    def __init__(self, name, marks):
        self.name = name     # instance attribute (unique per object)
        self.marks = marks

s1 = Student("Raj", 85)
s2 = Student("Priya", 92)

print(Student.school)   # ABC School
print(s1.school)        # ABC School
print(s1.name)          # Raj
```

---

# Class Methods and Static Methods

## `@classmethod` — Works with the class itself

```python
class Student:
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

s1 = Student("Raj")
s2 = Student("Priya")
print(Student.get_count())   # 2
```

---

## `@staticmethod` — No access to class or instance

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(3, 5))   # 8
```

---

# `__str__` Method

Defines the string representation of an object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

p = Person("Raj", 20)
print(p)   # Person(name=Raj, age=20)
```

---

# Deleting Attributes and Objects

```python
p = Person("Raj", 20)
del p.age          # delete attribute
del p              # delete object
```

---

# Common Mistakes

## Forgetting `self`

```python
class Dog:
    def bark():   # missing self
        print("Woof")

d = Dog()
d.bark()   # TypeError
```

---

## Using Class Attribute as Instance Attribute

```python
class Counter:
    count = 0

c = Counter()
c.count = 10   # creates a new instance attribute, does NOT change class attr
print(Counter.count)   # still 0
```

---

# Practice Questions

## Basic

1. Create a `Car` class with attributes `make`, `model`, and `year`.
2. Add a method `display_info()` to the `Car` class.
3. Create a `Circle` class with a method to compute area and circumference.
4. Create a `Student` class and add a method to check pass/fail.
5. Use `__str__` to return a formatted description of an object.
6. Create a `Person` class with `greet()` method.
7. Add a class attribute `species` to the `Dog` class.
8. Count total objects created using a class attribute.
9. Create a `Temperature` class with methods to convert Celsius to Fahrenheit.
10. Create a static method inside a class.

---

## Intermediate

11. Create a `Library` class that manages a list of books.
12. Create an `Employee` class with `__str__` and a salary raise method.
13. Create a `ShoppingCart` class with add, remove, and total methods.
14. Build a `Stack` class using a list.
15. Build a simple `Student` grade manager class.

---

# Mini Project – Bank Account Class

```python
class BankAccount:
    bank_name = "Python National Bank"

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance   # private attribute
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"Deposited ₹{amount}. New Balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            self.transactions.append(f"Withdrew ₹{amount}")
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

    def show_statement(self):
        print(f"\n--- Statement for {self.owner} (Acc: {self.account_number}) ---")
        for t in self.transactions:
            print(f"  {t}")
        print(f"  Current Balance: ₹{self.__balance}")

    def __str__(self):
        return f"Account({self.owner}, Acc#{self.account_number}, Balance=₹{self.__balance})"

# Usage
acc = BankAccount("Raj", "ACC001", 5000)
print(acc)
acc.deposit(2000)
acc.withdraw(1000)
acc.withdraw(9000)
acc.show_statement()
```

---

# Day 11 Summary

After completing Day 11, you should be able to:

- Define classes and create objects.
- Use `__init__` to initialise objects.
- Write instance methods using `self`.
- Use class attributes, `@classmethod`, and `@staticmethod`.
- Override `__str__` for readable output.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 30 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5 hours**
