# Лабораторная работа №4 — Работа с TXT и CSV

## Описание

Работа с текстовыми и CSV-файлами: чтение текста, обработка слов, подсчёт частоты и сохранение результата в CSV.

Для обработки текста используются функции из `src/lib/text.py`.

---

## Структура

```text
python_labs/
├── src/
│   ├── lab04/
│   │   ├── io_txt_csv.py
│   │   ├── text_report.py
│   │   └── README.md
│   │
│   ├── lib/
│   │   └── text.py
│   │
│   └── data/
│       └── lab04/
│           ├── input.txt
│           ├── a.txt
│           ├── b.txt
│           ├── report.csv
│           ├── report_per_file.csv
│           └── report_total.csv
│
└── images/
    └── lab04/
        ├── img01.png
        ├── img02.png
        └── img03.png
```

---

## Задание A — `io_txt_csv.py`

Реализованы функции:

- `read_text()` — чтение текстового файла в выбранной кодировке;
- `write_csv()` — запись данных в CSV;
- `ensure_parent_dir()` — создание родительских директорий при необходимости.

---

## Задание B — `text_report.py`

Программа:

1. читает текст из файла;
2. нормализует и разбивает его на слова;
3. подсчитывает частоту слов;
4. выводит статистику;
5. сохраняет результат в CSV.

### Запуск

Из корня проекта:

```powershell
python -m src.lab04.text_report
```

С указанием входного файла:

```powershell
python -m src.lab04.text_report --in src/data/lab04/input.txt
```

С кодировкой `cp1251`:

```powershell
python -m src.lab04.text_report --in src/data/lab04/input.txt --encoding cp1251
```

С указанием выходного файла:

```powershell
python -m src.lab04.text_report --in src/data/lab04/input.txt --out src/data/lab04/report.csv
```

![Запуск программы](../../images/lab04/img01.png)

![Результат CSV](../../images/lab04/img02.png)

---

## ★ Работа с несколькими файлами

Программа также может обработать несколько входных файлов и создать:

- `report_per_file.csv` — статистику отдельно по каждому файлу;
- `report_total.csv` — общую статистику по всем файлам.

### Запуск

```powershell
python -m src.lab04.text_report --in src/data/lab04/a.txt src/data/lab04/b.txt --per-file src/data/lab04/report_per_file.csv --total src/data/lab04/report_total.csv
```

![Несколько файлов](../../images/lab04/img03.png)
