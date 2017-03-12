"""
gridback/__init__.py
~~~~~~~~~~~~~~~~~~~~

Initialize Gridback server backend, which schedules API calls to a state's
energy-data provider.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy

from config import GRIDBACK_APP_TOKEN, BASE_DIR, DEBUG
from gridback.exceptions import InvalidRequestError


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


from gridback import (
    exceptions,
    utils,
    models,
    api,
)


@app.before_request
def before_request():
    g.request = models.BaseRequest(
        request.args.get('app_token'),
        request.args.get('email')
    )


# when production server starts, update all data
if not DEBUG:
    api.update_all_state_data()


scheduler = BackgroundScheduler()
scheduler.add_job(
    api.update_all_state_data,
    'interval',
    seconds=utils.constants.SCHEDULER_INTERVAL
)
scheduler.start()
