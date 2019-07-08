#!/usr/bin/env python3

"""Documentation of the app."""

from flask import Flask

APP = Flask(__name__)


@APP.route('/')
def hello():
    """Welcome the web user."""
    return 'Hello World!'


if __name__ == '__main__':
    APP.run()
