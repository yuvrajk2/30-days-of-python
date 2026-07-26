# 11. Print the Fibonacci series up to n terms.

from encodings.punycode import digits


n = int(input("Enter the number of terms:"))
fib1, fib2 = 0, 1
for i in range(n):
    print(fib1, end=" ")
    fib1, fib2 = fib2, fib1 + fib2
    
# 12. Check whether a number is prime.

num = int(input("\n Enter a number to check if it is prime:"))

if num > 1:
    for i in range(2, int(num/2) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number \n")
    
    
# 13.Find all prime numbers between 1 and 100.
for num in range(1, 101):
    if num > 1:
        for i in range(2, int(num/2) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, "is a prime number \n")

# 14. Reverse a string using a loop.

str = input("Enter a string to reverse:")
reversed_str = ""
for char in str:
    reversed_str = char + reversed_str
print("Reversed string:", reversed_str)

# 15.Find the sum of digits of a number.

num = int(input("Enter a number to find the sum of its digits:"))
sod = 0
while num>0:
    digit = num % 10
    sod += digit
    num //= 10
print("Sum of digits:", sod)