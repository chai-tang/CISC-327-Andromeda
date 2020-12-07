import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for selling tickets.
"""

test_user = User(
    email='test_frontend@test.com',
    name='testfrontend',
    password=generate_password_hash('123ABCxyz*'),
    balance=2000
)

test_ticket1 = Ticket(
    name='t1',
    email='seller@test.com',
    quantity=1,
    price=50,
    expiration_date=20221231
)

test_ticket2 = Ticket(
    name='t2',
    email='test_frontend@test.com',
    quantity=1,
    price=50,
    expiration_date=20221231
)

test_tickets = [
    test_ticket1,
	test_ticket2
]

valid_name = 'ticket'

valid_names = [
    't3',
	't3 Name'
]

invalid_names = [
    ' t3',
	't3:'
]

too_long_name = 'veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylongname'

valid_quantity = 1 

invalid_quantities = [
    0,
	101
]

valid_price = 50

invalid_price = [
    9,
	101
]

valid_date = 20211230

invalid_date = '2021 12 30'

default_timeout=1

class FrontEndSellTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_tickets', return_value=None)
    def test_sell_ticket_name_validation(self, *_):
        """
        **Test Case R4.1 - The name of the ticket must be alphanumeric with space allowed only if it is not the first character**
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of all available tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.sell_tickets to return None
        Actions:
        - open /
        - enter an invalid name into the #name field of the #sell_tickets form
        - enter a valid quantity into the #quantity field of the #sell_tickets form
        - enter a valid price into the #price field of the #sell_tickets form
        - enter a valid date into the #expiration_date field of the #sell_tickets form
        - click element input[type="submit"]
        - validate that the sell process failed and an error message is displayed
        - repeat above steps for each invalid and valid name
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # test all invalid names
        for invalid_input in invalid_names:
            # enter an invalid name and valid everything else
            self.type('#sell_name',invalid_input)
            self.type('#sell_quantity',valid_quantity)
            self.type('#sell_price',valid_price)
            self.type('#sell_expiration_date',valid_date)
            # submit the form
            self.click('#sell-submit')
            # validate that the ticket sale has failed and shown the appropriate error message
            self.assert_text("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",'#message',timeout=default_timeout)

        # test all valid names
        for valid_input in valid_names:
            # enter valid inputs
            self.type('#sell_name',valid_input)
            self.type('#sell_quantity',valid_quantity)
            self.type('#sell_price',valid_price)
            self.type('#sell_expiration_date',valid_date)
            # submit the form
            self.click('#sell-submit')
            # validate that the successful ticket sale message is being displayed
            self.assert_text("Tickets added to listing",'#message',timeout=default_timeout)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_tickets', return_value=None)
    def test_sell_ticket_name_max_length(self, *_):
        """
        **Test Case R4.2 - The name of the ticket must be no longer than 60 characters**
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_tickets to return a list of all available tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.sell_tickets to return None
        Actions:
        - open /
        - enter a too long name into the #name field of the #sell_tickets form
        - enter a valid quantity into the #quantity field of the #sell_tickets form
        - enter a valid price into the #price field of the #sell_tickets form
        - enter a valid date into the #expiration_date field of the #sell_tickets form
        - click element input[type="submit"]
        - repeat above steps for a valid name
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # enter an name that's too long and valid everything else
        self.type('#sell_name',too_long_name)
        self.type('#sell_quantity',valid_quantity)
        self.type('#sell_price',valid_price)
        self.type('#sell_expiration_date',valid_date)
        # submit the form
        self.click('#sell-submit')
        # validate that the ticket sale has failed and shown the appropriate error message
        self.assert_text("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",'#message',timeout=default_timeout)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_tickets', return_value=None)
    def test_sell_ticket_quantity_validation(self, *_):
        """
        **Test Case R4.3 - The quantity of the tickets has to be more than 0 and less than or equal to 100**
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_tickets to return a list of all available tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.sell_tickets to return None
        Actions:
        - open /
        - enter an invalid quantity into the #quantity field of the #sell_tickets form
        - enter a valid name into the #name field of the #sell_tickets form
        - enter a valid price into the #price field of the #sell_tickets form
        - enter a valid date into the #expiration_date field of the #sell_tickets form
        - click element input[type="submit"]
        - repeat above steps for each invalid and valid quantity
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # test all invalid quantities
        for invalid_input in invalid_quantities:
            # enter an invalid name and valid everything else
            self.type('#sell_name',valid_name)
            self.type('#sell_quantity',invalid_input)
            self.type('#sell_price',valid_price)
            self.type('#sell_expiration_date',valid_date)
            # submit the form
            self.click('#sell-submit')
            # validate that the ticket sale has failed and shown the appropriate error message
            self.assert_text("Ticket quantity must be between 1 and 100.",'#message',timeout=default_timeout)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_tickets', return_value=None)
    def test_sell_ticket_price_validation(self, *_):
        """
        **Test Case R4.4 - The price must be in the range [10,100]**
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_tickets to return a list of all available tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.sell_tickets to return None
        Actions:
        - open /
        - enter an invalid price into the #price field of the #sell_tickets form
        - enter a valid name into the #name field of the #sell_tickets form
        - enter a valid quantity into the #quantity field of the #sell_tickets form
        - enter a valid date into the #expiration_date field of the #sell_tickets form
        - click element input[type="submit"]
        - repeat above steps for each invalid and valid price
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # test all invalid quantities
        for invalid_input in invalid_price:
            # enter an invalid name and valid everything else
            self.type('#sell_name',valid_name)
            self.type('#sell_quantity',valid_quantity)
            self.type('#sell_price',invalid_input)
            self.type('#sell_expiration_date',valid_date)
            # submit the form
            self.click('#sell-submit')
            # validate that the ticket sale has failed and shown the appropriate error message
            self.assert_text("Ticket price must be between 10 and 100.",'#message',timeout=default_timeout)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_tickets', return_value=None)
    def test_sell_ticket_date_validation(self, *_):
        """
        **Test Case R4.5 - The date must be given in the format YYYYMMDD**
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_tickets to return a list of all available tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.sell_tickets to return None
        Actions:
        - open /
        - enter an invalid date into the #expiration_date field of the #sell_tickets form
        - enter a valid name into the #name field of the #sell_tickets form
        - enter a valid quantity into the #quantity field of the #sell_tickets form
        - enter a valid price into the #price field of the #sell_tickets form
        - click element input[type="submit"]
        - repeat above steps for a valid date
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # test all invalid quantities
        for invalid_input in invalid_date:
            # enter an invalid name and valid everything else
            self.type('#sell_name',valid_name)
            self.type('#sell_quantity',valid_quantity)
            self.type('#sell_price',valid_price)
            self.type('#sell_expiration_date',invalid_input)
            # submit the form
            self.click('#sell-submit')
            # validate that the ticket sale has failed and shown the appropriate error message
            self.assert_text("Expiration date must be in form YYYYMMDD.",'#message',timeout=default_timeout)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=test_tickets)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.sell_tickets', return_value=None)
    def test_sell_ticket_success(self, *_):
        """
        **Test Case R4.7 - The added new ticket information will be posted on the user profile page**
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_tickets to return a list of all available tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.sell_tickets to return None
        Actions:
        - open /
        - enter a valid name into the #name field of the #sell_tickets form
        - enter a valid quantity into the #quantity field of the #sell_tickets form
        - enter a valid price into the #price field of the #sell_tickets form
        - enter a valid date into the #expiration_date field of the #sell_tickets form
        - click element input[type"submit"]
        - verify that the current page is /
        - verify that the current page contains a #table element
        - verify that the new ticket is displayed in this #table element
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # enter the valid inputs
        # enter an invalid name and valid everything else
        self.type('#sell_name',valid_name)
        self.type('#sell_quantity',valid_quantity)
        self.type('#sell_price',valid_price)
        self.type('#sell_expiration_date',valid_date)
        # submit the form
        self.click('#sell-submit')
        # since sell_tickets is mocked, the new ticket can't actually be added to the listing
        # instead, we'll validate that the "ticket added to listing" message is displayed when all inputs are valid
        # and then check that our pre-made mocked tickets are being shown
        self.assert_text("Tickets added to listing",'#message',timeout=default_timeout)
        self.assert_text("t1 1 seller@test.com 50",'#tickets .ticket',timeout=default_timeout)