#!/usr/bin/python3
""" 
    list all states
    list all  cities by states
"""


from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    return render_template('9-states.html', states=storage.all(State))


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id=None):
    key = 'State.' + str(id)
    if key in storage.all(State):
        state = storage.all()[key]
    else:
        state = None
    return render_template('9-states.html', state=state)



@app.teardown_appcontext
def close_sql(reponse_or_exc):
    storage.close()


if __name__ == '__main__':
    app.run()
