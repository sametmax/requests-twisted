#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Requests."""

from requests import Response
from requests_twisted import TwistedRequestsSession
from twisted.trial.unittest import TestCase
from twisted.internet.defer import Deferred, inlineCallbacks

class RequestsTestCase(TestCase):

    @inlineCallbacks
    def test_get(self):
        # basic futures get
        sess = TwistedRequestsSession()
        defer = sess.get('http://httpbin.org/get')
        self.assertIsInstance(defer, Deferred)

        resp = yield defer
        self.assertIsInstance(resp, Response)
        self.assertEqual(200, resp.status_code)

        resp = yield sess.get('http://httpbin.org/status/404')
        self.assertEqual(404, resp.status_code)

    @inlineCallbacks
    def test_redirect(self):
        """ Tests for the ability to cleanly handle redirects. """
        sess = TwistedRequestsSession()
        resp = yield sess.get('http://httpbin.org/redirect-to?url=get')
        self.assertIsInstance(resp, Response)
        self.assertEqual(200, resp.status_code)

        resp = yield sess.get('http://httpbin.org/redirect-to?url=status/404')
        self.assertEqual(404, resp.status_code)



