#!/usr/bin/python3
"""Script that starts a Flask web application"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/states', strict_slashes=False)
def states():
    """Displays a HTML page with the list of all State objects."""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states)

@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
