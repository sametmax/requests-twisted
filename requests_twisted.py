# -*- coding: utf-8 -*-
"""
requests_twisted : Twisted adapter for the requests library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tiny add-on for the requests http library so it can
be used transparently with twisted by defering blocking calls to threads.

    from requests_twisted import TwistedRequestsSession
    session = TwistedRequestsSession()
    defer = session.get('http://github.com/sametmax/')
    def print_status(response):
        print(response.url, response.status_code)
    defer.addCallback(print_status)

"""

__title__ = 'requests-twisted'
__version__ = '0.1.2'
__author__ = 'Sam et Max'
__license__ = 'Zlib'

from requests import Session
from twisted.internet import threads

class TwistedRequestsSession(Session):

    def request(self, *args, **kwargs):
        """Maintains the existing api for Session.request.

        Used by all of the higher level methods, e.g. Session.get.
        """
        func = super(TwistedRequestsSession, self).request
        return threads.deferToThread(func, *args, **kwargs)
