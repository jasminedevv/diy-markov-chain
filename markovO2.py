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
        self.first_word = word_list[1]
        self["START"] = Dictogram()
        self["START"].add_count(word_list[1])
        for i in range(0, len(word_list)-2):
            # print("window:", word_list[i], word_list[i + 1])
            word1 = word_list[i]
            word2 = word_list[i+1]
            item = (word1, word2)
            next_word = word_list[i + 2]
            try:
                # print(word)
                self[item].add_count(next_word)
            except KeyError:
                # print(word)
                self[item] = Dictogram([next_word])
                # print(self[word])

    def random_walk(self):
        '''
            Requires sentences start with START and end with END
        '''
        sentence = list()
        first_word = self['START'].random_word()
        item = ('START', first_word)
        sentence.append(item[1])
        while 'END' not in item:
            # print("word:", word)
            prev_word = item[1]
            # pulls a random word out of a histogram
            next_word = self[item].random_word()
            # print("next word:", next_word)
            item = (prev_word, next_word)
            sentence.append(next_word)
        return sentence

        
def main():
    # import sys
    # arguments = sys.argv[1:]  # Exclude script name in first argument

    # Test histogram on letters in a word
    word = 'abracadabra'
    abra = list(word)
    abra = ["START"] + abra + ["END"]
    # print(abra)
    model = MarkovModel(abra)
    # print(model)
    # print('\n')
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