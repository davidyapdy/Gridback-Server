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

from flask import Flask


app = Flask(__name__)
app.config.from_object('config')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


from enerpy import (
    api,
    utils,
)
