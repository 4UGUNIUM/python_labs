"""Статистика слов во входном тексте."""

import os
import sys
from pathlib import Path

try:
    from src.lib.text import count_freq, normalize, tokenize, top_n
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from lib.text import count_freq, normalize, tokenize, top_n


TABLE = os.getenv("TEXT_STATS_TABLE", "0") == "1"


def text_stat(text: str, *, table: bool = TABLE) -> None:
    """Напечатать базовую статистику для всего переданного текста."""
    tokens = tokenize(normalize(text))
    frequencies = count_freq(tokens)
    popular = top_n(frequencies)
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")
    if table:
        width = max((len(word) for word, _ in popular), default=0)
        width = max(width, len("слово"))
        print(f"{'слово':<{width}} | частота")
        print("-" * (width + 10))
        for word, count in popular:
            print(f"{word:<{width}} | {count}")
    else:
        for word, count in popular:
            print(f"{word}:{count}")


def main() -> None:
    """Прочитать stdin до EOF и вывести статистику."""
    text_stat(sys.stdin.read())


if __name__ == "__main__":
    main()
