#!/usr/bin/python3
"""This module starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Displays a HTML page with the states, cities and amenities"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
