from stats import get_word_count
from stats import number_of_characters
from stats import sort_dictionary
import sys
books = {}

def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book> ")
        sys.exit(1)

        
    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOK BOT ============")
    print(f"Analyzing book found at books/{text}...")
    print("----------- Word Count -----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count ---------")
    for entry in number_of_characters(text):
        if entry["character"].isalpha():
            print(f"{entry["character"]}: {entry["count"]}")
    print("========== END ==========")
main()