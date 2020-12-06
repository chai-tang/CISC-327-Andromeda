import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for buying tickets.
"""

test_user = User(
    email='test_frontend@test.com',
    name='testfrontend',
    password=generate_password_hash('123ABCxyz*'),
    balance=200
)

test_ticket = Ticket(
    name='t2',
    email='test_frontend@test.com',
    quantity=5,
    price=50,
    expiration_date=20221231
)

valid_names = [
    'ticket',
    't3',
	't3 Name'
]

invalid_names = [
    ' t3',
	't3:',
    't3 '
]

lengthy = 'veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylongname'

non_lengthy = 'notverylongname'

valid_quantity = [
    1,
    50,
	100
]

invalid_quantities = [
    -1,
    0,
	101
]

default_timeout=1

class FrontEndUpdateTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    @patch('qa327.backend.buy_tickets', return_value=None)
    def test_buy_ticket_name_validation(self, *_):
        """
        **Test Case R6.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of all test tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.buy_tickets to return None

        Actions:

        - open /
        - enter an invalid name into element #name
        - enter a valid quantity into element #quantity
        - click element input[type="submit"]
        - repeat with each invalid name
        - validate that it causes an error
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - click element input[type="submit"]
        - repeat with each valid name 
        - validate that it does not cause an error
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
            self.type('#buy_name',invalid_input)
            self.type('#buy_quantity',valid_quantity[0])
            # submit the form
            self.click('#buy-submit')
            # validate that the ticket buy has failed and shown the appropriate error message
            self.assert_text("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",'#message',timeout=default_timeout)

        # test all valid names
        for valid_input in valid_names:
            # enter valid inputs
            self.type('#buy_name',valid_input)
            self.type('#buy_quantity',valid_quantity[0])
            # submit the form
            self.click('#buy-submit')
            # validate that the name error message is not being displayed
            message = self.get_text('#message')
            self.assert_not_equal("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",message)
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    @patch('qa327.backend.buy_tickets', return_value=None)
    def test_buy_ticket_name_max_length(self, *_):
        """
        **Test Case R6.2 - The name of the ticket is no longer than 60 characters**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of all test tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.buy_tickets to return None

        Actions:

        - open /
        - enter a lengthy name into element #name
        - enter a valid quantity into element #quantity
        - click element input[type="submit"]
        - validate that it causes an error
        - enter a non lenghty name into element #name
        - enter a valid quantity into element #quantity
        - click element input[type="submit"]
        - validate that it does not cause an error
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # enter a lengthy name and valid everything else
        self.type('#buy_name',lengthy)
        self.type('#buy_quantity',valid_quantity[0])
        # submit the form
        self.click('#buy-submit')
        # validate that the ticket buy has failed and shown the appropriate error message
        self.assert_text("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",'#message',timeout=default_timeout)

        # enter valid inputs
        self.type('#buy_name',non_lengthy)
        self.type('#buy_quantity',valid_quantity[0])
        # submit the form
        self.click('#buy-submit')
        # validate that the name error message is not being displayed
        message = self.get_text('#message')
        self.assert_not_equal("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",message)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    @patch('qa327.backend.buy_tickets', return_value=None)
    def test_buy_ticket_quantity_validation(self, *_):
        """
        **Test Case R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of all test tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.buy_tickets to return None

        Actions:

        - open /
        - enter a valid name into element #name
        - enter a invalid quantity into element #quantity
        - click element input[type="submit"]
        - repeat with each invalid quantity
        - validate that it causes an error
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - click element input[type="submit"]
        - repeat with each valid quantity
        - validate that it does not cause an error
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
            self.type('#buy_name',valid_names[0])
            self.type('#buy_quantity',invalid_input)
            # submit the form
            self.click('#buy-submit')
            # validate that the ticket buy has failed and shown the appropriate error message
            self.assert_text("Ticket quantity must be between 1 and 100",'#message',timeout=default_timeout)

        # test all valid quantities
        for valid_input in valid_quantity:
            # enter valid inputs
            self.type('#buy_name',valid_names[0])
            self.type('#buy_quantity',valid_input)
            # submit the form
            self.click('#buy-submit')
            # validate that the quantity error message is not being displayed
            message = self.get_text('#message')
            self.assert_not_equal("Ticket quantity must be between 1 and 100",message)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    @patch('qa327.backend.buy_tickets', return_value=None)
    def test_buy_ticket_is_purchaseable(self, *_):
        """
        **Test Case R6.4 - The ticket name exists in the database and the quantity is more than the quantity requested to buy**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of all test tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.buy_tickets to return None

        Actions:

        - open /
        - enter a valid name that does not exist in the list of all available tickets into the element #name
        - enter a valid quantity that is less than the quantity of available tickets into the element #quantity
        - click element input[type="submit"]
        - validate that it causes an error
        - enter a valid name that does exist in the list of all available tickets into the element #name
        - enter a valid quantity that is greater than the quantity of available tickets into the element #quantity
        - click element input[type="submit"]
        - validate that it causes an error
        - enter a valid name that does exist in yhe list of all available tickets into the element #name
        - enter a valid quantity that is less than the quantity of available tickets into the element #quantity
        - click element input[type="submit"]
        - validate that it does not cause an error
        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # attempt to buy a ticket that doesn't exist
        self.type('#buy_name',"notaticket")
        self.type('#buy_quantity',1)
        # submit the form
        self.click('#buy-submit')
        # validate that the ticket buy has failed and shown the appropriate error message
        self.assert_text("No such ticket notaticket",'#message',timeout=default_timeout)

        # attempt to buy a too many of a ticket that exists
        self.type('#buy_name',"t2")
        self.type('#buy_quantity',50)
        # submit the form
        self.click('#buy-submit')
        # validate that the ticket buy has failed and shown the appropriate error message
        self.assert_text("Not enough tickets.",'#message',timeout=default_timeout)

        # attempt to do a valid ticket purchase
        self.type('#buy_name',"t2")
        self.type('#buy_quantity',1)
        # submit the form
        self.click('#buy-submit')
        # validate that no error messages are displayed
        message = self.get_text('#message')
        self.assert_not_equal("No such ticket t2",message)
        self.assert_not_equal("Not enough tickets.",message)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    @patch('qa327.backend.buy_tickets', return_value=None)
    @patch('qa327.backend.set_balance', return_value=None)
    def test_buy_ticket_balance_validation(self, *_):
        """
        **Test Case R6.5 - The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of all test tickets
        - Mock backend.login_user to return a test_user instance
        - Mock backend.buy_tickets to return None
        - Mock backend.set_balance to return None

        Actions:

        - open / 
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity (but a quantity that will cost more than test_user's balance)
        - click element input[type="submit"]
        - validate that the ticket buy failed, with appropriate error message
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity (with a quantity that the test_user can afford)
        - click element input[type="submit"]
        - validate that the ticket buy succeeded, with appropriate message

        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # attempt to buy more tickets than can be afforded
        self.type('#buy_name',"t2")
        self.type('#buy_quantity',5)
        # submit the form
        self.click('#buy-submit')
        # validate that the ticket buy has failed and shown the appropriate error message
        self.assert_text("Not enough balance to purchase tickets.",'#message',timeout=default_timeout)

        # attempt to buy an affordable number of tickets
        self.type('#buy_name',"t2")
        self.type('#buy_quantity',1)
        # submit the form
        self.click('#buy-submit')
        # validate that the ticket buy has succeeded and shown the appropriate message
        self.assert_text("Tickets purchased",'#message',timeout=default_timeout)