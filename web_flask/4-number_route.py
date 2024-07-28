#!/usr/bin/python3
"""This module starts a flask web application"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def display_hbnb():
        """what happens when u type slash"""
        return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def display_plain_hbnb():
        """what happens when you type /hbnb"""
        return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
        """what happens when you type /c/text"""
        return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_py(text="is cool"):
        """returns python followed by the text"""
        return "Python {}".format(text.replace('_', ' '))

@app.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
	"""displays an accompanying text only if it is an int"""
	 return "{} is a number".format(n)


if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
