import sys

from stats import (
    counting_words,
    counting_characters,
    chars_dict_to_sorted_list,
)

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    
    chars_dict = counting_characters(text)
    sorted_chars = chars_dict_to_sorted_list(chars_dict)
    print(counting_words(text))
    print(sorted_chars)
    

main()





    