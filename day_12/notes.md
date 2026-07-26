# Python Notes – Day 12
## Inheritance, Encapsulation, Polymorphism, and Dunder Methods

---

# Learning Objectives

By the end of this lesson, you should be able to:

- Use inheritance to create child classes.
- Override methods and use `super()`.
- Apply encapsulation with private and protected attributes.
- Understand polymorphism.
- Use common dunder (magic) methods.

---

# Inheritance

Inheritance lets a child class reuse code from a parent class.

```python
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        print(f"{self.name} says {self.sound}")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

d = Dog("Buddy", "Woof")
c = Cat("Whiskers", "Meow")

d.speak()   # Buddy says Woof
c.speak()   # Whiskers says Meow
```

---

# `super()`

Calls the parent class's method.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, student_id, marks):
        super().__init__(name, age)   # call parent __init__
        self.student_id = student_id
        self.marks = marks

    def display(self):
        super().display()
        print(f"ID: {self.student_id}, Marks: {self.marks}")

s = Student("Raj", 20, "S001", 85)
s.display()
```

---

# Method Overriding

Child class provides its own implementation of a parent method.

```python
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f"{shape.__class__.__name__}: area = {shape.area():.2f}")
```

---

# Types of Inheritance

| Type | Description |
|------|-------------|
| Single | One parent, one child |
| Multiple | Child inherits from multiple parents |
| Multilevel | Chain: A → B → C |
| Hierarchical | One parent, multiple children |

```python
# Multiple Inheritance
class Flyable:
    def fly(self):
        print("Flying!")

class Swimmable:
    def swim(self):
        print("Swimming!")

class Duck(Flyable, Swimmable):
    pass

d = Duck()
d.fly()
d.swim()
```

---

# `isinstance()` and `issubclass()`

```python
print(isinstance(d, Duck))       # True
print(isinstance(d, Flyable))    # True
print(issubclass(Duck, Flyable)) # True
```

---

# Encapsulation

Encapsulation restricts direct access to an object's data.

| Prefix | Access Level |
|--------|-------------|
| `name` | Public — accessible from anywhere |
| `_name` | Protected — convention (not enforced) |
| `__name` | Private — name-mangled by Python |

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

acc = BankAccount(1000)
print(acc.get_balance())     # 1000
# print(acc.__balance)       # AttributeError
print(acc._BankAccount__balance)  # 1000 (name mangling — avoid this)
```

---

## Properties (`@property`)

A cleaner way to implement getters/setters.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0
t.celsius = 30
print(t.celsius)      # 30
```

---

# Polymorphism

The same interface works on different types.

```python
class Dog:
    def sound(self):
        return "Woof"

class Cat:
    def sound(self):
        return "Meow"

class Duck:
    def sound(self):
        return "Quack"

animals = [Dog(), Cat(), Duck()]
for animal in animals:
    print(animal.sound())
```

---

# Dunder (Magic) Methods

Special methods with double underscores that Python calls automatically.

| Method | Called When |
|--------|-------------|
| `__init__` | Object created |
| `__str__` | `str(obj)` or `print(obj)` |
| `__repr__` | `repr(obj)` — developer string |
| `__len__` | `len(obj)` |
| `__add__` | `obj1 + obj2` |
| `__sub__` | `obj1 - obj2` |
| `__mul__` | `obj1 * obj2` |
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |
| `__gt__` | `obj1 > obj2` |
| `__contains__` | `item in obj` |
| `__getitem__` | `obj[key]` |
| `__del__` | Object deleted |

### Example

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __len__(self):
        import math
        return int(math.sqrt(self.x**2 + self.y**2))

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)    # Vector(4, 6)
print(v1 * 3)     # Vector(3, 6)
print(v1 == v2)   # False
print(len(v2))    # 5
```

---

# Abstract Classes

Force child classes to implement specific methods.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        import math
        return math.pi * self.r ** 2
    def perimeter(self):
        import math
        return 2 * math.pi * self.r

# Shape()   # TypeError — cannot instantiate abstract class
c = Circle(5)
print(c.area())
```

---

# Practice Questions

## Basic

1. Create a `Vehicle` class and a `Car` subclass that overrides `describe()`.
2. Use `super()` to call the parent `__init__` from a child class.
3. Create a class hierarchy: `Animal → Mammal → Dog`.
4. Demonstrate method overriding with a `Sound` method.
5. Use `@property` to create a getter and setter.
6. Implement `__str__` and `__repr__` in a class.
7. Implement `__add__` to add two objects.
8. Use `isinstance()` to check object types.
9. Create a private attribute and access it via a getter method.
10. Implement multiple inheritance with two parent classes.

---

## Intermediate

11. Create an abstract `Shape` class with `Circle` and `Triangle` implementations.
12. Implement `__eq__` and `__lt__` for a `Student` class (compare by marks).
13. Create a `Playlist` class with `__len__`, `__getitem__`, and `__contains__`.
14. Implement encapsulation in a `Patient` medical record class.
15. Build a `Temperature` class supporting `+` and `-` operators.

---

# Mini Project – Employee Management System

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def __str__(self):
        return (f"ID: {self.employee_id} | Name: {self.name} | "
                f"Dept: {self.department} | Salary: ₹{self.calculate_salary():,.2f}")

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, dept, monthly_salary):
        super().__init__(name, emp_id, dept)
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary

    def give_raise(self, percent):
        self._monthly_salary *= (1 + percent / 100)
        print(f"Raise applied. New salary: ₹{self._monthly_salary:,.2f}")

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, dept, hourly_rate, hours_worked):
        super().__init__(name, emp_id, dept)
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked

class Manager(FullTimeEmployee):
    def __init__(self, name, emp_id, dept, monthly_salary, bonus):
        super().__init__(name, emp_id, dept, monthly_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self._monthly_salary + self.bonus

# Usage
employees = [
    FullTimeEmployee("Raj", "E001", "Engineering", 80000),
    PartTimeEmployee("Priya", "E002", "Design", 500, 120),
    Manager("Sam", "E003", "Operations", 100000, 20000),
]

print("=== Employee Report ===")
for emp in employees:
    print(emp)

total_payroll = sum(e.calculate_salary() for e in employees)
print(f"\nTotal Payroll: ₹{total_payroll:,.2f}")
```

---

# Day 12 Summary

After completing Day 12, you should be able to:

- Use inheritance and `super()`.
- Override methods in child classes.
- Apply encapsulation with private attributes and `@property`.
- Understand polymorphism through method overriding.
- Implement common dunder methods.

---

# Recommended Practice Time

| Activity | Time |
|----------|------|
| Reading Notes | 45 minutes |
| Coding Along | 60 minutes |
| Practice Problems | 60 minutes |
| Mini Project | 45 minutes |

**Total:** Approximately **3.5–4 hours**
