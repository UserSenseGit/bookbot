import sys
print(sys.argv)




from stats import counting_words

from stats import counting_characters

from stats import sorted_dictionaries


def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    char_count = counting_characters(text)
    sorted_chars = sorted_dictionaries(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(counting_words(text))
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============    ")
    

main()





    