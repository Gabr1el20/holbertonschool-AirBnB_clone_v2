#!/usr/bin/python3
"Task 9. Script that starts a web Application"
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """Remove the current
    SQLAlchemy session"""
    storage.close()


@app.route("/states", strict_slashes=False)
def states():
    """Generate a list of all the states"""
    return render_template("9-states.html",
                           states=storage.all(State).values())


@app.route("/states/<string:id>", strict_slashes=False)
def states_id(id):
    """ Display the list of states, and
    their cities if the id is displayed"""
    for s in storage.all(State).values():
        if s.id == id:
            return render_template("9-states.html", id=id,
                                   state=s, status='id')
    return render_template("9-states.html", states=s, status='none')


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
