"""This script generates random words given the distribution.
This generating process is done through probability integral transform. It is
acheived through sampling from uniform distribution and solving for the inverse
under its cumulative distribution function. Currently one sampling function
takes 1e-5 seconds on my mac.
"""


import random
import math

def cumulative_dist(histogram):
    """Compute the cumulative occurance given histogram."""
    cumulative = []
    sum = 0
    for word_index, word_tuple in enumerate(histogram):
        sum += word_tuple[1]
        cumulative.append((word_tuple[0], sum))
    return cumulative


def binary_search(cumulative, target):
    """Search throught the list to find target.
    If target is not found,returns the next indexself.
    """
    left = 0
    right = len(cumulative) - 1
    while left < right:
        middle = math.floor((left + right)/2)
        if cumulative[middle][1] == target:
            return middle
        elif cumulative[middle][1] < target:
            left = middle+1
        elif cumulative[middle][1] > target:
            right = middle-1
    return left if target <= cumulative[left][1] else left+1


def sample(cumulative):
    """Generate sample from the distribution."""
    totals = cumulative[-1][1]
    random_int = random.randint(1, totals)
    return cumulative[binary_search(cumulative, random_int)][0]


def read_hist():
    """Read the histogram from a txt file."""
    hist = []
    with open('MD_hist.txt', 'r') as f:
        for i in f:
            hist_entry = i.split()
            hist.append((hist_entry[0], int(hist_entry[1])))
    return hist
 

if __name__ == '__main__':
    my_hist = [('fish', 4), ('one', 1), ('two', 1), ('red', 1), ('blue', 1)]
    cd = cumulative_dist(my_hist)
    for i in range(8):
        print(sample(cd))
  