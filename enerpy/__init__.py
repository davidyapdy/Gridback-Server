"""
enerpy
~~~~~~

Initialize D.E.E.P.'s energy app backend, which runs the API to progammatically
interact with EnergizeCT's free energy pricing data.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from config import ENERPY_APP_TOKEN, BASE_DIR
from enerpy.exceptions import InvalidRequestError


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


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
    models
)

