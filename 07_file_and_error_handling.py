"""Exercise set 7: reading/writing files and handling errors."""

from pathlib import Path

def main():
    data_file = Path(__file__).with_name("student_data.txt")
    data_file.write_text("Python file handling example.\n", encoding="utf-8")
    print("Text read from file:")
    print(data_file.read_text(encoding="utf-8"), end="")

    name = input("\nStudent name: ").strip()
    try:
        marks = float(input("Student marks: "))
        with data_file.open("a", encoding="utf-8") as file:
            file.write(f"Student: {name}, Marks: {marks:g}\n")
    except ValueError:
        print("Invalid marks. Please enter a numeric value.")
    except OSError as error:
        print(f"Could not save the record: {error}")

    try:
        if not data_file.exists():
            print("Data file is missing.")
        elif data_file.stat().st_size == 0:
            print("Data file is empty.")
        else:
            print("\nComplete saved file:")
            print(data_file.read_text(encoding="utf-8"), end="")
    except OSError as error:
        print(f"Could not read the file: {error}")

if __name__ == "__main__":
    main()
