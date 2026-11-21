"""Command-line Student Management System.

Records contain a student's name, roll number, and one or more subject marks.
Data is stored in students.json beside this program.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")


def load_students():
    """Load records, returning an empty list for a new or empty data file."""
    if not DATA_FILE.exists() or DATA_FILE.stat().st_size == 0:
        return []
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)
        if not isinstance(records, list):
            print("Data file format is invalid; starting with no records.")
            return []
        return records
    except (json.JSONDecodeError, OSError) as error:
        print(f"Could not load student records: {error}")
        return []


def save_students(students):
    """Write all records to disk in readable JSON format."""
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except OSError as error:
        print(f"Could not save student records: {error}")


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This value cannot be empty.")


def read_marks():
    """Read multiple marks separated by spaces; each mark must be 0-100."""
    while True:
        raw = input("Enter subject marks separated by spaces (e.g. 85 90 78): ")
        try:
            marks = [float(part) for part in raw.split()]
            if not marks:
                print("Enter at least one mark.")
            elif any(mark < 0 or mark > 100 for mark in marks):
                print("Every mark must be between 0 and 100.")
            else:
                return marks
        except ValueError:
            print("Invalid input. Enter numbers separated by spaces.")


def add_student(students):
    print("\n--- Add student ---")
    name = read_non_empty("Student name: ")
    roll_number = read_non_empty("Roll number: ")
    if any(record["roll_number"].casefold() == roll_number.casefold()
           for record in students):
        print("That roll number is already registered.")
        return
    marks = read_marks()
    students.append({"name": name, "roll_number": roll_number, "marks": marks})
    save_students(students)
    print("Student added successfully.")


def view_students(students):
    print("\n--- All students ---")
    if not students:
        print("No student records found.")
        return
    for record in students:
        average = sum(record["marks"]) / len(record["marks"])
        print(f"Name       : {record['name']}")
        print(f"Roll number: {record['roll_number']}")
        print("Marks      :", ", ".join(f"{mark:g}" for mark in record["marks"]))
        print(f"Average    : {average:.2f}")
        print("-" * 32)


def find_student(students, roll_number):
    for record in students:
        if record["roll_number"].casefold() == roll_number.casefold():
            return record
    return None


def search_student(students):
    print("\n--- Search student ---")
    roll_number = input("Enter roll number: ").strip()
    record = find_student(students, roll_number)
    if record is None:
        print("No student found with that roll number.")
        return None
    print("Student found:")
    print(f"Name       : {record['name']}")
    print(f"Roll number: {record['roll_number']}")
    print("Marks      :", ", ".join(f"{mark:g}" for mark in record["marks"]))
    return record


def calculate_average(students):
    print("\n--- Calculate average marks ---")
    record = search_student(students)
    if record is not None:
        average = sum(record["marks"]) / len(record["marks"])
        print(f"Average marks for {record['name']}: {average:.2f}")


def main():
    students = load_students()
    while True:
        print("\n" + "=" * 34)
        print("       STUDENT MANAGEMENT")
        print("=" * 34)
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
            print("Program closed.")
            break
        else:
            print("Invalid choice. Select an option from 1 to 5.")


if __name__ == "__main__":
    main()
