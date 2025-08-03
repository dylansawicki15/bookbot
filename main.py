from stats import count_words, count_characters, map_character_dict
import sys
def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    relative_path_to_book = sys.argv[1]
    book_text = get_book_text(relative_path_to_book)
    num_words = count_words(book_text)
    char_counts = count_characters(book_text)
    map_char_dict = map_character_dict(char_counts)
    sorted_map_char_dict = sorted(map_char_dict, key=lambda x: x["num"], reverse=True)

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {relative_path_to_book}
    ----------- Word Count ----------
    Found {num_words} total words    
    """)

    for char in sorted_map_char_dict:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print("""
    ============= END ===============
    """)