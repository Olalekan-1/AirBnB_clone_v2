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


# Run the web application on 0.0.0.0:5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
