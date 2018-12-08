from markov import MarkovModel
import re


def read_corpus(corpus):
    with open(corpus, 'r') as file:
        text = file.read()
    return text

def remove_chars(text, chars):
    for char in chars:
        text = text.replace(char, "")
    return text

def tokenize(corpus):
    # separate text into a list by space
    raw_text = read_corpus(corpus)
    raw_text.replace("\n", "END START")
    bad_chars = ["\"", "'", "(", ")",]
    raw_text = remove_chars(raw_text, "\"`()'`“")
    text = raw_text.split(" ")
    for i, word in enumerate(text):
        if '.' in word:
            text.insert(i+1, "END")
            text.insert(i+2, "START")
        '''
        if '\n' in text[i]:
            # print("word in question:", text[i])
            right = text[:i]
            # print("right:", right)
            # print(right)
            left = text[i:]
            # print("left:", left)
            words = word.split('\n')
            # print(word)
            # print("words:", words)
            # try:
            right.extend(words)
            # print(right)
            left.extend(right)
            text = left
            # except AttributeError:
            #     print(right)
            #     print(left)
            #     print("attr error")
        '''
    return text

def give_sentence():
    text = tokenize("corpus.txt")

    # re.sub(r'(?<=\n).*', 'START END', text)

    model = MarkovModel(text)

    sentence = model.random_walk()

    sentence = " ".join(sentence[:-1])

    # print()

    # (?<=\n).*

    re.sub(r'(?<=\n).*', '', sentence)
    new_sentence = ""
    
    sentence = sentence.split('\n')

    # print(sentence)

    if type(sentence) is list:
        return max(sentence, key=len)
    else:
        return sentence

give_sentence()