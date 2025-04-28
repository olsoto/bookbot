from stats import get_num_words
from stats import get_num_char_apps
from stats import get_sorted_dictionaries
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
       
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_url = sys.argv[1]
    num_words = get_num_words(get_book_text(book_url))
    dict = get_num_char_apps(get_book_text(book_url))
    dicts_list = get_sorted_dictionaries(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_url}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in dicts_list:
        char = dict["char"]
        num = dict["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")
    return 0

main()