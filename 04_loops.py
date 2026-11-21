"""Exercise set 4: for loops, while loops, and prime numbers."""

def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True

def main():
    print("Numbers from 1 to 100:")
    for number in range(1, 101):
        print(number, end=" " if number < 100 else "\n")

    value = int(input("\nEnter a number for its multiplication table: "))
    for multiplier in range(1, 11):
        print(f"{value} x {multiplier} = {value * multiplier}")

    n = int(input("\nEnter N to calculate 1 + 2 + ... + N: "))
    if n < 1:
        print("N must be at least 1.")
    else:
        total = 0
        for number in range(1, n + 1):
            total += number
        print(f"Sum: {total}")

    word = input("\nEnter a word: ")
    vowels = sum(1 for character in word.lower() if character in "aeiou")
    print(f"Vowel count: {vowels}")

    print("\nPrime numbers between 1 and 100:")
    print(*[number for number in range(1, 101) if is_prime(number)])

if __name__ == "__main__":
    main()
