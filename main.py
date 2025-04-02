import sys
from stats import get_book_text, get_num_chars, get_num_words, word_count

def main():
     
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    count = get_num_chars(text)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")

    count_list = word_count(count)

    for words in count_list:
        print(f"{words[0]}: {words[1]}")
    print("============= END ===============")
    
main()