"""
api/providers.py
~~~~~~~~~~~~~~~~

API routes for obtaining company data.

:author: Sean Pianka
:github: @seanpianka
:e-mail: pianka@eml.cc

"""
import json

from gridback import app, db, models


@app.route('/prices/')
def prices():
    """

    :return: JSON dump representation of the company data.
    """
    default_state = 'CT'


    providers = models.Provider.query.all()


    return json.dumps(providers)

