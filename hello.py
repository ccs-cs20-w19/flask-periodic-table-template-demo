import makeWords

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route('/make/<word>')
def show_make(word):
    return repr(makeWords.wordToElems(word))

