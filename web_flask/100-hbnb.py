#!/usr/bin/python3
"""Script that starts a Flask web application"""

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from flask import Flask, render_template@app.route("/hbnb", strict_slashes=False)

def hbnb():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    places = storage.all("Place")
    return render_template("100-hbnb.html", states=states, amenities=amenities, places=places)

@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
