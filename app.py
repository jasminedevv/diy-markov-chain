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

from flask import Flask
app = Flask(__name__)
import os

# app.histogram = Dictogram(list)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# if __name__ == '__main__':
    # code to run when file is executed 