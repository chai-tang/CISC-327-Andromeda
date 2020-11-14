import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all unit tests for the frontend registration.

The tests will only test the frontend portion of the program, by patching the backend to return
specfic values. For example:

@patch('qa327.backend.get_user', return_value=test_user)

Will patch the backend get_user function (within the scope of the current test case)
so that it return 'test_user' instance below rather than reading
the user from the database.

Annotate @patch before unit tests can mock backend methods (for that testing function)
"""

# Moch a sample user
test_user = User(
    email='valid_email@test.com',
    name='validuser',
    password=generate_password_hash('123ABCxyz*')
)

# some test data:
valid_email = 'valid_email@test.com'

valid_password = '123ABCxyz*'
valid_password2 = '456DEFpqr#'

valid_username = 'validuser'

invalid_emails = [
    'has space@test.com',
    '.startswithperiod@test.com',
    'consecutive..periods@test.com',
    'has\\backslash@test.com',
    'has"double"quotes@test.com',
    'wacky)(brackets@test.com',
    'veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylongemail@test.com',
    '@test.com',
    'nodomain.com',
    ' ',
    'local@-hyphens-.com',
    'local@$special#chars!%^&*.com',
    'local@_unscoredomain_.com',
    'local@veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylongdomain.com',
    'local@'
]

invalid_passwords = [
    'onlylowercase',
    'ONLYUPPERCASE',
    '12345678',
    '$@#!&*^',
    'UPPERlower',
    'UPPER123',
    'UPPER!@#$%',
    'lower123',
    'lower!@#$%',
    '1234!@#$',
    'a',
    ' ',
    'almostVALID123',
    '*ALMOSTVALID123*',
    '*almostvalid123*'
]

invalid_usernames = [
    'special!@#$%^&*char',
    ' firstspace',
    'lastspace ',
    ' ',
    '\\backslash',
    'double"quotes"',
    'a',
    'more_than_twenty_characters_long'
]

new_email = 'new@test.com'
new_name = 'mr new'
new_password = 'New123!'

new_user = User(
    email='new@test.com',
    name='mr new',
    password='New123!',
    balance=5000
)

default_timeout=1

class FrontEndRegistrationTest(BaseCase):

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.register_user', return_value=None)
    def test_register_homepage_redirect(self, *_):
        """
        **Test R.1 If the user has logged in, redirect back to the user profile page**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - open /register
        - validate that the current page is /

        """
        # open /logout
        self.open(base_url + '/logout')
        # open login
        self.open(base_url + '/login')
        # enter test_user's email and password into the appropriate fields
        self.type("#email", "valid_email@test.com")
        self.type("#password", "123ABCxyz*")
        # click enter button
        self.click('input[type="submit"]')
        # open /register
        self.open(base_url + '/register')
        # validate that we have been redirected to homepage
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/')

    @patch('qa327.backend.register_user', return_value=None)    
    def test_register_exists(self, *_):
        """
        **Test Case R2.2 - otherwise, show the user registration page**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - validate that the current page is /register
        """
        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')
        # validate that the current page is /register
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/register')

    @patch('qa327.backend.register_user', return_value=None)
    def test_register_forms_exist(self, *_):
        """
        **Test Case R2.3 - the registration page shows a registration form requesting: email, user name, password, password2**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - validate that the current page contains a text input element with id #email 
        - validate that this #email element has a label with the text "Email"
        - validate that the current page contains a text input element with id #name 
        - validate that this #name element has a label with the text "Name"
        - validate that the current page contains a text input element with id #password
        - validate that this #password element has a label with the text "Password"
        - validate that the current page contains a text input element with id #password2
        - validate that this #password2 element has a label with the text "Confirm Password"
        """
        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')
        # validate that the current page contains the required elements:
        self.assert_element('#email',timeout=default_timeout)
        self.assert_text('Email','label[for=email]',timeout=default_timeout)
        self.assert_element('#name',timeout=default_timeout)
        self.assert_text('Name','label[for=name]',timeout=default_timeout)
        self.assert_element('#password',timeout=default_timeout)
        self.assert_text('Password','label[for=password]',timeout=default_timeout)
        self.assert_element('#password2',timeout=default_timeout)
        self.assert_text('Confirm Password','label[for=password2]',timeout=default_timeout)

    @patch('qa327.backend.register_user', return_value=None)
    def test_register_postrequest(self, *_):
        """
        **Test Case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - validate that the current page has a form element
        - validate that this form element has the attribute method="post"
        """
        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')
        # validate that the current page has a form element
        self.assert_element('form',timeout=default_timeout)
        # validate that this form element has the attribute method="post"
        method = self.get_attribute('form','method',timeout=default_timeout)
        self.assert_equal(method,'post')

    @patch('qa327.backend.register_user', return_value=None)
    def test_register_forms_required(self, *_):
        """
        **Test Case R2.5.1 - Email, name, password, password2 cannot be empty**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - validate that the #email, #password and #password2 elements all have the 'required' attribute
        """
        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')
        # validate that the #email, #password and #password2 elements all have the 'required' attribute
        email_required = self.get_attribute('#email','required',timeout=default_timeout)
        self.assert_not_equal(email_required,None)
        name_required = self.get_attribute('#name','required',timeout=default_timeout)
        self.assert_not_equal(email_required,None)
        password_required = self.get_attribute('#password','required',timeout=default_timeout)
        self.assert_not_equal(email_required,None)
        password2_required = self.get_attribute('#password','required',timeout=default_timeout)
        self.assert_not_equal(email_required,None)

    @patch('qa327.backend.register_user', return_value=None)
    def test_register_email_validation(self, *_):

        """
        **Test Case R2.5.2 - Email has to satisfy the same requirements as defined in R1**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - enter an invalid input into #email
        - fill all other input fields with valid inputs
        - click element input[type="submit"]
        - validate that the current page is /login with a #message element containing the text 'email format is incorrect'
        - do this for all the invalid_emails
        """

        # open /logout
        self.open(base_url + '/logout')

        # test all invalid emails
        for invalid_input in invalid_emails:
            # enter invalid email and valid everything else
            self.open(base_url + '/register')
            self.type("#email", invalid_input)
            self.type("#name", valid_username)
            self.type('#password',valid_password)
            self.type('#password2',valid_password)
            # submit the forms
            self.click('input[type="submit"]')
            # validate that we are redirected to /login with appropriate error message
            current_url = self.driver.current_url
            self.assert_equal(current_url,base_url+'/login?message=email+format+is+incorrect',msg=invalid_input)

    @patch('qa327.backend.register_user', return_value=None)
    def test_register_password_validation(self, *_):

        """
        **Test Case R2.5.3 - Password has to satisfy the same requirements as defined in R1**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - enter an invalid input into #password
        - fill all other input fields with valid inputs
        - click element input[type="submit"]
        - validate that the current page is /login with a #message element containing the text 'password format is incorrect'
        - do this for all the invalid_passwords
        """  

        # open /logout
        self.open(base_url + '/logout')

        # test all invalid passwords
        for invalid_input in invalid_passwords:
            # enter invalid password and valid everything else
            self.open(base_url + '/register')
            self.type("#email", valid_email)
            self.type("#name", valid_username)
            self.type('#password',invalid_input)
            self.type('#password2',invalid_input)
            # submit the forms
            self.click('input[type="submit"]')
            # validate that we are redirected to /login with appropriate error message
            current_url = self.driver.current_url
            self.assert_equal(current_url,base_url+'/login?message=password+format+is+incorrect',msg=invalid_input)

    @patch('qa327.backend.register_user', return_value=None)  
    def test_register_passwords_identical(self, *_):

        """
        **Test Case R2.6 - 	Password and password2 have to be exactly the same**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - fill the #email and #name fields with valid inputs
        - enter valid_password into the #password element
        - enter valid_password2 into the #password2 element
        - click element input[type="submit"]
        - validate that the current page is /login with a #message element containing the text '{} format is incorrect.'.format(the_corresponding_attribute)
        """  

        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')
        # fill all fields with valid inputs, but enter two different passwords
        self.type("#email", valid_email)
        self.type("#name", valid_username)
        self.type('#password',valid_password)
        self.type('#password2',valid_password2)
        # submit the forms
        self.click('input[type="submit"]')
        # validate that we are redirected to /login with appropriate error message
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/login?message=password+format+is+incorrect')

    @patch('qa327.backend.register_user', return_value=None)
    def test_register_username_validation(self, *_):
        """
        **Test Case R2.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.**
        AND
        **Test Case R2.8 - User name has to be longer than 2 characters and less than 20 characters.**

        Mocking:

        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - for each name in invalid_usernames:
        - fill the #email, #password and #password2 fields with valid inputs
        - enter an invalid username into the #name element
        - click element input[type='submit']
        - validate that the current page is /login with a #message element containing the text '{} format is incorrect.'.format(the_corresponding_attribute)
        """

        # open /logout
        self.open(base_url + '/logout')
        
        # test all invalid usernames
        for invalid_input in invalid_usernames:
            # enter invalid password and valid everything else
            self.open(base_url + '/register')
            self.type("#email", valid_email)
            self.type("#name", invalid_input)
            self.type('#password',valid_password)
            self.type('#password2',valid_password)
            # submit the forms
            self.click('input[type="submit"]')
            # validate that we are redirected to /login with appropriate error message
            current_url = self.driver.current_url
            self.assert_equal(current_url,base_url+'/login?message=username+format+is+incorrect',msg=invalid_input)

    @patch('qa327.backend.get_user', return_value=test_user)
    @patch('qa327.backend.register_user', return_value=None)
    def test_register_email_already_exists(self, *_):
        """
        **Test Case R2.10 - If the email already exists, show message 'this email has been ALREADY used'**

        Mocking:

        - Mock backend.get_user to return a test_user instance
        - Mock backend.register_user to return None (which indicates user creation successful)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - enter test_user's email into the #email element
        - enter valid inputs into all other fields
        - click element input[type='submit']
        - validate that the current page is still /register
        - validate that the current page contains a #message element containing text "this email has been ALREADY used"
        """

        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')

        # enter test user's email into the #email element
        self.type("#email", "valid_email@test.com")
        # enter valid inputs into all other fields
        self.type("#name", valid_username)
        self.type('#password',valid_password)
        self.type('#password2',valid_password)
        # submit the forms
        self.click('input[type="submit"]')

        # validate that the current page is still /register
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/register')
        # validate that the current page contains a #message element containing text "this email has been ALREADY used"
        self.assert_text('this email has been ALREADY used','#message',timeout=default_timeout)

    @patch('qa327.backend.get_user', return_value=None)
    @patch('qa327.backend.register_user', return_value=None)
    @patch('qa327.backend.set_balance', return_value=None)
    def test_register_registration_successful(self, *_):
        """
        **Test Case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page**

        Mocking:

        - Mock backend.get_user to return None (which indicates that no user with that email already exists)
        - Mock backend.register_user to return None (which indicates user creation successful)
        - Mock backend.set_balance to return None (which indicates that balance was set successfully)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /register
        - enter new_email, new_name and new_password into the appropriate input elements
        - click element input['type=submit']
        - validate that the current page is /login
        """

        # open /logout
        self.open(base_url + '/logout')
        # open register
        self.open(base_url + '/register')

        # enter new user's info into the appropriate forms
        self.type("#email", new_email)
        self.type("#name", new_name)
        self.type('#password',new_password)
        self.type('#password2',new_password)
        # submit the forms
        self.click('input[type="submit"]')

        # validate that the current page is /login
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/login?message=Registration+successful%2C+please+login+now')
