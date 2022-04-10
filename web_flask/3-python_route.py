#!/usr/bin/python3
"""
    HBNB
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ index function """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ hbnb route """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cis(text):
    """ c with extra pramas """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py(text='is cool'):
    """ route with default value"""
    return 'python ' + text.replace('_', " ")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
