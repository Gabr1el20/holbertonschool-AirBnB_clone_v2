#!/usr/bin/python3
from models import storage
from models.state import State
from flask import Flask, render_template
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def app_teardown_appcontext(self):
    """method to remove
    the current SQLAlchemy session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def filters():
    """Display a HTML page like
    6-index.html
    """
    return render_template("10-hbnb_filters.html",
                           states=storage.all(State).values(),
                           amenities=storage.all(Amenity).values())


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
