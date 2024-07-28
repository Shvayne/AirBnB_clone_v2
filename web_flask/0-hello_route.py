#!/usr/bin/python3
"""this is a module that starts a flask web app"""  
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
	"""what to do when a slash is encountered"""
	return "Hello HBNB!"


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
