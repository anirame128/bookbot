import sys
from stats import get_num_words, get_num_char, sort_dictionary

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(get_book_text(sys.argv[1]))
    num_chars = get_num_char(get_book_text(sys.argv[1]))
    sorted_dictionary = sort_dictionary(num_chars)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_dictionary:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()
