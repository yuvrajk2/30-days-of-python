# Multiplication Table Generator

# It should generate multiplication table for 1 ,2 ,3...n
# It should align table properly and print in a readable format. 
# tables hsould be printed in a tabular format with proper spacing.
# tables should be in columns

n = int(input("Enter the number of tables to generate: "))

for i in range(1, n + 1):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("\n")  # Add a newline for better readability between tables