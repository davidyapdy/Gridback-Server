"""
utils/authentication.py
~~~~~~~~~~~~~~~~~~~~~~~

Authentication methods for e-mail addresses and database models.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
def validate_email(email):
    if not email:
        return False

    if 'gmail' in email.split('@')[1].lower():
        pass


