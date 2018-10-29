import random

# reformat this to only need to open the file once
def get_word():
    ''' Returns a random word from the system dictionary excluding contractions. '''

    word_file = "/usr/share/dict/words"
    words = open(word_file).readlines()
    word = random.choice(words)
    # prevents it from grabbing words with single quotes in them
    while '\'' in word:
        word = random.choice(words)
    return word

def get_words(num):
    '''
        Takes an int.
        Returns that number of words from the system dictionary.
    '''
    words = []
    for _ in range(num):
        word = get_word()
        words.append(word)
    return words

if __name__ == "__main__":
    from sys import argv

    my_words = get_words(int( argv[1] ))
    print(" ".join(my_words))