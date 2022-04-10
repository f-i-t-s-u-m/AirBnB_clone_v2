#!/usr/bin/python3
""" list states python file """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    if id is None:
        return render_template('9-states.html', states=storage.all(State))
    else:
        try:
            return render_template('9-states.html',
                                   state=storage.all()[f'State.{id}'])
        except KeyError:
            return render_template('9-states.html', state=None)


@app.teardown_appcontext
def teardown_appcontext(response_or_exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
