import pytest
import requests
from seleniumbase import BaseCase

from qa327_test.conftest import base_url

invalid_paths = [
    '/asdfasdfasdfdasdf',
    '/%20',
    '/-------'
    '/loginx'
    '/lohout'
]

default_timeout=1

class FrontEndIndexTest(BaseCase):

    def test_other_requests(self, *_):
        """
        **Test Case R8 - For any other requests, the system should return a 404 error**

        Mocking:

        - None

        Actions:

        - The user visits an invalid path in `invalid_paths`
        - The page should show an error message and the browser should receive an 'HTTP 404' response
        
        """
        # visit ever invalid path in 'invalid_paths'
        for path in invalid_paths:
            response = requests.get(base_url + path)
            self.assert_equal(response.status_code, 404, response.status_code)
             # open invalid path
            self.open(base_url + path)
            # validate that error message is shown
            self.assert_element("#message", timeout=default_timeout)
            self.assert_text("404 ERROR: The requested URL was not found on the server.", "#message", timeout=default_timeout)
            # validate that browser received a HTTP 404 response
            #response = requests.get(base_url + path)
            #self.assert_equal(response.status_code, 404, response.status_code)
            # or
            #assert response.status_code == 404