from stats import get_num_words, get_char_count, sort_dictionary
import sys
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    num_words = get_num_words(get_book_text(sys.argv[1]))
    char_count = get_char_count(get_book_text(sys.argv[1]))
    sorted_counts = sort_dictionary(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char, count in sorted_counts:
        if char.isalpha():
            print(f"{char}: {count}")
        else:
            pass
    print("============= END ===============")
main()