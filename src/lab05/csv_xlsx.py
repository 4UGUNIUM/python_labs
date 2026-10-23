import csv
from pathlib import Path
from openpyxl import Workbook


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX.
    Первая строка CSV — заголовок. Лист называется Sheet1,
    ширина колонок подбирается по содержимому (минимум 8 символов).
    """
    source = Path(csv_path)
    target = Path(xlsx_path)

    if source.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался CSV-файл: {source}")
    if target.suffix.lower() != ".xlsx":
        raise ValueError(f"Ожидался XLSX-файл: {target}")

    with source.open(encoding="utf-8", newline="") as file:
        rows = list(csv.reader(file))

    if not rows or not rows[0] or not any(value.strip() for value in rows[0]):
        raise ValueError("CSV не обнаружен или пустой или не содержит заголовка и тд(лень расписывывать)")

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Sheet1"

    for row in rows:
        sheet.append(row)

    for column in sheet.columns:
        column_letter = column[0].column_letter
        max_length = max(len(str(cell.value or "")) for cell in column)
        sheet.column_dimensions[column_letter].width = max(8, max_length)

    target.parent.mkdir(parents=True, exist_ok=True)
    workbook.save(target)
