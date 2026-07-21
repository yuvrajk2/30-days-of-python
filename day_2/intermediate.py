# Build a BMI calculator.
height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kilograms:\n"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("Your BMI is: ", bmi, " - You are underweight.\n")
else:
    if bmi < 24.9:
        print("Your BMI is: ", bmi, " - You have a normal weight.\n")
    else:
        if bmi < 29.9:
            print("Your BMI is: ", bmi, " - You are overweight.\n")
        else:
            print("Your BMI is: ", bmi, " - You are obese.\n")
            

# Create a basic electricity bill calculator.

units = float(input("Enter the number of units consumed:\n"))
VAT = 0.13 # vat = 13%
ampere = 0.05 # ampere = 5%
amount = 0

if units <= 100:
    amount = units * 5
elif units <= 200:
    amount = (100 * 5) + ((units - 100) * 7)
else:
    amount = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    
total_amount = amount + (amount * VAT) + (amount * ampere)
print("The total electricity bill is: ", total_amount, "\n")

# Calculate discounts based on purchase amount.

purchase_amount = float(input("Enter the purchase amount:\n"))
if purchase_amount < 1000:
    discount = 0
elif purchase_amount < 5000:
    discount = purchase_amount * 0.05
else:
    discount = purchase_amount * 0.10

final_amount = purchase_amount - discount
print("The final amount after discount is: ", final_amount, "\n")

# Create a password validation program.
password = input("Enter a password:\n")

if len(password) < 8:
    print("Password is too short. It must be at least 8 characters long.\n")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.\n")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.\n")
else:
    print("Password is valid.\n")


# Build a menu-driven calculator.

print("Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

