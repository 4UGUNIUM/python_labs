import csv
from pathlib import Path



def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    
    """
    Читает текстовый файл и возвращает его содержимое одной строкой.

    Для другой кодировки можно передать, например, encoding="cp1251".
    """
    
    p = Path(path)
    return p.read_text(encoding=encoding)





def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    """Записывает строки в CSV-файл."""
    p = Path(path)

    if rows:
        row_len = len(rows[0])
        for row in rows:
            if len(row) != row_len:
                raise ValueError("Строки имеют разную длину")

    if header is not None:
        for row in rows:
            if len(row) != len(header):
                raise ValueError("Длина строки не совпадает с длиной заголовка")

    ensure_parent_dir(p)
    with p.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",")

        if header is not None:
            writer.writerow(header)
        for row in rows:
            writer.writerow(row)





def ensure_parent_dir(path: str | Path) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)



# txt = read_text("src/data/lab04/input.txt")  # должен вернуть строку
# write_csv([("word","count"),("test",3)], "src/data/check.csv")  # создаст CSV
# # print(txt)
