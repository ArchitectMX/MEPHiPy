from pathlib import Path
import json


def process_students(source, destination):
    with open(source, encoding="utf-8") as file:
        students = json.load(file)
    for student in students:
        student["passed"] = student["score"] >= 60
    with open(destination, "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
    return max(students, key=lambda student: student["score"], default=None)


base = Path(__file__).resolve().parent
print("Лучший студент:", process_students(base / "students.json", base / "students_result.json"))
