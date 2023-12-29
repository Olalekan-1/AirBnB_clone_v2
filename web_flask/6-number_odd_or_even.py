#!/usr/bin/python3

"""
 Starts a new flask application
 """

from flask import Flask
from flask import render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def ren_template(n):
    return render_template('5-number.html', var=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def ren_template1(n):
    return render_template('6-number_odd_or_even.html', var=n)


# Run the web application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
