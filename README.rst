DEPRECATION WARNING
====================

.. WARNING::

    There is a much better lib than this one for the job: txrequests_ .

    You are now invited to use this instead.


If I have any improvements to make, I'll make them to txrequests and not here.


Twisted adapter for the requests library
============================================

Tiny add-on for the requests_ HTTP library so it can
be used transparently with Twisted_ by deferring blocking calls to threads.

It just wraps all requests in deferToThread, really.

Usage:

.. code-block:: python

    # To use requests with Twisted, you just need to use
    # a our requests.Session subclass manually.
    # See http://docs.python-requests.org/en/latest/user/advanced/
    # for some informations about the Session class.
    from requests_twisted import TwistedRequestsSession
    session = TwistedRequestsSession()

    # Then after, instead of doing requests.get|post|whatever(), you just do
    # session.get|post|whatever().
    # It returns a defer :
    defer = session.get('http://github.com/sametmax/')
    def print_status(response):
        print(response.url, response.status_code)

    # Which you just handle as you would usually do.
    defer.addCallback(print_status)

There are no changes to the request API, the only difference is the defer.

If you are doing a lot of requests, remember you can change the reactor thread pool by doing :

.. code-block:: python

    from twisted.internet import reactor
    reactor.suggestThreadPoolSize(number_of_threads)

The default size of the thread pool depends on the reactor being used; the default reactor uses a minimum size of 5 and a maximum size of 10. Be careful that you understand threads and their resource usage before drastically altering the thread pool sizes.

Installation
============

    pip install requests-twisted

Informations
============

Supports : Python 2.7 (maybe 2.6, I didn't test it)
Licence : Zlib

.. _`requests`: https://github.com/kennethreitz/requests
.. _`Twisted`: http://twistedmatrix.com
.. _`txrequests`: https://pypi.python.org/pypi/txrequests
