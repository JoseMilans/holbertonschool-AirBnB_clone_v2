#!/usr/bin/python3
"""This module starts a Flask web application with two routes
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Function that displays 'Hello HBNB!' at the root URL
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Displays 'HBNB' at the /hbnb URL"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
