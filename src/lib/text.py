import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")

    if not text.strip():
        raise ValueError("Передан пустой текст")

    Comtext = text
    if yo2e:
        Comtext = Comtext.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        Comtext = Comtext.casefold()

    Comtext = ' '.join(Comtext.split())
    return Comtext


def tokenize(text: str) -> list[str]:

    if not isinstance(text, str):
        raise TypeError("Текст должен быть строкой")

    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:

    if not isinstance(tokens, list):
        raise TypeError("Ожидался список слов")

    if not tokens:
        raise ValueError("Список слов пуст")

    t = tokens
    result = {}
    for words in t:
        result[words] = t.count(words)
    return result


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    if not isinstance(freq, dict):
        raise TypeError("Ожидался словарь частот")

    if not freq:
        raise ValueError("Словарь частот пуст")

    if n <= 0:
        raise ValueError("Количество слов должно быть больше нуля")

    result = list(freq.items())
    result.sort(key=lambda x: (-x[1], x[0]))
    return result[:n]
