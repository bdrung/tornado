# flake8: noqa
from __future__ import absolute_import, division, print_function
from tornado4.test.util import unittest


class ImportTest(unittest.TestCase):
    def test_import_everything(self):
        # Some of our modules are not otherwise tested.  Import them
        # all (unless they have external dependencies) here to at
        # least ensure that there are no syntax errors.
        import tornado4.auth
        import tornado4.autoreload
        import tornado4.concurrent
        import tornado4.escape
        import tornado4.gen
        import tornado4.http1connection
        import tornado4.httpclient
        import tornado4.httpserver
        import tornado4.httputil
        import tornado4.ioloop
        import tornado4.iostream
        import tornado4.locale
        import tornado4.log
        import tornado4.netutil
        import tornado4.options
        import tornado4.process
        import tornado4.simple_httpclient
        import tornado4.stack_context
        import tornado4.tcpserver
        import tornado4.tcpclient
        import tornado4.template
        import tornado4.testing
        import tornado4.util
        import tornado4.web
        import tornado4.websocket
        import tornado4.wsgi

    # for modules with dependencies, if those dependencies can be loaded,
    # load them too.

    def test_import_pycurl(self):
        try:
            import pycurl  # type: ignore
        except ImportError:
            pass
        else:
            import tornado4.curl_httpclient
