# 2. Data types and operators

integer_value = 10
float_value = 3.14
string_value = "Python"
boolean_value = True

print(type(integer_value), integer_value)
print(type(float_value), float_value)
print(type(string_value), string_value)
print(type(boolean_value), boolean_value)

celsius = float(input("\nTemperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

length = float(input("\nRectangle length: "))
width = float(input("Rectangle width: "))
print("Area:", length * width)
print("Perimeter:", 2 * (length + width))

a = 10
b = 5
print("\nComparison operators")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("\nLogical operators")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a < 0 or b > 0:", a < 0 or b > 0)
print("not (a == b):", not (a == b))
