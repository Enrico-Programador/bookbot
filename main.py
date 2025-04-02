from stats import get_num_words, word_count

def main():
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    get_num_words()
    print("--------- Character Count -------")
    count_list = word_count()
    for words in count_list:
        print(f"{words[0]}: {words[1]}")
    print("============= END ===============")
    
main()