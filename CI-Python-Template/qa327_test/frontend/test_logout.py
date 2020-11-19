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

        # open logout page
        self.open(base_url + "/logout")
        # open login page again
        self.open(base_url + "/login")
        self.assert_equal(current_url, base_url+"/login")
        self.assert_text("Please login", "#message")
