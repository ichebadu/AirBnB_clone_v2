#!/usr/bin/python3
"""This module contains a simple flask
server application. The flask server
listens on PORT 5000, 0.0.0.0

This server serves data from the storage engine
and renders it using jinja
"""

from flask import Flask, escape, render_template
from models import storage
import models
app = Flask(__name__)


@app.teardown_appcontext
def teardown(c):
    """Teardown function is called after each
    request

    This function is called after every request
    and it closes the current storage session
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def serve_hbng():
    """Route handler for states endpoint
    it responds with html template

    This endpoint serves data from the storage engine
    and renders it using jinja
    """

    states = list(storage.all(models.classes["State"]).values())
    amenities = list(storage.all(models.classes["Amenity"]).values())

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
