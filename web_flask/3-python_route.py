#!/usr/bin/python3
"""
This module starts a Flask web application with multiple routes
"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Function that displays 'Hello HBNB!' at the root URL
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_hbnb():
    """Displays 'HBNB' at the /hbnb URL"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Displays 'C ' followed by text with underscores replaced by spaces
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Displays 'Python ' followed by text with spaces"""
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
