#!/usr/bin/python3
""" list state """

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_all():
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def teardown_appcontext(self):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
