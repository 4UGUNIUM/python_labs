"""Чистые функции для нормализации текста и подсчёта частот слов."""

import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Нормализовать регистр, ``ё`` и пробельные символы в тексте."""
    if not isinstance(text, str):
        raise TypeError("text должен быть строкой")
    result = text.casefold() if casefold else text.lower()
    if yo2e:
        result = result.replace("ё", "е")
    result = result.replace("\t", " ").replace("\r", " ").replace("\n", " ")
    return " ".join(result.split())


def tokenize(text: str) -> list[str]:
    r"""Вернуть слова по шаблону ``\w+(?:-\w+)*``."""
    if not isinstance(text, str):
        raise TypeError("text должен быть строкой")
    return re.findall(r"\w+(?:-\w+)*", text, flags=re.UNICODE)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Подсчитать, сколько раз встречается каждый токен."""
    if not isinstance(tokens, list):
        raise TypeError("tokens должен быть списком")
    if not all(isinstance(token, str) for token in tokens):
        raise TypeError("каждый токен должен быть строкой")
    result: dict[str, int] = {}
    for token in tokens:
        result[token] = result.get(token, 0) + 1
    return result


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Вернуть первые ``n`` пар по частоте и алфавиту слова."""
    if not isinstance(freq, dict):
        raise TypeError("freq должен быть словарём")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n должно быть неотрицательным целым числом")
    if not all(isinstance(word, str) and isinstance(count, int)
               for word, count in freq.items()):
        raise TypeError("слова должны быть строками, а частоты — целыми числами")
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))[:n]
