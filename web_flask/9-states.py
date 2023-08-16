#!/usr/bin/python3
"""Task 9. Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """After each request, remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Display a HTML page with the list of all States. Route ("/states")
    """
    return render_template("7-states_list.html",
                           states=storage.all(State).values())


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Display a HTML page of a specific state by id. Route ("/states/<id>")
    """
    return render_template("9-states.html",
                           states=storage.all(State).get(f'State.{id}'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)