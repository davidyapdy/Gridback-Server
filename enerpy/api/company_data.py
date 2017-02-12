import json

from enerpy import app
from enerpy.utils import energizect


@app.route('/')
def index():
    """

    :return: JSON dump representation of the company data.
    """
    return json.dumps(energizect.get_prices())
