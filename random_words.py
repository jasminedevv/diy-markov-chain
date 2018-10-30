import random
from sys import argv

def get_word(wordlist):
    '''
        Returns a random word from wordlist
    '''
    return random.choice(wordlist)
    
def get_words(num, wordlist):
    '''
        Returns num number of words from the wordlist
    '''
    words = list()
    for _ in range(num):
        word = get_word(wordlist)
        words.append(word)
    return words

if __name__ == "__main__":
    with open("/usr/share/dict/words") as words:
        words = words.read().splitlines()
        my_words = get_words(int( argv[1] ), words)
        print(" ".join(my_words))