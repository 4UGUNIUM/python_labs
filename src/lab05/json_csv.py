import csv
import json
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """

    source = Path(json_path)
    target = Path(csv_path)
    check_extension(source, ".json")#проверка расширения исходного файла
    check_extension(target, ".csv")#проверка расширения целевого файла

    contents = source.read_text(encoding="utf-8")#чтение содержимого JSON

    if not contents.strip():
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    data = json.loads(contents)#запись содержимого JSON

    if not isinstance(data, list) or not data:
        raise ValueError("Некорректная структура JSON: ожидается непустой список словарей")

    if any(not isinstance(row, dict) for row in data):
        raise ValueError("Некорректные данные в JSON")
    

    fieldnames = list(dict.fromkeys(key for row in data for key in row))#получение уникальных ключей из всех словарей
    if not fieldnames:
        raise ValueError("В JSON нет полей для записи в CSV")

    ensure_parent_dir(target)#папки
    with target.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    source = Path(csv_path)
    target = Path(json_path)
    check_extension(source, ".csv")#проверка расширения исходного файла
    check_extension(target, ".json")#проверка расширения целевого файла

    with source.open(encoding="utf-8", newline="") as file:

        reader = csv.DictReader(file)  # чтение CSV
        fieldnames = reader.fieldnames  # получение названий столбцов

        if not fieldnames or not any(fieldnames):
            raise ValueError("CSV пустой или не содержит заголовка")
        if any(name is None or name.strip() == "" for name in fieldnames):
            raise ValueError("Заголовок CSV содержит пустое имя столбца")
        if len(set(fieldnames)) != len(fieldnames):
            raise ValueError("Заголовок CSV содержит повторяющиеся имена столбцов")
        rows = list(reader)

    ensure_parent_dir(target)
    with target.open("w", encoding="utf-8") as file:
        json.dump(rows, file, ensure_ascii=False, indent=2)


def check_extension(path: Path, extension: str) -> None: #чекер расширения файла
    if path.suffix.lower() != extension:
        raise ValueError(f"Ожидался файл с расширением {extension}: {path}")


def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

