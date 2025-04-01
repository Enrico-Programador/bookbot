
def get_book_text(filepath):
    with open(filepath) as f:
        x = f.read()
    return x

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    length = text.split()
    print(f"Found {len(length)} total words")

def get_num_chars():

    count = {}
    text = get_book_text("books/frankenstein.txt").lower()

    for letters in text:

        try:
            if letters in count:
                count[letters] = count[letters] + 1
            else:
                count[letters] = 1

        except Exception as e:
            pass

    return count


def word_count():
    
    count = get_num_chars()

    return print(count)

            #python3 main.py