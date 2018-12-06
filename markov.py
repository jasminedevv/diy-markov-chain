from sys import argv

from dictogram import Dictogram

import random

# Generate a dictionary of histograms

# get a dict of every word in the corpus where the key is the word and the value is an empty histogram

# loop through the list and make a histogram of every word that comes after it

class MarkovModel(dict):
    def __init__(self, word_list):
        super(MarkovModel, self).__init__()
        # self = dict()
        for i in range(0, len(word_list)-1):
            word = word_list[i]
            next_word = word_list[i + 1]
            try:
                self[word].add_count(next_word)
            except KeyError:
                self[word] = Dictogram(next_word)

def main():
    import sys
    arguments = sys.argv[1:]  # Exclude script name in first argument

    # Test histogram on letters in a word
    word = 'abracadabra'
    abra = list(word)
    print(abra)
    model = MarkovModel(abra)
    print(model)


if __name__ == '__main__':
    main()