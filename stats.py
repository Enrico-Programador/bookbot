
def get_book_text(filepath):
    with open(filepath) as f:
        x = f.read()
    return x

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    length = text.split()
    print(f"{len(length)} words found in the document")

def get_num_chars():
    count = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    text = get_book_text("books/frankenstein.txt").lower()
    print(text)
    for letters in text:

        try:
            if letters in count:
                count[letters] = count[letters] + 1

        except Exception as e:
            pass
        print(count)

            #python3 main.py