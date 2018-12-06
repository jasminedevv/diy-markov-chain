from sys import argv

from dictogram import Dictogram


# Generate a dictionary of histograms

# get a dict of every word in the corpus where the key is the word and the value is an empty histogram

# loop through the list and make a histogram of every word that comes after it

class MarkovModel(dict):
    '''
        A list of Dictograms. Use the random_walk() function to generate random sentences.
    '''
    def __init__(self, word_list):
        super(MarkovModel, self).__init__()
        # self = dict()
        for i in range(0, len(word_list)-1):
            # print("window:", word_list[i], word_list[i + 1])
            word = word_list[i]
            next_word = word_list[i + 1]
            try:
                # print(word)
                self[word].add_count(next_word)
            except KeyError:
                # print(word)
                self[word] = Dictogram([next_word])
                # print(self[word])

    def random_walk(self):
        '''
            Requires sentences start with 0 and end with 1
        '''
        sentence = list()
        word = "START"
        while word is not "END":
            # print("word:", word)
            # pulls a random word out of a histogram
            next_word = self[word].random_word()
            sentence.append(next_word)
            # print("next word:", next_word)
            word = next_word
        return sentence

        
def main():
    # import sys
    # arguments = sys.argv[1:]  # Exclude script name in first argument

    # Test histogram on letters in a word
    word = 'abracadabra'
    abra = list(word)
    abra = ["START"] + abra + ["END"]
    print(abra)
    model = MarkovModel(abra)
    sentence = model.random_walk()
    print("".join(sentence[:-1]))

    fish_text = 'one fish two fish red fish blue fish'
    fish_text = ["START"] + fish_text.split(" ") + ["END"]
    # print(fish_text)
    fish = MarkovModel(fish_text)
    # print(fish)
    seusse = fish.random_walk()
    print(" ".join(seusse[:-1]))



if __name__ == '__main__':
    main()