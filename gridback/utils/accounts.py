"""
accounts
~~~~~~~~

:author: Sean Pianka
:github: @seanpianka
:e-mail: pianka@eml.cc

"""
from flask import request

from gridback import app, db


@app.route('/add_account/')
def add_account():
    email = request.form.get('email')
