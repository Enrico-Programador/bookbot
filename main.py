from stats import get_num_words, word_count

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    word_count()
    
main()