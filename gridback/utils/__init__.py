"""
utils/__init__.py
~~~~~~~~~~~~~~~~~

Module containing utility functionality of the Gridback backend.

:author: Sean Pianka
:e-mail: pianka@eml.cc
:github: @seanpianka

"""
import datetime


def print_log(msg, *args, **kwargs):
    """ Provide a standard utility to log important information to the terminal,
    such as time information of an event.

    """
    now = datetime.datetime.now()
    time_format = (now.year, now.month, now.day,
                   now.hour, now.minute, now.second)
    print("[{:02}-{:02}-{:02} {:02}:{:02}:{:02}]: {}".\
          format(*time_format, msg), *args, **kwargs)


from gridback.utils import (
    constants,
    authentication
)
