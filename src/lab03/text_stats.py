from src.lib.text import count_freq, normalize, tokenize, top_n


TABLE = 1  # 1 — табличный режим, 0 — обычный режим


def text_stat(text: str) -> None:
    """Вывести статистику слов для переданного текста."""
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top = top_n(freq)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    if TABLE:
        width = max((len(word) for word, _ in top), default=0)
        width = max(width, len("Слово"))
        print("Слово" + " " * (width - len("Слово")) + " | частота")
        print("-" * (width + 11))
        for word, count in top:
            print(word + " " * (width - len(word)) + f" | {count}")
    else:
        for word, count in top:
            print(f"{word}:{count}")


text = input()
text_stat(text)
