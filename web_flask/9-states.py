#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/states')
def states_list():
    """Display a HTML page with a list of all State objects"""
    states = storage.all(State).values()
    return render_template('9-states.html', obj_list=states)


@app.route('/states/<id>')
def state_cities(id):
    """Displays a HTML page with the cities of a certain State"""
    states = storage.all(State)
    state = next((state for state in states.values() if state.id == id), None)
    return render_template('9-states.html', state=state, id=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
