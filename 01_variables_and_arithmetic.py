"""Exercise set 1: output, variables, input, and arithmetic."""

def main():
    print("Python Beginner Challenge")
    name = input("Enter your name: ").strip()
    branch = input("Enter your branch: ").strip()
    year = input("Enter your year of study: ").strip()
    print(f"Hello! I am {name}, studying {branch} in {year}.")

    student_name = "Aarav"
    roll_number = 101
    age = 18
    cgpa = 8.5
    print("\nSample student details")
    print(f"Name: {student_name}")
    print(f"Roll number: {roll_number}")
    print(f"Age: {age}")
    print(f"CGPA: {cgpa}")

    first = float(input("\nEnter the first number: "))
    second = float(input("Enter the second number: "))
    print(f"Sum: {first + second}")
    print(f"Difference: {first - second}")
    print(f"Product: {first * second}")
    if second == 0:
        print("Quotient: undefined (division by zero)")
    else:
        print(f"Quotient: {first / second}")

if __name__ == "__main__":
    main()
