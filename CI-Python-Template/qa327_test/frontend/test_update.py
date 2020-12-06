import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for updating tickets.
"""

test_user = User(
    email='test_frontend@test.com',
    name='testfrontend',
    password=generate_password_hash('123ABCxyz*'),
    balance=2000
)

test_ticket = Ticket(
    name='t2',
    email='test_frontend@test.com',
    quantity=1,
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

valid_price = [
    10,
    50,
    100
]

invalid_price = [
    -1,
    9,
	101
]

valid_date = 20211230

invalid_date = '2021 12 30'

default_timeout=1

class FrontEndUpdateTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.update_tickets', return_value=None)
    def test_update_ticket_name_validation(self, *_):
        """
        **Test Case R5.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.update_tickets to return None

        Actions:

        - open /
        - enter an invalid name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
        - click element input[type="submit"]
        - repeat with each invalid name
        - validate that it causes an error
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
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
            self.type('#update_name',invalid_input)
            self.type('#update_quantity',valid_quantity[0])
            self.type('#update_price',valid_price[0])
            self.type('#update_expiration_date',valid_date)
            # submit the form
            self.click('#update-submit')
            # validate that the ticket update has failed and shown the appropriate error message
            self.assert_text("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",'#message',timeout=default_timeout)

        # test all valid names
        for valid_input in valid_names:
            # enter valid inputs
            self.type('#update_name',valid_input)
            self.type('#update_quantity',valid_quantity[0])
            self.type('#update_price',valid_price[0])
            self.type('#update_expiration_date',valid_date)
            # submit the form
            self.click('#update-submit')
            # validate that the name error message is not being displayed
            message = self.get_text('#message')
            self.assert_not_equal("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",message)
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.update_tickets', return_value=None)
    def test_update_ticket_name_max_length(self, *_):
        """
        **Test Case R5.2 - The name of the ticket is no longer than 60 characters**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.update_tickets to return None

        Actions:

        - open /
        - enter a lengthy name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
        - click element input[type="submit"]
        - validate that it causes an error
        - enter a non lenghty name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
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

        # enter an lengthy name and valid everything else
        self.type('#update_name',lengthy)
        self.type('#update_quantity',valid_quantity[0])
        self.type('#update_price',valid_price[0])
        self.type('#update_expiration_date',valid_date)
        # submit the form
        self.click('#update-submit')
        # validate that the ticket update has failed and shown the appropriate error message
        self.assert_text("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",'#message',timeout=default_timeout)

        # enter all valid inputs
        self.type('#update_name',non_lengthy)
        self.type('#update_quantity',valid_quantity[0])
        self.type('#update_price',valid_price[0])
        self.type('#update_expiration_date',valid_date)
        # submit the form
        self.click('#update-submit')
        # validate that the name error message is not being displayed
        message = self.get_text('#message')
        self.assert_not_equal("Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.",message)
        
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.update_tickets', return_value=None)
    def test_update_ticket_quantity_validation(self, *_):
        """
        **Test Case R5.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.update_tickets to return None

        Actions:

        - open /
        - enter a valid name into element #name
        - enter a invalid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
        - click element input[type="submit"]
        - repeat with each invalid quantity
        - validate that it causes an error
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
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
            # enter an invalid quantity and valid everything else
            self.type('#update_name',valid_names[0])
            self.type('#update_quantity',invalid_input)
            self.type('#update_price',valid_price[0])
            self.type('#update_expiration_date',valid_date)
            # submit the form
            self.click('#update-submit')
            # validate that the ticket update has failed and shown the appropriate error message
            self.assert_text("Quantity must be between 1 and 100",'#message',timeout=default_timeout)

        # test all valid quantities
        for valid_input in valid_quantity:
            # enter valid inputs
            self.type('#update_name',valid_names[0])
            self.type('#update_quantity',valid_input)
            self.type('#update_price',valid_price[0])
            self.type('#update_expiration_date',valid_date)
            # submit the form
            self.click('#update-submit')
            # validate that the quantity error message is not being displayed
            message = self.get_text('#message')
            self.assert_not_equal("Quantity must be between 1 and 100",message)
    
    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.update_tickets', return_value=None)
    def test_update_ticket_price_validation(self, *_):
        """
        **Test Case R5.4 - Price has to be of range [10, 100]**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.update_tickets to return None

        Actions:

        - open /
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - enter a invalid price into element #price 
        - enter a valid date into element #expiration_date
        - click element input[type="submit"]
        - repeat with each invalid price
        - validate that it causes an error
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
        - click element input[type="submit"]
        - repeat with each valid price
        - validate that it does not cause an error

        """
        # login and go the the homepage
        self.open(base_url + '/logout')
        self.open(base_url + '/login')
        self.type("#email", "test_frontend@test.com")
        self.type('#password','123ABCxyz*')
        self.click('input[type="submit"]')
        self.open(base_url + '/')

        # test all invalid prices
        for invalid_input in invalid_price:
            # enter an invalid price and valid everything else
            self.type('#update_name',valid_names[0])
            self.type('#update_quantity',valid_quantity[0])
            self.type('#update_price',invalid_input)
            self.type('#update_expiration_date',valid_date)
            # submit the form
            self.click('#update-submit')
            # validate that the ticket update has failed and shown the appropriate error message
            self.assert_text("Price must be between 10 and 100",'#message',timeout=default_timeout)

        # test all valid prices
        for valid_input in valid_price:
            # enter valid inputs
            self.type('#update_name',valid_names[0])
            self.type('#update_quantity',valid_input)
            self.type('#update_price',valid_input)
            self.type('#update_expiration_date',valid_date)
            # submit the form
            self.click('#update-submit')
            # validate that the price error message is not being displayed
            message = self.get_text('#message')
            self.assert_not_equal("Price must be between 10 and 100",message)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.update_tickets', return_value=None)
    def test_update_ticket_date_validation(self, *_):
        """
        **Test Case R5.5 - Date must be given in the format YYYYMMDD (e.g. 20200901)**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.update_tickets to return None

        Actions:

        - open /
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a invalid date into element #expiration_date
        - click element input[type="submit"]
        - validate that it causes an error
        - enter a valid name into element #name
        - enter a valid quantity into element #quantity
        - enter a valid price into element #price 
        - enter a valid date into element #expiration_date
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

        # enter an invalid date and valid everything else
        self.type('#update_name',valid_names[0])
        self.type('#update_quantity',valid_quantity[0])
        self.type('#update_price',valid_price[0])
        self.type('#update_expiration_date',invalid_date)
        # submit the form
        self.click('#update-submit')
        # validate that the ticket update has failed and shown the appropriate error message
        self.assert_text("Expiration date must be in form YYYYMMDD",'#message',timeout=default_timeout)

        # enter all valid inputs
        self.type('#update_name',valid_names[0])
        self.type('#update_quantity',valid_quantity[0])
        self.type('#update_price',valid_price[0])
        self.type('#update_expiration_date',valid_date)
        # submit the form
        self.click('#update-submit')
        # validate that the date error message is not being displayed
        message = self.get_text('#message')
        self.assert_not_equal("Expiration date must be in form YYYYMMDD",message)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.login_user', return_value=test_user)
    @patch('qa327.backend.get_all_tickets', return_value=[test_ticket])
    @patch('qa327.backend.update_tickets', return_value=None)
    def test_update_ticket_must_exist(self, *_):
        """
        **Test Case R5.6 - The ticket of the given name must exist**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.get_all_tickets to return a list of test ticket instances
        - Mock backend.update_tickets to return None

        Actions:

        - open /
        - enter a name that does not exist in list of all available tickets into the element #name
        - click element input[type="submit"]
        - validate that it causes an error
        - enter a name that does exist in list of all available tickets into the element #name
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

        # attempt to update a ticket that doesn't exist
        self.type('#update_name','notaticket')
        self.type('#update_quantity',valid_quantity[0])
        self.type('#update_price',valid_price[0])
        self.type('#update_expiration_date',valid_date)
        # submit the form
        self.click('#update-submit')
        # validate that the ticket update has failed and shown the appropriate error message
        self.assert_text("No such ticket notaticket.",'#message',timeout=default_timeout)

        # attempt to update a ticket that does exist
        self.type('#update_name','t2')
        self.type('#update_quantity',valid_quantity[0])
        self.type('#update_price',valid_price[0])
        self.type('#update_expiration_date',valid_date)
        # submit the form
        self.click('#update-submit')
        # validate that the ticket update has succeeded
        self.assert_text("Listing updated",'#message',timeout=default_timeout)
