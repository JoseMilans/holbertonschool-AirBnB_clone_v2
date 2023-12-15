#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/states_list')
def states_list():
    """
    Display a HTML page with a list of all State objects present in DBStorage
    sorted by name
    """
    from models.state import State
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
