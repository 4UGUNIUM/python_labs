import argparse
import sys
from pathlib import Path

from src.lib.text import count_freq, normalize, tokenize, top_n


def cat_file(path: str, numbered: bool = False) -> None:
    with Path(path).open(encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            line = line.rstrip("\r\n")
            if numbered:
                print(f"{line_number}: {line}")
            else:
                print(line)


def show_stats(path: str, amount: int) -> None:
    text = Path(path).read_text(encoding="utf-8")
    words = tokenize(normalize(text)) if text.strip() else []

    if not words:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print(f"Топ-{amount}:")
        return

    frequencies = count_freq(words)
    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print(f"Топ-{amount}:")
    for word, count in top_n(frequencies, amount):
        print(f"{word}:{count}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Утилиты для текста: cat и статистика слов")
    commands = parser.add_subparsers(dest="command", required=True)

    cat_parser = commands.add_parser("cat", help="вывести файл построчно")
    cat_parser.add_argument("--input", required=True, help="путь к текстовому файлу")
    cat_parser.add_argument("-n", action="store_true", help="нумеровать строки")

    stats_parser = commands.add_parser("stats", help="посчитать частоты слов")
    stats_parser.add_argument("--input", required=True, help="путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="сколько частых слов показать (по умолчанию 5)")

    args = parser.parse_args(argv)
    if args.command == "stats" and args.top <= 0:
        parser.error("значение --top должно быть больше нуля")

    try:
        if args.command == "cat":
            cat_file(args.input, args.n)
        else:
            show_stats(args.input, args.top)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
