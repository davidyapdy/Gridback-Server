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

from config import GRIDBACK_APP_TOKEN, BASE_DIR
from gridback.exceptions import InvalidRequestError


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


@app.before_request
def before_request():
    app_token = request.args.get('app_token')
    if not app_token:
        raise InvalidRequestError("No app token provided.")
    elif app_token != GRIDBACK_APP_TOKEN:
        raise InvalidRequestError("Invalid app token provided.")


from gridback import (
    api,
    utils,
    exceptions,
    models
)

# backgroundscheduler.start here, seconds=1800, store energizect api call in db
# hopefully no issues with race conditions/locking
