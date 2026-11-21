# 4. Loops

print("Numbers from 1 to 100:")
for number in range(1, 101):
    print(number, end=" ")
print()

number = int(input("\nEnter a number for its multiplication table: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

n = int(input("\nFind the sum from 1 to N. Enter N: "))
total = 0
for number in range(1, n + 1):
    total += number
print("Sum:", total)

word = input("\nEnter a word: ")
vowel_count = 0
for character in word.lower():
    if character in "aeiou":
        vowel_count += 1
print("Number of vowels:", vowel_count)

print("\nPrime numbers between 1 and 100:")
for number in range(2, 101):
    is_prime = True
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=" ")
print()
