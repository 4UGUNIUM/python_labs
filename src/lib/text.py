def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    Comtext = text
    if yo2e:
        Comtext = Comtext.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        Comtext = Comtext.casefold()

    Comtext = ' '.join(Comtext.split())
    return Comtext

# print(normalize("ПрИвЕт\nМИр\t"))# привет мир
# print(normalize("ёжик, Ёлка", yo2e=True))# ежик, елка
# print(normalize("Hello\r\nWorld"))# hello world
# print(normalize("  двойные   пробелы  "))# двойные пробелы

def tokenize(text: str) -> list[str]:
    Comtext = text
    Comtext = normalize(Comtext)
    result = ""
    count = 0

    for i in Comtext:
        if i.isalnum() or (
            (i == "-" or i == '_')
            and count > 0 and count + 1 < len(Comtext)
            and Comtext[count - 1].isalnum() and Comtext[count + 1].isalnum()
        ): result += i
        else:result += " "

        count += 1

    return result.split()

# print(tokenize("привет мир"))  # ["привет", "мир"]
# print(tokenize("hello,world!!!"))  # ["hello", "world"]
# print(tokenize("по-настоящему круто"))  # ["по-настоящему", "круто"]
# print(tokenize("2025 год"))  # ["2025", "год"]
# print(tokenize("emoji 😀 не слово"))  # ["emoji", "не", "слово"]

def count_freq(tokens: list[str]) -> dict[str, int]:
    t = tokens
    result = {}
    for words in t:
        result[words] = t.count(words)
    return result


# print(count_freq(["a", "b", "a", "c", "b", "a"]))  # {"a": 3, "b": 2, "c": 1}
# print(count_freq(["bb", "aa", "bb", "aa", "cc"]))  # {"aa": 2, "bb": 2, "cc": 1}

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    result = list(freq.items()) #.items - делает словарь парами(слово-колво)
    result.sort(key=lambda x: (-x[1], x[0]))
    return result[:n]

# print(top_n({"a": 3, "b": 2, "c": 1}, n=2))  # [('a', 3), ('b', 2)]
# print(top_n({"bb": 2, "aa": 2, "cc": 1}, n=2))  # [('aa', 2), ('bb', 2)]


