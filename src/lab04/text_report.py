from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lab04.io_txt_csv import read_text, write_csv
from pathlib import Path 
    
    
def text_report(path: str | Path, out: str | Path, encoding: str = "utf-8"):
    text = read_text(path, encoding=encoding)
    
    tokens = tokenize(normalize(text))
    freq = count_freq(tokens)
    top = top_n(freq)

    lib = list(freq.items())
    lib.sort(key = lambda x:(-x[1],x[0]))


    if not top:
        raise ValueError("Не удалось получить топ слов")

    print("Всего слов: ", len(tokens))
    print('Уникальных слов: ', len(set(tokens)))
    print('топ-5: ')
    for i in top:
        print(f"{i[0]}:{i[1]}")

    
    
    
    write_csv(lib, out, ["word", "count"])


    


print(text_report("src/data/lab04/input.txt", 'src/data/check.csv'))

