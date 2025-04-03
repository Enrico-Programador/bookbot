
def get_book_text(filepath):
    with open(filepath) as f:
        x = f.read()
    return x

def get_num_words(text):
    
    length = text.split()
    return print(f"Found {len(length)} total words")

def get_num_chars(text):

    count = {}

    for letters in text:
        lowered = letters.lower()
        if lowered in count:
            count[lowered] = count[lowered] + 1
        else:
            count[lowered] = 1

    return count


def word_count(count):

    count_list = []

    for words in count:
        to_append = []
        if words.isalpha() == True:
            to_append.append(words)
            to_append.append(count[words])
            count_list.append(to_append)

    count_list.sort(reverse=True, key=lambda x: x[1])
    return count_list
