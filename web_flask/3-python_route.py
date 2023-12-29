#!/usr/bin/python3

"""
 Starts a new flask application
 """

from flask import Flask


# Create a Flask web application
app = Flask(__name__)


# Define a route for the root URL
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<string:text>', strict_slashes=False)
def c_is_fun(text):
    modify = text.replace('_', ' ')
    return f'C {modify}'


@app.route('/python/<string:text>/', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_is_cool(text='is cool'):
    modify = text.replace('_', ' ')
    return f'Python {modify}'


# Run the web application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
