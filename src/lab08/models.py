from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")


def validate_student(rec):
    """Проверяет запись; при ошибке поднимает ValueError."""
    if not isinstance(rec, dict) or set(rec) != set(STUDENT_FIELDS):
        raise ValueError("Ключи записи должны быть ровно: fio, birthdate, group, gpa")
    for field in ("fio", "group"):
        if not isinstance(rec[field], str) or not rec[field].strip():
            raise ValueError(f"{field}: требуется непустая строка")
    value = rec["birthdate"]
    if not isinstance(value, str):
        raise ValueError("birthdate: требуется строка YYYY-MM-DD")
    try:
        birthday = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError("birthdate: несуществующая дата или неверный формат") from error
    if birthday.isoformat() != value:
        raise ValueError("birthdate: требуется формат YYYY-MM-DD")
    if birthday > date.today():
        raise ValueError("birthdate: дата не должна быть в будущем")
    gpa = rec["gpa"]
    if isinstance(gpa, bool) or not isinstance(gpa, (int, float)) or not 0 <= gpa <= 5:
        raise ValueError("gpa: требуется число от 0 до 5, не bool")


def make_student(fio, birthdate, group, gpa):
    rec = dict(fio=fio, birthdate=birthdate, group=group, gpa=gpa)
    validate_student(rec)
    rec["fio"] = fio.strip()
    rec["group"] = group.strip()
    rec["gpa"] = float(gpa)
    return rec


def student_age(rec, today=None):
    validate_student(rec)
    today = date.today() if today is None else today
    birthday = date.fromisoformat(rec["birthdate"])
    if today < birthday:
        raise ValueError("today: дата раньше рождения")
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def format_student(rec):
    validate_student(rec)
    parts = rec["fio"].split()
    initials = "".join(part[0] + "." for part in parts[1:])
    name = parts[0] + (" " + initials if initials else "")
    return f'{name} ({rec["group"]}), {student_age(rec)} лет, GPA {rec["gpa"]:.2f}'


def student_to_dict(rec):
    validate_student(rec)
    return rec.copy()


def student_from_dict(d):
    validate_student(d)
    return make_student(**d)
