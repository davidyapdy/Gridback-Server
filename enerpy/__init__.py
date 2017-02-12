"""
enerpy
~~~~~~

Initialize D.E.E.P.'s energy app backend, which runs the API to progammatically
interact with EnergizeCT's free energy pricing data.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
import os

from flask import Flask, request, jsonify

from config import ENERPY_APP_TOKEN
from enerpy.exceptions import InvalidRequestError


app = Flask(__name__)
app.config.from_object('config')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code

    return response


@app.before_request
def before_request():
    app_token = request.args.get('app_token')
    if not app_token:
        raise InvalidRequestError("No app token provided.")
    elif app_token != ENERPY_APP_TOKEN:
        raise InvalidRequestError("Invalid app token provided.")



from enerpy import (
    api,
    utils,
    exceptions,
)
