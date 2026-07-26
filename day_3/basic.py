#1. Print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)

print("\n")
# 2. Print numbers from 10 to 1 using a while loop.
i = 10
while i >= 1:
    print(i)
    i -= 1

print("\n")
# 3. Print all even numbers from 1 to 20.

for k  in range(1,21):
    if k%2 == 0:
        print(k)

print("\n")
# 4. Print all odd numbers from 1 to 20.

for l in range(1, 21):
    if l%2 != 0:
        print(l)

print("\n")
# 5. Calculate the sum of numbers from 1 to 100.

total = 0
for m in range(1, 101):
    total += m
print(total)

print("\n")

# 6. Print the multiplication table of 5.
for n in range(1, 11):
    print(f"5 x {n} = {5*n}")
    
print("\n")

# 7. Print each character of a string on a separate line.
string = "Hello , World!"
for char in string:
    print(char)

print("\n")

# 8. Count the number of vowels in a string.

str = "Hello, how are you?, I hope you are doing well."
vowels = "aeiouAEIOU"
count = 0
for char in str:
    if char in vowels:
        count += 1

print(count)

print("\n")

# 9.Print 5 different patterns of stars using nested loops.

# Pattern 1: Right triangle
for p in range(1, 6):
    for q in range(p):
        print("*", end="")
    print()

print("\n")

# Pattern 2: Left triangle
for p in range(1, 6):
    for q in range(5 - p):
        print(" ", end="")
    for r in range(p):
        print("*", end="")
    print()

print("\n")

# Pattern 3: Pyramid
for p in range(1, 6):
    for q in range(5 - p):
        print(" ", end="")
    for r in range(2 * p - 1):
        print("*", end="")
    print()

print("\n")

# Pattern 4: Inverted pyramid
for p in range(5, 0, -1):
    for q in range(5 - p):
        print(" ", end="")
    for r in range(2 * p - 1):
        print("*", end="")
    print()

print("\n")

# Pattern 5: Diamond
for p in range(1, 6):
    for q in range(5 - p):
        print(" ", end="")
    for r in range(2 * p - 1):
        print("*", end="")
    print()
    
for p in range(4, 0, -1):
    for q in range(5 - p):
        print(" ", end="")
    for r in range(2 * p - 1):
        print("*", end="")
    print()

print("\n")

# 10. Find the factorial of a number.
num = int(input("Enter a number to find its factorial: "))
def factorial(num):
    if num == 0 or num  == 1:
        return 1
    else:
        return num* factorial(num-1)

print(f"The factorial of {num} is {factorial(num)}")