'''
Architecture answers
Key features of the application:
1. the histogram generator
2. the stochastic sampler
3. the flask app

I think the file names are accurate

There are no global variables.

I think my functions are small enough.
Some of them have minor side effects but these are required and manageable

I do not have any functions here that are not methods of a class.

Files can be used as modules and scripts too.

Modules are all pretty independent.

'''

# import cleanup
# import tokenize
# import word_count
# import sample
# import sentence

# define some functions that compose the above modules

from flask import Flask, render_template, request
app = Flask(__name__)
import os

from markov import MarkovModel

def butcher_word(word):
    butchered = list(word)
    butchered = ["START"] + butchered + ["END"]
    model = MarkovModel(butchered)
    new_word = model.random_walk()
    return "".join(new_word[:-1])

def butcher_sentence(sentence):
    sentence = sentence.split(" ")
    new_sentence = []
    for word in sentence:
        butchered_word = butcher_word(word)
        new_sentence.append(butchered_word)
    return " ".join(new_sentence)

# app.histogram = Dictogram(list)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/butcher-word/<word>')
def try_very_hard(word):
    return butcher_word(word)

@app.route('/butcher-sentence', methods=['GET', 'POST'])
def butcher():
    if request.method == 'POST':
        print("posted")
        text = request.form['text']
        sentence = butcher_sentence(text)
        return sentence
    else:
        return render_template('form.html')

def show_form():
    return form.html

# if __name__ == '__main__':
    # code to run when file is executed 