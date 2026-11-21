"""Exercise set 3: if/elif/else, leap years, and a calculator."""

def main():
    number = int(input("Enter an integer: "))
    print("Even" if number % 2 == 0 else "Odd")

    marks = float(input("\nEnter marks out of 100: "))
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
    elif marks >= 90:
        print("Grade: A")
    elif marks >= 80:
        print("Grade: B")
    elif marks >= 70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    elif marks >= 40:
        print("Grade: E")
    else:
        print("Grade: F")

    year = int(input("\nEnter a year: "))
    leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    print("Leap year" if leap else "Not a leap year")

    print("\nCalculator")
    first = float(input("First number: "))
    operator = input("Operator (+, -, *, /): ").strip()
    second = float(input("Second number: "))
    if operator == "+":
        result = first + second
    elif operator == "-":
        result = first - second
    elif operator == "*":
        result = first * second
    elif operator == "/":
        if second == 0:
            print("Cannot divide by zero.")
            return
        result = first / second
    else:
        print("Invalid operator.")
        return
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
