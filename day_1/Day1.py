a = int(input("Enter a number: "))
b =  int (input("Enter another number: "))
sum = a+b
sub = a-b
mul = a*b

if b!=0:
    div = a/b
else:
    div = "undefined (division by zero)"

exp = a** b
print("Sum:", sum)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)
print("Exponentiation:", exp)
