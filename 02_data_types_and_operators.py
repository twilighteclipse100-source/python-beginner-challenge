"""Exercise set 2: data types, conversion, geometry, and operators."""

def main():
    integer_value = 12
    float_value = 3.5
    string_value = "Python"
    boolean_value = True
    print("Data type examples:")
    for value in (integer_value, float_value, string_value, boolean_value):
        print(f"{value!r} is {type(value).__name__}")

    celsius = float(input("\nTemperature in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Fahrenheit: {fahrenheit:.2f}")

    length = float(input("\nRectangle length: "))
    width = float(input("Rectangle width: "))
    print(f"Area: {length * width:.2f}")
    print(f"Perimeter: {2 * (length + width):.2f}")

    a, b = 10, 5
    print("\nComparison operators:")
    print(f"a == b: {a == b}")
    print(f"a != b: {a != b}")
    print(f"a > b: {a > b}")
    print(f"a <= b: {a <= b}")
    print("\nLogical operators:")
    print(f"a > 0 and b > 0: {a > 0 and b > 0}")
    print(f"a < 0 or b > 0: {a < 0 or b > 0}")
    print(f"not (a == b): {not (a == b)}")

if __name__ == "__main__":
    main()
