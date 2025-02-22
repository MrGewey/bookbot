def main():
    #Type in the book. It will convert to lowercase, and check the books/ directory for the book.
    '''which_book: str = input("Enter the Book's name: ")
    path: str = f"books/{which_book.lower()}.txt"

    #j
    with open(path) as f:
        file_contents = f.read()
        print(len(file_contents.split()))
    return file_contents'''
    with open("books/frankenstein.txt") as f:
        file_contents: str = f.read()
        print(len(file_contents.split()))

#from stats import count_all

        

            



main()
#count_all()