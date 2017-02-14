"""
company_data
~~~~~~~~~~~~

:author: Sean Pianka
:github: @seanpianka
:e-mail: pianka@eml.cc

"""
import json

from enerpy import app
from enerpy.utils import energizect


@app.route('/prices/')
def prices():
    """

    :return: JSON dump representation of the company data.
    """
    return json.dumps(energizect.get_prices())

