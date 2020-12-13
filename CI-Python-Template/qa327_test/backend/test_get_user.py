import pytest
import sqlite3
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.backend import get_user
from qa327.models import db, User

"""
This file defines all unit tests for the get_user backend method
"""

invalid_email = 'not_a_user@test.com'
invalid_name = 'mr new'
invalid_password = 'New123!'
valid_email = 'test_user@test.com'
valid_name = 'test user'
valid_password = 'Test123!'

class BackendMethodTest(BaseCase):

    def test_get_user(self, *_):
        """
        **Test backend method get_user**

        Mocking:
        None

        Actions:
        - validate that an email with no existing user returns None
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - register new user
        - validate if the two emails are returning existing users
        - delete user

        """

        # validate that get_user() does not return a user if the new_email does not yet belong to a user
        assert get_user(invalid_email) == None
        assert get_user(valid_email) == None

        # open /logout
        self.open(base_url + '/logout')
        # open /register
        self.open(base_url + '/register')

        # enter new user's info into the appropriate forms
        self.type("#email", valid_email)
        self.type("#name", valid_name)
        self.type('#password', valid_password)
        self.type('#password2', valid_password)

        # submit the forms
        self.click('input[type="submit"]')

        # validate that get_user() does return a user now that new_email belongs to a user
        assert get_user(valid_email) != None
        assert get_user(invalid_email) == None

        #must remove this user from db.sqlite in order to run test again
        new_user = User.query.filter_by(email=valid_email).first()
        db.session.delete(new_user)
        db.session.commit()
