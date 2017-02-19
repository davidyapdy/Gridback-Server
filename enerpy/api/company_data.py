"""
company_data
~~~~~~~~~~~~

:author: Sean Pianka
:github: @seanpianka
:e-mail: pianka@eml.cc

"""
import json

from enerpy import app, db, models
from enerpy.utils import energizect


@app.route('/prices/')
def prices():
    """

    :return: JSON dump representation of the company data.
    """
    companies = models.Company.query.all()

    if not companies:
        companies = energizect.get_prices()

    return json.dumps(companies)

