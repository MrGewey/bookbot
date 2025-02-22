from stats import count_words
from stats import count_all
from stats import report
def main():
    #Type in the book. It will convert to lowercase, and check the books/ directory for the book.
    '''which_book: str = input("Enter the Book's name: ")
    path: str = f"books/{which_book.lower()}.txt"

    #j
    with open(path) as f:
        file_contents = f.read()
        print(len(file_contents.split()))
    return file_contents'''
    

    #print(f"{count_words()} words found in the document")
    #print(count_all())
    print(report())


main()