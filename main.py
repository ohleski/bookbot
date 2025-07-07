import sys

from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book_text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    num_chars = get_num_chars(book_text)
    sorted_chars = sort_char_count(num_chars)
    sorted_list=sort_char_list_by_num(sorted_chars)
    for li in sorted_list:
        if li["char"].isalpha():
            print(f"{li["char"]}: {li["num"]}")

    print("============= END ===============")    

main()    