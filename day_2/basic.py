# Check Whether the number is even or odd
num = int(input("\nEnter a number: \t"))
if num % 2 ==0:
    print("\nThe number is even.\n")
else:
    print("\nThe number is odd.\n")
    
# check whether the number is positive,negative or zero

if num > 0:
    print("The number is positive.\n")
elif num < 0 :
    print("The number is negative.\n")
else :
    print("The number is 0.\n")
    
# Find a larger of two numbers
a = int(input("\nEnter first number:\t"))
b = int(input("\n Enter second number: \t"))

if a>b:
    print("\nThe larger number is: ",a,"\n")
else:
    print("\nThe larger number is: ",b,"\n")

# Find the largest of  three numbers

c = int(input("Enter the third number:\n"))

if a>b and a>c :
    print("The largest number is :",a,"\n")
elif b>a and b>c :
    print("The largest number is :",b,"\n")
else:
    print("The largest number is :",c,"\n")
    
# Check whether a year is a leap year.

year = int(input("\nEnter a year:\t"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("\nThe year is a leap year.\n")
else:
    print("\nThe year is not a leap year.\n")
    
# Check whether a person is eligible to vote.

age = int(input("Enter your age:\n"))

if age >= 18 :
    print("You can vote.\n")
else: 
    print("You're not eligible to vote.\n")
    
#  Check whether a number is divisible by 5 and 11.

num1 = int(input("Enter a number:\n"))

if num1 % 5 == 0 and num1 % 11 == 0:
    print("The number is divible by both 5 and 11.\n")
else:
    print("The number is not divisible by 5 and 11.\n")

# Check whether a character is a vowel or consonant.

vowel = input("Enter a character:\n")
if vowel in "aeiouAEIOU":
    print("The character is a vowel.\n")
else:
    print("The character is a consonant. \n")
    
# Find the absolute value of a number.

num2 = int(input("Enter a number:\n"))

if num2 < 0:
    print("The absolute value of the number is: ", -num2,"\n")
else:
    print("The absolute value of the number is: ", num2,"\n")
    
# Build a simple grade calculator.
marks = int(input("Enter your marks:\n"))
if marks >= 90:
    print("Your grade is A.\n")
elif marks >= 80:
    print("Your grade is B.\n")
elif marks >= 70:
    print("Your grade is C.\n")
elif marks >= 60:
    print("Your grade is D.\n")
else:
    print("Your grade is F.\n")
    