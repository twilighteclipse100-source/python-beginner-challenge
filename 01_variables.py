# 1. Getting started, output and variables

# Replace these sample details with your own.
name = "Your Name"
branch = "Your Branch"
year = "First Year"

print("Hello! My name is", name)
print("Branch:", branch)
print("Year:", year)
print("I am learning Python.")

student_name = "Aarav"
roll_number = 101
age = 18
cgpa = 8.5

print("\nStudent details")
print("Name:", student_name)
print("Roll number:", roll_number)
print("Age:", age)
print("CGPA:", cgpa)

print("\nBasic arithmetic")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

print("Sum:", first + second)
print("Difference:", first - second)
print("Product:", first * second)

if second != 0:
    print("Quotient:", first / second)
else:
    print("Quotient: Cannot divide by zero.")
