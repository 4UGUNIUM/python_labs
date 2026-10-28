import csv
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Конвертирует CSV в XLSX.
    Первая строка CSV — заголовок. Лист называется Sheet1,
    ширина колонок подбирается по содержимому (минимум 8 символов).
    """
    try:
        from openpyxl import Workbook
    except ModuleNotFoundError as error:
        if error.name != "openpyxl":
            raise
        raise RuntimeError("Для создания XLSX установите openpyxl: python -m pip install openpyxl") from error

    source = Path(csv_path)
    target = Path(xlsx_path)

    if source.suffix.lower() != ".csv":
        raise ValueError(f"Ожидался CSV-файл: {source}")
    if target.suffix.lower() != ".xlsx":
        raise ValueError(f"Ожидался XLSX-файл: {target}")

    with source.open(encoding="utf-8", newline="") as file:
        rows = list(csv.reader(file))

    if not rows or not rows[0] or not any(value.strip() for value in rows[0]):
        raise ValueError("CSV пустой или не содержит заголовка")

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

csv_to_xlsx("src/data/lab06/out/people.csv", "src/data/output.xlsx")