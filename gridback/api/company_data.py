"""
company_data
~~~~~~~~~~~~

:author: Sean Pianka
:github: @seanpianka
:e-mail: pianka@eml.cc

"""
import json

from gridback import app, db, models
from gridback.utils import energizect


@app.route('/prices/')
def prices():
    """

    :return: JSON dump representation of the company data.
    """
    providers = models.Provider.query.all()

    if not providers:
        providers = energizect.get_prices()

    return json.dumps(providers)

