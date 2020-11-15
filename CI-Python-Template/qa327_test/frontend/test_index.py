import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend index.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Mock a sample user
test_user = User(
    email='valid_email@test.com',
    name='validuser',
    password=generate_password_hash('123ABCxyz*'),
    balance=2000
)

# Mock a sample ticket
test_ticket = Ticket(
    name='ticketname',
    email='valid_email@test.com',
    quantity=50,
    price=45,
    expiration_date=20221231
)

default_timeout=1

class FrontEndIndexTest(BaseCase):

    def test_homepage_login_redirect(self, *_):
        """
        **Test R3.1 If the user is not logged in, redirect to login page**
        
        Mocking:
        None
        
        Actions:
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /
        - validate that the current page is /login
        
        """
        #open /logout
        self.open(base_url + '/logout')
        #open /
        self.open(base_url + '/')
        #validate that we have been redirected to /login
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/login')
        
    @patch('qa327.backend.get_user', return_value='test_user')
    @patch('qa327.backend.login_user', return_value='test_user')
    def test_homepage_contents(self, *_):
        """
        ***Test R3.2-4 This page shows a Header 'Hi {}'.format(user.name), This page shows user balance., This page shows a logout link, pointing to /logout***
        
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        
        Actions:
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - validate that the current page contains a #welcome_header element
        - validate that the #welcome_header element contains the text 'Hi validuser'
        - validate that the current page contains a #balance element
        - validate that the #balance element contains the text 'Your balance is: 2000!'
        - validate that the current page contains a logout link
        
        """
        #open /logout
        self.open(base_url + '/logout')
        #open /login
        self.open(base_url + '/login')
        #enter the test_user's email into element #email
        self.type("#email", 'valid_email@test.com')
        #enter the test_user's password into element #password
        self.type("#password",'123ABCxyz*')
        #click submit button
        self.click('input[type="submit"]')
        #validate that the current page contains a #welcome_header element
        self.assert_element('#welcome_header',timeout=default_timeout)
        #validate that the #welcome_header element contains the text 'Hi validuser'
        self.assert_text('Hi validuser','id=welcome_header',timeout=default_timeout)
        #validate that the current page contains a #balance element
        self.assert_element('#balance',timeout=default_timeout)
        #validate that the #balance element contains the text 'Your balance is: 2000!'
        self.assert_text('Your balance is: 2000!','id=balance',timeout=default_timeout)
        #validate that the current page contains a logout link
        self.assert_element('href=/logout',timeout=default_timeout)
        self.assert_text('logout','href=/logout',timeout=default_timeout)
        
    @patch('qa327.backend.get_user', return_value='test_user')
    @patch('qa327.backend.login_user', return_value='test_user')
    @patch('qa327.backend.get_all_tickets', return_value='test_ticket')
    def test_homepage_tickets(self, *_):
        """
        ***Test Case R3.5 This page lists all available tickets. Information including the quantity of each ticket, the owner's email, and the price, for tickets that are not expired.***
        
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.get_all_tickets to return a test_ticket instance
        
        Actions:
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - validate that the current page contains a #tickets element
        - validate that the #tickets element contains the text 'ticketname 50 valid_email@test.com 45'
        
        """
        #open /logout
        self.open(base_url + '/logout')
        #open /login
        self.open(base_url + '/login')
        #enter the test_user's email into element #email
        self.type("#email", 'valid_email@test.com')
        #enter the test_user's password into element #password
        self.type("#password",'123ABCxyz*')
        #click submit button
        self.click('input[type="submit"]')
        #validate that the current page contains a #tickets element
        self.assert_element('#tickets',timeout=default_timeout)
        #validate that the #tickets element contains the text 'ticketname 50 valid_email@test.com 45'
        self.assert_text('ticketname 50 valid_email@test.com 45','id=tickets',timeout=default_timeout)
        
    @patch('qa327.backend.get_user', return_value='test_user')
    @patch('qa327.backend.login_user', return_value='test_user')
    @patch('qa327.backend.get_all_tickets', return_value='test_ticket')
    def test_homepage_sell_form(self, *_):
        """
        ***R3.6,9 The page contains a form that a user can submit new tickets for sell. Fields: name, quantity, price, expiration date, The ticket-selling form can be posted to /sell***
        
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.get_all_tickets to return a test_ticket instance
        
        Actions:
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - verify that the current page contains a sell form
        - verify that the sell form has a name field
        - verify that the sell form has a quantity field
        - verify that the sell form has a price field
        - verify that the sell form has an expiration date field
        - verify that the sell form can be posted to /sell
        
        """
        #open /logout
        self.open(base_url + '/logout')
        #open /login
        self.open(base_url + '/login')
        #enter the test_user's email into element #email
        self.type("#email", 'valid_email@test.com')
        #enter the test_user's password into element #password
        self.type("#password",'123ABCxyz*')
        #click submit button
        self.click('input[type="submit"]')
        #verify that the current page has a sell form
        self.assert_text('Sell','form action="/sell">div>label',timeout=default_timeout)
        #verify that the sell form has a name field
        self.assert_element('#sell_name',timeout=default_timeout)
        #verify that the sell form has a quantity field
        self.assert_element('#sell_quantity',timeout=default_timeout)
        #verify that the sell form has a price field
        self.assert_element('#sell_price',timeout=default_timeout)
        #verify that the sell form has an expiration date field
        self.assert_element('#sell_expiration_date',timeout=default_timeout)
        #verify that the sell form can be posted to /sell
        self.assert_element('form action="/sell" method="post"',timeout=default_timeout)
        
   
        
        
    @patch('qa327.backend.get_user', return_value='test_user')
    @patch('qa327.backend.login_user', return_value='test_user')
    @patch('qa327.backend.get_all_tickets', return_value='test_ticket')
    def test_homepage_buy_form(self, *_):
        """
        ***R3.7,10 The page contains a form that a user can buy new tickets. Fields: name, quantity, The ticket-buying form can be posted to /buy***
        
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.get_all_tickets to return a test_ticket instance
        
        Actions:
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - verify that the current page contains a buy form
        - verify that the buy form has a name field
        - verify that the buy form has a quantity field
        - verify that the buy form can be posted to /buy
        
        """
        #open /logout
        self.open(base_url + '/logout')
        #open /login
        self.open(base_url + '/login')
        #enter the test_user's email into element #email
        self.type("#email", 'valid_email@test.com')
        #enter the test_user's password into element #password
        self.type("#password",'123ABCxyz*')
        #click submit button
        self.click('input[type="submit"]')
        #verify that the current page has a buy form
        self.assert_text('Buy','form action="/buy">div>label',timeout=default_timeout)
        #verify that the buy form has a name field
        self.assert_element('#buy_name',timeout=default_timeout)
        #verify that the buy form has a quantity field
        self.assert_element('#buy_quantity',timeout=default_timeout)
        #verify that the buy form can be posted to /buy
        self.assert_element('form action="/buy" method="post"',timeout=default_timeout)
        
    @patch('qa327.backend.get_user', return_value='test_user')
    @patch('qa327.backend.login_user', return_value='test_user')
    @patch('qa327.backend.get_all_tickets', return_value='test_ticket')
    def test_homepage_update_form(self, *_):
        """
        ***R3.8,11 The page contains a form that a user can update existing tickets. Fields: name, quantity, price, expiration date, The ticket-update form can be posted to /update***
        
        Mocking:
        - Mock backend.get_user to return a test_user instance
        - Mock backend.login_user to return a test_user instance
        - Mock backend.get_all_tickets to return a test_ticket instance
        
        Actions:
        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - verify that the current page contains an update form
        - verify that the update form has a name field
        - verify that the update form has a quantity field
        - verify that the update form has a price field
        - verify that the update form has an expiration date field
        - verify that the update form can be posted to /update
        
        """
        #open /logout
        self.open(base_url + '/logout')
        #open /login
        self.open(base_url + '/login')
        #enter the test_user's email into element #email
        self.type("#email", 'valid_email@test.com')
        #enter the test_user's password into element #password
        self.type("#password",'123ABCxyz*')
        #click submit button
        self.click('input[type="submit"]')
        #verify that the current page has an update form
        self.assert_text('Update','form action="/update">div>label',timeout=default_timeout)
        #verify that the update form has a name field
        self.assert_element('#update_name',timeout=default_timeout)
        #verify that the update form has a quantity field
        self.assert_element('#update_quantity',timeout=default_timeout)
        #verify that the update form has a price field
        self.assert_element('#update_price',timeout=default_timeout)
        #verify that the update form has an expiration date field
        self.assert_element('#update_expiration_date',timeout=default_timeout)
        #verify that the update form can be posted to /update
        self.assert_element('form action="/update" method="post"',timeout=default_timeout)
        
        
