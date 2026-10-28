from datetime import date
from tempfile import TemporaryDirectory
from pathlib import Path

from src.lab08.models import (
    make_student, validate_student, student_age, format_student,
    student_to_dict, student_from_dict,
)
from src.lab08.serialize import students_from_json, students_to_json


def main():
    student = make_student("Иванов Иван Иванович", "2007-09-20", "БИВТ-26-6-1", 4)
    assert student_age(student, date(2026, 9, 19)) == 18
    assert student_age(student, date(2026, 9, 20)) == 19
    assert isinstance(student["gpa"], float)
    copy = student_to_dict(student)
    assert copy == student and copy is not student
    copy["gpa"] = 5
    assert student["gpa"] == 4
    assert student_from_dict(student) is not student
    assert format_student(student).startswith("Иванов И.И. (БИВТ-26-6-1),")
    bad = [
        dict(student, birthdate="2003-02-30"), dict(student, birthdate="2999-01-01"),
        dict(student, birthdate="20070920"), dict(student, gpa=7),
        dict(student, gpa=True), dict(student, gpa=float("nan")),
        dict(student, gpa=-1), dict(student, fio=" "), dict(student, group=""),
        dict(student, extra=1), {k: v for k, v in student.items() if k != "fio"},
    ]
    for rec in bad:
        try:
            validate_student(rec)
        except ValueError:
            pass
        else:
            raise AssertionError(rec)
    with TemporaryDirectory(dir="data/lab08") as directory:
        path = Path(directory) / "students.json"
        students_to_json([student], path)
        assert students_from_json(path) == [student]
        students_to_json([], path)
        assert students_from_json(path) == []
    try:
        students_from_json("data/lab08/students_bad.json")
    except ValueError as error:
        assert "1" in str(error) and "birthdate" in str(error)
        print(error)
    else:
        raise AssertionError("Битая запись принята")
    try:
        make_student("Иванов Иван", "2007-09-20", "БИВТ-26-6-1", 7)
    except ValueError as error:
        print(error)
    students = students_from_json("data/lab08/students_input.json")
    students_to_json(students, "data/lab08/students_output.json")
    assert students_from_json("data/lab08/students_output.json") == students
    print("OK: возраст, копии, формат, валидация и JSON туда-обратно")


if __name__ == "__main__":
    main()
