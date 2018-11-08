# import cleanup
# import tokenize
# import word_count
# import sample
# import sentence

# define some functions that compose the above modules

from flask import Flask
app = Flask(__name__)
import os

@app.route('/')
def hello_world():
    return 'Hello, World!'

# if __name__ == '__main__':
    # code to run when file is executed 