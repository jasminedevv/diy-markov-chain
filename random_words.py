from sys import argv
import random

def get_word():
    word_file = "/usr/share/dict/words"
    words = open(word_file).read().splitlines()
    word = random.choice(words)
    # prevents it from grabbing words with single quotes in them
    while '\'' in word:
        word = random.choice(words)
    return word

def get_words(num):
    words = []
    for i in range(0, num):
        word = get_word()
        words.append(word)
    return words

my_words = get_words(int( argv[1] ))
print(" ".join(my_words))