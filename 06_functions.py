"""Exercise set 6: reusable functions and a function-based calculator."""

def largest_of_three(first, second, third):
    return max(first, second, third)

def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            return False
    return True

def average_marks(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def main():
    print("Largest of 12, 45, 23:", largest_of_three(12, 45, 23))
    number = int(input("Enter a number to test for primality: "))
    print("Prime" if is_prime(number) else "Not prime")
    sample_marks = [82, 91, 76, 88, 95]
    print("Average of sample marks:", average_marks(sample_marks))

    first = float(input("\nCalculator - first number: "))
    operator = input("Operator (+, -, *, /): ").strip()
    second = float(input("Second number: "))
    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if operator not in operations:
        print("Invalid operator.")
    else:
        try:
            print("Result:", operations[operator](first, second))
        except ZeroDivisionError as error:
            print(error)

if __name__ == "__main__":
    main()
