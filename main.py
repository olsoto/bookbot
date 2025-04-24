def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    return len(text.split())
    
def main():
    num_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"{num_words} words found in the document")
    return 0

main()