#!/usr/bin/python3
'''
This script starts a Flask web application
'''

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_route():
    ''' states_list route'''

    results = storage.all(State)
    return render_template('7-states_list.html', states=results)


@app.teardown_appcontext
def close_session(exception=None):
    ''' shuts down the MySQL session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
