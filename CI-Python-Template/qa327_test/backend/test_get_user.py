import pytest
import sqlite3
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from qa327.backend import get_user
from qa327.models import db, User

"""
This file defines all unit tests for the frontend registration.
"""

new_email = 'not_a_user@test.com'
new_name = 'mr new'
new_password = 'New123!'

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
        - validate that the email now returns an existing user
        - delete user
        
        """

        # validate that get_user() does not return a user if the new_email does not yet belong to a user
        assert get_user(new_email) == None
        
        # open /logout
        self.open(base_url + '/logout')
        # open /register
        self.open(base_url + '/register')

        # enter new user's info into the appropriate forms
        self.type("#email", new_email)
        self.type("#name", new_name)
        self.type('#password',new_password)
        self.type('#password2',new_password)

        # submit the forms
        self.click('input[type="submit"]')

        # validate that get_user() does return a user now that new_email belongs to a user
        assert get_user(new_email) != None

        #must remove this user from db.sqlite in order to run test again
        

