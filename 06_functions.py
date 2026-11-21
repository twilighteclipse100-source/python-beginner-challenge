# 6. Functions

def largest_of_three(a, b, c):
    return max(a, b, c)


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


if __name__ == "__main__":
    print("Largest:", largest_of_three(12, 45, 23))
    number = int(input("Enter a number to check for prime: "))
    print("Prime" if is_prime(number) else "Not prime")

    marks = [85, 90, 78, 92, 88]
    print("Average marks:", average_marks(marks))

    first = float(input("Calculator - first number: "))
    operation = input("Choose +, -, * or /: ")
    second = float(input("Second number: "))

    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}
    if operation in operations:
        try:
            print("Result:", operations[operation](first, second))
        except ZeroDivisionError as error:
            print(error)
    else:
        print("Unknown operation.")
