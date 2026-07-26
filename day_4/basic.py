# 1. Write a function that prints "Hello, Python!".
def greet():
    print("Hello, Python!")
    
greet()

print("\n")

# 2. Write a function that takes a name and prints a greeting.

def greet(name):
    print(f"Hello, {name}!!")
greet("Raj")
# greet("Sam")

print("\n")

# 3. Write a function that returns the square of a number.

def sqr(num):
    return num*num
result = sqr(6)
print(result)

print("\n")

# 4. Write a function that returns the larger of two numbers.

def great(a,b):
    if a>b:
        return a
    else:
        return b

print(great(5,7))

print("\n")

# 5.Write a function with a default parameter.

def greet(name="Harry"):
    print(f"Hello, {name}!!")

greet()

print("\n")

# 6.Write a function that calculates the area of a rectangle.

def AOR(l,w):
    return l * w
A = AOR(7,9)

print(A)

print("\n")

# 7.Write a function that converts Celsius to Fahrenheit.

def TempConvert(C):
    F = (C * 1.8) + 32
    return F
print(TempConvert(37))

# 8. Write a function that checks if a number is even or odd.

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
print(check_even_odd(9))

# 9. Write a function using *args that returns the sum.

def total(*numbers):
    print(sum(numbers))
total(10,9,8,6)
total(10,29)

# 10. Write a function that returns the reverse of a string.

def ROS(str):
    return str[::-1]
print(ROS("Python"))