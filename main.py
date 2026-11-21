"""A beginner-friendly command-line Student Management System.

Student records are stored in students.json in this same folder.
Each student has a name, roll number, and a list of subject marks.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    """Read student records from the JSON file."""
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Warning: Could not read the data file. Starting with an empty list.")
        return []


def save_students(students):
    """Save all student records to the JSON file."""
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def get_non_empty_text(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")


def get_marks():
    """Collect one or more marks and return them as a list."""
    while True:
        raw_marks = input("Enter subject marks separated by spaces: ").strip()
        try:
            marks = [float(value) for value in raw_marks.split()]
            if not marks:
                print("Enter at least one mark.")
            elif any(mark < 0 or mark > 100 for mark in marks):
                print("Marks must be between 0 and 100.")
            else:
                return marks
        except ValueError:
            print("Please enter numbers only, separated by spaces.")


def add_student(students):
    print("\n--- Add student ---")
    name = get_non_empty_text("Student name: ")
    roll_number = get_non_empty_text("Roll number: ")

    if any(student["roll_number"] == roll_number for student in students):
        print("A student with that roll number already exists.")
        return

    marks = get_marks()
    students.append({
        "name": name,
        "roll_number": roll_number,
        "marks": marks
    })
    save_students(students)
    print("Student added and saved successfully.")


def view_students(students):
    print("\n--- All students ---")
    if not students:
        print("No student records found.")
        return

    for student in students:
        average = sum(student["marks"]) / len(student["marks"])
        print(f"Name: {student['name']}")
        print(f"Roll number: {student['roll_number']}")
        print(f"Marks: {student['marks']}")
        print(f"Average: {average:.2f}")
        print("-" * 30)


def search_student(students):
    print("\n--- Search student ---")
    roll_number = input("Enter roll number: ").strip()
    for student in students:
        if student["roll_number"] == roll_number:
            print("Student found:")
            print("Name:", student["name"])
            print("Roll number:", student["roll_number"])
            print("Marks:", student["marks"])
            return student
    print("No student found with that roll number.")
    return None


def calculate_average(students):
    print("\n--- Calculate average marks ---")
    student = search_student(students)
    if student is not None:
        average = sum(student["marks"]) / len(student["marks"])
        print(f"Average marks for {student['name']}: {average:.2f}")


def main():
    students = load_students()

    while True:
        print("\n==============================")
        print("    STUDENT MANAGEMENT")
        print("==============================")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student by roll number")
        print("4. Calculate average marks")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            calculate_average(students)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
