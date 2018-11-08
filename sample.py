from dictogram import Dictogram
from sys import argv

corp_file = open(argv[1]).read()
corpus = corp_file.split(" ")

hist = Dictogram(corpus)

def _set_cumulative_distribution(self):
    count_sum = 0
    for index, (_, count) in enumerate(self):
        count_sum += count
    self.cumulative_distribution = count_sum