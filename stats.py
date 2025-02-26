import sys
args = sys.argv
def count_words():
    with open(args[1]) as f:
        file_contents: str = f.read()
        word_count = (len(file_contents.split()))
        return word_count

def count_all():
    total = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 
        'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0
        }
    with open(args[1]) as book:
        booky: str = book.read()
        lower_book: str = booky.lower()
        words: str = lower_book.split()
        for word in words:
            for character in word:
                if character in total:
                    total[character] += 1
                else:
                    1 == 1
    return total

def report():

    tally = count_all()
    
    sorted_tally = sorted(tally.items(), key = lambda x:x[1], reverse = True)
    converted_dict = dict(sorted_tally)
    
       
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {args[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words()} total words")
    print("--------- Character Count -------")
    for letter in converted_dict:
        print(f"{letter}: {converted_dict[letter]}")
    print("============= END ===============")