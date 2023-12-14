#!/usr/bin/python3
"""
This module starts a Flask web application with multiple routes
and a number template route
"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>')
def is_number(n):
    """Displays 'n is a number' only if n is an integer
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def num_template(n):
    """Displays an HTML template with the number
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def num_odd_or_even(n):
    """Displays a template with <n> value and whether it's even or odd
    """
    return render_template('6-number_odd_or_even.html',
                           num=n, is_even=(n % 2 == 0))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
