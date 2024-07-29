#!/usr/bin/python3
"""This script starts a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)

@app.teardown_appcontext
def close_session(self):
	"""close current sqlalchemy session"""
	storage.close()

@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
	"""Displays a HTML page with list of states and cities in them"""
	states = storage.all(State).values()
	return render_template('8-cities_by_states.html', states=states)

if __name__ == "__main__":
	app.run(host='0.0.0.0', portt=5000)

