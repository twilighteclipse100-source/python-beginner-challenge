# 5. Strings, lists and dictionaries

subjects = ["Mathematics", "Physics", "Chemistry", "English", "Computer Science"]
print("Subjects:")
for subject in subjects:
    print(subject)

marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i + 1}: "))
    marks.append(mark)

print("\nTotal:", sum(marks))
print("Average:", sum(marks) / len(marks))
print("Highest:", max(marks))
print("Lowest:", min(marks))

student = {
    "name": "Aarav",
    "roll_number": 101,
    "marks": marks
}
print("\nStudent dictionary:", student)

names = ["Aarav", "Diya", "Kabir", "Meera"]
search_name = input("\nEnter a name to search: ")
if search_name in names:
    print(search_name, "exists in the list.")
else:
    print(search_name, "does not exist in the list.")

text = input("\nEnter text to count character frequencies: ")
frequencies = {}
for character in text:
    frequencies[character] = frequencies.get(character, 0) + 1
print("Character frequencies:", frequencies)
