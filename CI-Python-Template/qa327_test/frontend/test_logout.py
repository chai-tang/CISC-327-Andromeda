import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for logging out.
"""

# Mock a sample user
test_user = User(
    email='test_logout@test.com',
    name='test_logout',
    password=generate_password_hash('TeStL0g0uT!')
)

# Mock some sample tickets
test_tickets = [
    {'name': 't1', 'quantity': 1, 'contact': 'seller@test.com', 'price': 100},
    {'name': 't2', 'quantity': 100, 'contact': 'seller2@test.com', 'price': 10}
]


class FrontEndHomePageTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    def test_logout(self, *_):
        """
        This is a sample front end unit test to log in, then log out, and redirection to home page
        """
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "test_logout@test.com")
        self.type("#password", "TeStL0g0uT!")
        # click enter button
        self.click('input[type="submit"]')

        # after clicking on the browser (the line above)
        # the front-end code is activated
        # and tries to call get_user function.
        # The get_user function is supposed to read data from database
        # and return the value. However, here we only want to test the
        # front-end, without running the backend logics.
        # so we patch the backend to return a specific user instance,
        # rather than running that program. (see @ annotations above)


        # open home page
        self.open(base_url)
        # test if the page loads correctly
        self.assert_element("#welcome-header")
        self.assert_text("Welcome test_logout !", "#welcome-header")

        self.click('logout')
        self.open(base_url + "/login")
        self.assert_text("Log In")
        self.assert_text("Please login", "#message")
