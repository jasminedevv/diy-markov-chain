'''
Options:
1. make the list index the number of instances? but what if there are multiple words with the same number of instances? List of words at the index? that adds another list traversal.
2. probably make the highest instance word to easiest to find
3. list of lists or list of tuples? Tuple of lists? What are the benefits of immutability here? If I have to switch them around anyway does it make sense to use tuples?

Histogram Function:
has to go through the whole corpus 1 word at a time. Can we avoid this?
can we compress all the words down to a number and then search through the list that matches the number? Wait but why?

The obvious way:
make a list of lists that looks like [['the', 67], ['a', 68]]
iterate through all the words in the corpus
for each word check the list:
    check hist[i[0]]
    If found increment the number index
        check the number of the element next to it and swap their positions if the current item now has more words
        the most frequent word should be at the beginning
        this makes sense because the most common word will appear twice as often and the second most common word
    else add it to the end of the list with [word, 1]

The slightly less obvious way:
sort the list
count each instance
'''

class Histogram(list):
    # is there a way to make this not O(n2)?
    def __init__(self, corpus):
        '''
        corpus should be a string
        hist should be a list
        returns a histogram
        '''
        # a list of lists with two members each
        self.hist = [["fish", 1]]
        # a list of strings
        self.corpus = corpus
        print(self.corpus) 
        # length of the corpus
        self.corp_len = len(corpus)
        for i in range(self.corp_len):
            print("Checking index in corpus:", i)
            search_result = self._search(self.corpus[i])
            if search_result is False:
                new_count = [self.corpus[i], 1]
                print("Adding:", new_count)
                self.hist.append(new_count)
            else:
                self.hist[i][1] += 1
    def _compare_and_swap(self, index):
        if self.hist[index][1] > self.hist[index - 1][1]:
            self.hist[index] = self.hist[index - 1]
                
    def _search(self, word):
        '''
        Traverses the histogram and returns the index if it finds a match
        '''
        print("Searching for:", word)
        # needs to traverse the HISTOGRAM not the corpus
        for i in range(len(self)):
            if self.hist[i] is word:
                print(self.hist[i])
                return i
        # returns false if word not found
        print("Did not find it.")
        return False

if __name__ == "__main__":
    corp_file = "fish.txt"
    corpus = open(corp_file).read()
    print(corpus)
    corpus = corpus.split()
    print(corpus)
    my_hist = Histogram(corpus)
    print(my_hist)