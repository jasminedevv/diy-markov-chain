'''
Options:
1. make the list index the number of instances? but what if there are multiple words with the same number of instances? List of words at the index? that adds another list traversal.
2. probably make the highest instance word to easiest to find
3. list of lists or list of tuples? Tuple of lists? What are the benefits of immutability here? If I have to switch them around anyway does it make sense to use tuples?

Histogram Function:
has to go through the whole corpus 1 word at a time. Can we avoid this?
can we compress all the words down to a number and then search through the list that matches the number? Wait but why?

The obvious way:
have a dict where the key is the word and the value is the number
for each word in corpus:
    try:
        increment the value of the word key
    except KeyError:
        add the element to the dict with value 1
 
The weird way:
make a list of tuples that looks like [('the', 67), ('a', 68), ... , ("Guadeloupe", 1)]
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


def hist(wordlist):
    '''
        Takes a list of words and return a histogram in the form of a dict.
    '''
    hist = dict()
    for word in wordlist:
        try:
            hist[word] += 1
        except KeyError:
            hist[word] = 1
    return hist

def swap_elements_in_list(my_list, j, k):
    my_list[j], my_list[k] = my_list[k], my_list[j]

def check_list_of_tuples_for_word(my_list, word):
    '''
        Should return True or False, swaps the positions of two elements sometimes
    '''
    for i, (word_out, count) in enumerate(hist):
            # print("Iterator: "+str(i), "word out: "+word_out, "count: "+str(count))
            # print(word_in, word_out)
            # print(word_in, word_out)
            if word_out == word:
                # print("word in was equal to word out")  
                count += 1
                # print(count, "<-- should be more than one")
                prev = my_list[i-1]
                # count is the current selected element, prev is the one before it in the list
                print(count, prev[1])
                if count > prev[1]:
                    # print("swapping them")
                    # swap them
                    swap_elements_in_list(my_list, i, i-1)
                return True
            return False
            # if it didn't find the word

def tuple_hist(wordlist):
    hist = []
    # iterates through the word list
    for word_in in wordlist:
        # print("checking word:", word_in)
        # iterates through the histogram for each word in the wordlist
        did_find_word = check_list_of_tuples_for_word(hist, word_in)
        if not did_find_word:
            new_element = (word_in, 1)
            print("appending:", new_element)
            hist.append( new_element )
    return hist 
            

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
    print(tuple_hist(corpus))
    # print(corpus)
    # my_hist = Histogram(corpus)
    # print(my_hist)