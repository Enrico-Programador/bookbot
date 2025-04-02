from stats import get_book_text, get_num_chars, get_num_words, word_count

def main():

    text = get_book_text("books/frankenstein.txt")
    count = get_num_chars(text)

    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")

    count_list = word_count(count)

    for words in count_list:
        print(f"{words[0]}: {words[1]}")
    print("============= END ===============")
    
main()