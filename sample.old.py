'''
    Pick a random word from a histogram
'''

from listogram import Listogram
from sys import argv

# using fang's sampler so I can move forward while I write my own https://github.com/MakeFang/TweetGen/blob/master/tut_5/sample.py
from fang_sample import cumulative_dist, binary_search, sample

# corp_file = open(argv[1]).read()
# corpus = corp_file.split(" ")

# hist = Listogram(corpus)

'''
    Final structure looks like a list of tuples
'''

class Histogram(Listogram):
    def __init__(self, word_list=None):
        super(Histogram, self).__init__(word_list)
        ''' 
            self should be a listogram in format [(word, count) sorted by ascending order of count 
        '''
        print("I just initialized myself: ", self)
        highest_word_count = self[-1][1]
        histogram = [None]
        new_range_start = 0
        '''
            Rearranges the sorted listogram into lists that contain all the words of the same count with None spaces where there were no words of a specific count.
        '''
        for index in range(highest_word_count):
            for range_end, (word, count) in self[:new_range_start]:
                if count is index:
                    histogram[index] = histogram[index].append(word)
                else:
                    new_range_start = range_end
                    break
        print("I look like:", self)
        print(histogram)

def test_me():
    corpus = ['one', 'fish', 'two', 'fish', 'red', 'fish', 'blue', 'fish']
    histogram = Listogram(corpus)

    histogram.cumulative = cumulative_dist(histogram)

    for _ in range(8):
        print(sample(histogram.cumulative))

if __name__ == '__main__':
    test_me()
 