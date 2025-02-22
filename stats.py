

def count_all():
    total = {}
    i = 0
    with open("books/frankenstein.txt") as book:
        booky: str = book.read()
        lower_book: str = booky.lower()
        words: str = lower_book.split()
        for word in words:
            split_words = word.split()
            for character in split_words:
                slice_word = character[:]
                print(slice_word)