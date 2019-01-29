import makeWords

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/make/<word>')
def show_make(word):
    # show the user profile for that user
    return repr(makeWords.wordToElems(word))

