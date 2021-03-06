import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

"""
This file defines all unit tests for other(invalid) requests.
"""

# some test data:
invalid_paths = [
    '/asdfasdfasdfdasdf',
    '/%20',
    '/-------',
    '/loginx',
    '/lohout'
]

default_timeout=1

class FrontEndOtherRequestsTest(BaseCase):

    def test_other_requests(self, *_):
        """
        **Test Case R8 - For any other requests, the system should return a 404 error**

        Mocking:

        - None

        Actions:

        - The user visits an invalid path in `invalid_paths`
        - The page should show an error message and the browser should receive an 'HTTP 404' response
        
        """
        
        # visit every invalid path in 'invalid_paths'
        for path in invalid_paths:
             # open invalid path
            self.open(base_url + path)
            # validate that error message is shown
            self.assert_element("#message", timeout=default_timeout)
            self.assert_text("404 ERROR: The requested URL was not found on the server.", "#message", timeout=default_timeout)

        # close opened window
        self.driver.close()

        # visit every invalid path in 'invalid_paths'
        for path in invalid_paths:
            # validate that browser received a HTTP 404 response
            r = requests.get(base_url + path)
            assert r.status_code == 404
        
        # it only works when they are in seperate for loops, not sure why
