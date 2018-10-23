# rearranges words given from argv
import random
from sys import argv

def rearrange(words):
    length = len(words)
    new_order = []
    for word in words:
        index = random.randint(0,length)
        new_order.insert(index, word)
    return new_order

print(" ".join(rearrange(argv[1:])))