#!/usr/bin/python3
"""This script starts a flask web appliciation"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_session(self):
	"""close the current sqlalchemy session"""
	storage.close()

@app.route('/states_list', strict_slashes=False)
def show_states():
	"""lists the states"""
	states = storage.all(State).values()
	sort_states = sorted(states, key=lambda k: k.name)
	return render_template('7-states_list.html', states=sort_states)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
