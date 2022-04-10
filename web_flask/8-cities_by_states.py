#!/usr/bin/python3
""" list state """

from flask import Flask, render_template
from models import storage, state
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_all():
    return render_template('7-states_list.html', states=storage.all(state.State))


@app.route('/cities_by_states', strict_slashes=False)
def state_cities():
    return render_template('8-cities_by_states.html', states=storage.all(state.State))


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0")
