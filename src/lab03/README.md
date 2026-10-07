# Лабораторная работа №3 — тексты и частоты слов

Цель работы — нормализовать текст, выделить слова, посчитать частоты
словарём и вывести топ-N. Используется только стандартная библиотека Python.

## Структура

```text
src/lib/text.py             # normalize, tokenize, count_freq, top_n
src/lab03/text_stats.py     # программа со stdin
src/lab03/README.md          # отчёт
images/lab03/img01.png ...  # скриншоты проверок
```

## Задание A — `src/lib/text.py`

Реализованы функции:

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str
def tokenize(text: str) -> list[str]
def count_freq(tokens: list[str]) -> dict[str, int]
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]
```

### Полный код `src/lib/text.py`

```python
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

    Comtext = " ".join(Comtext.split())
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

    result = {}
    for word in tokens:
        result[word] = tokens.count(word)
    return result


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict):
        raise TypeError("Ожидался словарь частот")
    if not freq:
        raise ValueError("Словарь частот пуст")
    if n <= 0:
        raise ValueError("Количество слов должно быть больше нуля")

    result = list(freq.items())
    result.sort(key=lambda item: (-item[1], item[0]))
    return result[:n]
```

`normalize` применяет `casefold()` (или `lower()`), заменяет `ё` на `е`,
превращает `\\t`, `\\r`, `\\n` в пробелы, схлопывает пробелы и обрезает края.
`tokenize` использует шаблон `\\w+(?:-\\w+)*`: цифры и подчёркивания
считаются частью слова, дефис разрешён внутри слова. `top_n` сортирует пары
по ключу `(-частота, слово)`.

### Проверки

```python
from src.lib.text import count_freq, normalize, tokenize, top_n

assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\r\nWorld") == "hello world"
assert tokenize("по-настоящему foo_bar 2025 😀") == [
    "по-настоящему", "foo_bar", "2025"
]
assert count_freq(["a", "b", "a", "c", "b", "a"]) == {
    "a": 3, "b": 2, "c": 1
}
assert top_n({"bb": 2, "aa": 2, "cc": 1}, 2) == [
    ("aa", 2), ("bb", 2)
]
```

Результаты проверок:

![Проверка normalize](../../images/lab03/img01.png)

![Проверка tokenize](../../images/lab03/img02.png)

![Проверка count_freq](../../images/lab03/img03.png)

![Проверка top_n](../../images/lab03/img04.png)

## Задание B — `src/lab03/text_stats.py`

### Полный код `src/lab03/text_stats.py`

```python
from src.lib.text import normalize, tokenize, top_n, count_freq

TABLE = 1


def text_stat(text: str):
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top = top_n(freq)

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    if TABLE:
        max_word_len = max(
            max((len(word) for word, _ in top), default=0),
            len("Слово"),
        )
        print("Слово" + " " * (max_word_len - len("Слово")) + " | частота")
        print("-" * (max_word_len + 11))
        for word, count in top:
            print(word + " " * (max_word_len - len(word)) + f" | {count}")
    else:
        for word, count in top:
            print(f"{word}:{count}")


text = input()
text_stat(text)
```

Программа читает одну строку из stdin, нормализует текст и печатает:

```text
Всего слов: <N>
Уникальных слов: <K>
Топ-5:
слово:количество
```

Запуск из корня проекта:

```powershell
"Привет, мир! Привет!!!" | python -m src.lab03.text_stats
```

Результат:

```text
Всего слов: 3
Уникальных слов: 2
Топ-5:
Слово  | частота
----------------
привет | 2
мир    | 1
```

Табличный режим включается константой:

```python
TABLE = 1
```

Если установить `TABLE = 0`, программа выводит строки в формате
`слово:количество`.

Скриншоты запуска:

![Обычный режим text_stats.py](../../images/lab03/img05.png)

![Табличный режим text_stats.py](../../images/lab03/img06.png)

## Вывод

Реализованы нормализация, токенизация с поддержкой дефисов,
подсчёт частот и детерминированная сортировка топа. Функции модуля не
выполняют ввод-вывод и могут использоваться в следующих лабораторных работах.
