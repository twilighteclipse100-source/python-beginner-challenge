# 7. File handling and error handling

from pathlib import Path

file_path = Path("sample_notes.txt")

# Write text to a file, then read it back.
file_path.write_text("Hello! This text was saved using Python.\n", encoding="utf-8")
print("File contents:")
print(file_path.read_text(encoding="utf-8"))

# Save and display a student's name and marks.
student_name = input("Student name: ")
try:
    marks = float(input("Student marks: "))
    with file_path.open("a", encoding="utf-8") as file:
        file.write(f"Student: {student_name}, Marks: {marks}\n")
except ValueError:
    print("Please enter marks as a number.")

# Handle missing or empty files.
try:
    if not file_path.exists():
        print("The data file does not exist yet.")
    elif file_path.stat().st_size == 0:
        print("The data file is empty.")
    else:
        print("\nSaved data:")
        print(file_path.read_text(encoding="utf-8"))
except OSError as error:
    print("Could not access the file:", error)
