
def get_book_text(filepath):
    with open(filepath) as f:
        x = f.read()
    return x

def get_num_words():
    text = get_book_text("books/frankenstein.txt")
    length = text.split()
    print(f"{len(length)} words found in the document")
    