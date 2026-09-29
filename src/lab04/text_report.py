from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab04.io_txt_csv import read_text, write_csv
from pathlib import Path 
import argparse
    
    
def text_report(path: str | Path, out: str | Path, encoding: str = "utf-8"):
    """принимает на вход файл с текстом и создает csv-файл-отчет"""
    text = read_text(path, encoding=encoding)
    
    if len(text)==0: write_csv([], out, ["word", "count"])
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top = top_n(freq)

    lib = list(freq.items())
    lib.sort(key = lambda x:(-x[1],x[0]))


    if not top: raise ValueError("Не удалось получить топ слов")

    print("Всего слов: ", len(tokens))
    print('Уникальных слов: ', len(set(tokens)))
    print('топ-5: ')
    for i in top:
        print(f"{i[0]}:{i[1]}")

    write_csv(lib, out, ["word", "count"])


def multiple_text_report(paths: list[str], per_file: str | Path, total: str | Path, encoding: str = "utf-8"):
    per_file_rows = []
    total_freq = {}

    for path in paths:
        text = read_text(path, encoding=encoding)
        tokens = tokenize(normalize(text))
        freq = count_freq(tokens)

        # Данные отдельно по каждому файлу
        for word, count in freq.items():
            per_file_rows.append( (Path(path).name, word, count) ) #Path(path).name берет имя крч

        # Общая частота слов во всех файлах
        for word, count in freq.items():
            if word in total_freq:
                total_freq[word] += count
            else:
                total_freq[word] = count

    # Сортировка отчёта по каждому файлу
    per_file_rows.sort(key=lambda item: (item[0], -item[2], item[1]))

    # Общий отчёт
    total_rows = list(total_freq.items())
    total_rows.sort(key=lambda item: (-item[1], item[0]))

    write_csv(per_file_rows, per_file, ("file", "word", "count"))
    write_csv(total_rows, total, ("word", "count"))



#работа с консолью Игнорировать 
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--in",
        dest="input_files",
        nargs="+",
        default=["src/data/lab04/input.txt"]
    )

    parser.add_argument(
        "--out",
        default="src/data/lab04/report.csv"
    )

    parser.add_argument(
        "--encoding",
        default="utf-8"
    )

    parser.add_argument(
        "--per-file"
    )

    parser.add_argument(
        "--total"
    )

    args = parser.parse_args()

    # ★ Несколько файлов
    if args.per_file and args.total:
        multiple_text_report(
            args.input_files,
            args.per_file,
            args.total,
            args.encoding
        )

    # Обычный режим
    else:
        text_report(
            args.input_files[0],
            args.out,
            args.encoding
        )