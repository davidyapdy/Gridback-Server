"""
api/__init__.py
~~~~~~~~~~~~~~~

API definition for Gridback backend.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
from gridback import db, models
from gridback.api import (
    providers,
    states
)


def update_all_state_data():
    for state, api in states.apis.items():
        print_log("Updating \"{}\" data...".format(state))


        data = api()
        for provider in data:
            provider = models.Provider(
                None,
                provider.get('name'),
                provider.get('phone_number'),
                provider.get('cycle'),
                provider.get('supply_rate'),
                provider.get('pricing_model'),
                provider.get('renewable'),
                provider.get('img'),
                provider.get('enrollment'),
                provider.get('cancellation'),
            )
            db.session.add(provider)
            db.session.commit()


        print_log("Completed update.".format(state))
