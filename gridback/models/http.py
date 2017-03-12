"""
models/http.py
~~~~~~~~~~~~~~

Response and request model for Gridback.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
from datetime import datetime

from gridback import GRIDBACK_APP_TOKEN, models
from gridback.exceptions import InvalidRequestError


class BaseRequest:
    def __init__(self, app_token, email):
        """ Initialize a client request given parameters expected in request.

        :param app_token: identifying token sent by official client

        """
        self._timestamp = None
        self.timestamp = datetime.timestamp()

        self._app_token = None
        self.app_token = app_token

        # set through subsequent email validation
        self._person = None

        self._email = None
        self.email = email


    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, new_timestamp):
        self._timestamp = new_timestamp

    @property
    def app_token(self):
        return self._app_token

    @app_token.setter
    def app_token(self, new_app_token):
        if not new_app_token:
            raise InvalidRequestError('No app token.')
        if not Request._validate_app_token(new_app_token):
            raise InvalidRequestError('Invalid app token.')
        self._app_token = new_app_token

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        if not new_email:
            raise InvalidRequestError('No email provided.')
        self.person = models.Person.from_email(new_email)
        self._email = new_email

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, new_person):
        person_validators = all((
            isinstance(new_person, models.Person),
            models.Person.from_email(new_person.email) == new_person
        ))
        if not person_validators:
            raise InvalidRequestError('No person matches provided email.')
        self._person = new_person


    @staticmethod
    def _validate_app_token(app_token):
        return app_token and app_token == GRIDBACK_APP_TOKEN


class BaseResponse:
    def __init__(self):
        pass
