import json
from pathlib import Path

from src.lab08.models import student_from_dict, student_to_dict


def students_to_json(students, path):
    if not isinstance(students, list):
        raise ValueError("Ожидается список студентов")
    data = [student_to_dict(rec) for rec in students]
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def students_from_json(path):
    with Path(path).open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать массив студентов")
    students = []
    for number, rec in enumerate(data, start=1):
        try:
            students.append(student_from_dict(rec))
        except ValueError as error:
            raise ValueError(f"Запись {number}: {error}") from error
    return students
