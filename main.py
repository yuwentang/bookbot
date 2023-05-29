
print("\033c")

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    words = count_words(text)
    letters = count_letters(words)
    print("--- Begin report of books/frankenstein.txt ---")
    make_report(words, letters)
    #print(report)
    #print(str(len(words))+" words found in the document")
    #print(letters)

def get_text(path):
    with open(path) as f:
        content = f.read()
    return content

def count_words(content):
    words = content.split()
    return words

def count_letters(words):
    letters = {}
    for word in words:
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                if letter in letters:
                    letters[letter] = letters[letter] + 1
                else:
                    letters[letter] = 1
    letters = sorted(letters.items(), key=lambda x:x[1], reverse=True)
    letters = dict(letters)
    return letters

def make_report(words, letters):
    print(str(len(words))+" words found in the document\n")
    for key in list(letters.keys()):
        print(f"The {key} character was found {letters[key]} times") 

main()

'''
path = "books/frankenstein.txt"

with open(path) as f:
    content = f.read()
    words = content.split()
    print(str(len(words))+" words found in the document")
'''

'''
to clean all the details of path
1. print("\033c")
2. from os import system
system("clear")

'''

'''
path = "books/frankenstein.txt"

with open(path) as f:
    print(f.read())


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
'''