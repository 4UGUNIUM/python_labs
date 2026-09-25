from src.lib.text import normalize, tokenize, top_n, count_freq

TABLE = 1 #Для включения режима таблички


def text_stat(text: str):
    t = text

    tokens = tokenize(normalize(t))
    freq = count_freq(tokens)
    top = top_n(freq)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    if TABLE:
        max_word_len = max( max((len(i[0]) for i in top), default=0), len("Слово") )

        print("Слово" + " " * (max_word_len - len("Слово")) + " | частота")
        print("-" * (max_word_len + 11))

        for i in top:
            print(i[0] + " " * (max_word_len - len(i[0])) + f" | {i[1]}")

    else:
        for i in top:
            print(f"{i[0]}:{i[1]}")

text = input()
text_stat(text)