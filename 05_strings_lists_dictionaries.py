"""Exercise set 5: strings, lists, dictionaries, and character counts."""

def main():
    subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
    print("Subjects:")
    for subject in subjects:
        print("-", subject)

    marks = []
    for index in range(5):
        while True:
            try:
                mark = float(input(f"Enter marks for subject {index + 1} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a number.")
    print(f"Total: {sum(marks):.2f}")
    print(f"Average: {sum(marks) / len(marks):.2f}")
    print(f"Highest: {max(marks):.2f}")
    print(f"Lowest: {min(marks):.2f}")

    student = {"name": "Aarav", "roll_number": 101, "marks": marks}
    print("\nStudent dictionary:", student)

    names = ["Aarav", "Diya", "Kabir", "Meera"]
    searched_name = input("\nEnter a name to search: ").strip()
    print("Name exists." if searched_name.casefold() in [n.casefold() for n in names]
          else "Name does not exist.")

    text = input("\nEnter a string for character frequency: ")
    frequencies = {}
    for character in text:
        frequencies[character] = frequencies.get(character, 0) + 1
    print("Character frequencies:")
    for character, count in frequencies.items():
        label = "space" if character == " " else character
        print(f"{label!r}: {count}")

if __name__ == "__main__":
    main()
