#!/usr/bin/python3
'''
This script that starts a Flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    '''hello route'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''hbnb route'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''c route'''
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
