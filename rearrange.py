# rearranges words given from argv
import random

def shuffle(words):
    ''' Takes: a list (words)
        For each string in the list put it at a random index in a new list
        Returns: the new list which is just the original list in a different order. '''
    length = len(words)
    new_order = []
    for word in words:
        # print("word is: " + str(word))
        index = random.randint(0,length)
        # print("index is: " + str(index))
        new_order.insert(index, word)
        # print("new order is: " + str(new_order))
    return new_order

if __name__ == "__main__":
    from sys import argv

    print(" ".join(shuffle(argv[1:])))