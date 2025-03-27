def get_book_text(filepath):
    with open(filepath) as f:
        x = f.read()
    return x


def main():
    text = get_book_text("books/frankenstein.txt")
    text = "family johnson baby"
    length = text.split()
    print(f"{len(length)} words found in the document")
    
main()