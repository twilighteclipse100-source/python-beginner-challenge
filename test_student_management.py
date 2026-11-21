"""Basic automated tests for Student Management System helpers."""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT_DIR = Path(__file__).resolve().parents[1] / "student_management"
sys.path.insert(0, str(PROJECT_DIR))
import main as student_app


class StudentManagementTests(unittest.TestCase):
    def test_find_student_matches_roll_number_case_insensitively(self):
        students = [{"name": "Aanya", "roll_number": "Ab12", "marks": [80, 90]}]
        self.assertEqual(student_app.find_student(students, "ab12")["name"], "Aanya")

    def test_find_student_returns_none_when_missing(self):
        self.assertIsNone(student_app.find_student([], "404"))

    def test_load_students_when_file_is_missing(self):
        with tempfile.TemporaryDirectory() as folder:
            temporary_file = Path(folder) / "students.json"
            with patch.object(student_app, "DATA_FILE", temporary_file):
                self.assertEqual(student_app.load_students(), [])

    def test_save_and_load_students(self):
        students = [{"name": "Aanya", "roll_number": "24", "marks": [88.0, 92.0]}]
        with tempfile.TemporaryDirectory() as folder:
            temporary_file = Path(folder) / "students.json"
            with patch.object(student_app, "DATA_FILE", temporary_file):
                student_app.save_students(students)
                self.assertEqual(student_app.load_students(), students)


if __name__ == "__main__":
    unittest.main()
