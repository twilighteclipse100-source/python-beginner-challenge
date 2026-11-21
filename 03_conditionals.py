# 3. Conditional statements

number = int(input("Enter an integer: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

marks = float(input("\nEnter marks out of 100: "))
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 40:
    grade = "E"
else:
    grade = "F"
print("Grade:", grade)

year = int(input("\nEnter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

print("\nSimple calculator")
first = float(input("First number: "))
operator = input("Operation (+, -, *, /): ")
second = float(input("Second number: "))

if operator == "+":
    print("Result:", first + second)
elif operator == "-":
    print("Result:", first - second)
elif operator == "*":
    print("Result:", first * second)
elif operator == "/":
    if second != 0:
        print("Result:", first / second)
    else:
        print("Cannot divide by zero.")
else:
    print("Unknown operation.")
