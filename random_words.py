import random

# reformat this to only need to open the file once
def get_word(wordlist):
    '''
    Returns a random word from the wordlist excluding contractions. 
    '''
    word = random.choice(wordlist)
    # prevents it from grabbing words with single quotes in them
    while '\'' in word:
        word = random.choice(words)
    return word

def get_words(num, wordlist):
    '''
        Takes an int.
        Returns that number of words from the system dictionary.
    '''
    words = []
    for _ in range(num):
        word = get_word(wordlist)
        words.append(word)
    return words

if __name__ == "__main__":
    from sys import argv
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    my_words = get_words(int( argv[1] ), words)
    print(" ".join(my_words))