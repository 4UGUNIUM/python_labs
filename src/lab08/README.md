# Лабораторная работа №8 — запись Student

Модель реализована словарём, без классов. Поля: `fio` — непустое ФИО, `birthdate` — существующая дата YYYY-MM-DD не в будущем, `group` — непустая группа, `gpa` — число от 0 до 5. Значения bool и NaN не принимаются.

## Функции

| Функция | Назначение |
|---|---|
| make_student | Проверяет поля, убирает пробелы по краям ФИО и группы, приводит числовой GPA к float |
| validate_student | Проверяет значения и точное совпадение ключей с STUDENT_FIELDS |
| student_age | Считает полные годы с учётом дня рождения; today — объект date |
| format_student | Выводит фамилию, инициалы, группу, возраст и GPA с двумя знаками |
| student_to_dict | Возвращает независимую копию проверенной записи |
| student_from_dict | Проверяет словарь и создаёт новую запись с GPA типа float |
| students_to_json | Проверяет список, сохраняет UTF-8 JSON с ensure_ascii=False и indent=2 |
| students_from_json | Читает массив JSON и проверяет каждую запись |

Политика загрузки — **strict**: первая битая запись вызывает ValueError с её номером (начиная с 1) и причиной. Пропущенные и лишние ключи запрещены. Числовые строки GPA не принимаются. Отсутствующий файл вызывает FileNotFoundError, неверный JSON — JSONDecodeError.

## Запуск

Из корня проекта:

```powershell
python -m src.lab08.check
python -c "from src.lab08.serialize import students_from_json, students_to_json; rows = students_from_json('data/lab08/students_input.json'); students_to_json(rows, 'data/lab08/students_output.json')"
```

Пример функций:

```python
from datetime import date
from src.lab08.models import make_student, student_age, format_student

student = make_student("Иванов Иван Иванович", "2007-09-20", "БИВТ-26-6-1", 4)
print(student_age(student, date(2026, 9, 19)))  # 18
print(student_age(student, date(2026, 9, 20)))  # 19
print(format_student(student))  # возраст зависит от текущей даты
```

## Данные до и после

Входной пример:

```json
{"fio": "Иванов Иван Иванович", "birthdate": "2007-09-20", "group": "БИВТ-26-6-1", "gpa": 4}
```

После загрузки и сохранения:

```json
{
  "fio": "Иванов Иван Иванович",
  "birthdate": "2007-09-20",
  "group": "БИВТ-26-6-1",
  "gpa": 4.0
}
```

Полные массивы: [вход](../../data/lab08/students_input.json), [выход](../../data/lab08/students_output.json), [битая дата](../../data/lab08/students_bad.json).

Проверка охватывает день до рождения и день рождения, копирование, инициалы, неверные ключи, пустые строки, невозможную и будущую даты, GPA вне диапазона, bool, NaN и JSON туда-обратно. Битая дата и GPA 7 отклоняются с сообщениями об ошибках.

Скриншоты запусков пока не добавлены.
