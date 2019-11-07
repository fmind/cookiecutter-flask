#!/usr/bin/env python3

"""Documentation of the app."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    """Welcome the web user."""
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
