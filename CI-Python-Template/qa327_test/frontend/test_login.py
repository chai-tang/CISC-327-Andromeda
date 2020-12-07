import pytest
from seleniumbase import BaseCase

from qa327_test.conftest import base_url
from unittest.mock import patch
from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash

test_user = User(
    email='valid_email@test.com',
    name='validuser',
    password=generate_password_hash('123ABCxyz*')
)

wrong_email = 'wrong_email@test.com'
wrong_password = 'WrongP4ss!'

valid_email = 'valid_email@test.com'

valid_password = '123ABCxyz*'

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

default_timeout=1

class FrontEndLoginTest(BaseCase):

    def test_login_exists(self, *_):
        """
        **Test Case R1.1 - If the user hasn't logged in, show the login page**
        AND
        **Test Case R1.2 - the login page has a message that by default says 'please login'**

        Mocking:

        - None

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /
        - validate that the current page is the /login page
        - validate that the current page contains a #message element with text "please login"
        """
        
        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # validate that this page is the login page
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/login')
        # validate that the current page contains a #message element with text "please login"
        self.assert_text('Please login','#message')

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_login_redirect(self, *_):
        """
        **Test Case R1.3 - 	If the user has logged in, redirect to the user profile page**

        Mocking:

        - Mock backend.login_user to return a test_user instance

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - open /login again
        - validate that the current page is /
        """

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter test user credentials to login elements
        self.type("#email",valid_email)
        self.type("#password",valid_password)
        # submit the forms
        self.click('input[type="submit"]')
        # open login page again
        self.open(base_url + '/login')
        current_url = self.driver.current_url
        # validate that the current page is /
        self.assert_equal(current_url,base_url+'/')
    
    def test_login_forms_exist(self, *_):
        """
        **Test Case R1.4 - The login page provides a login form which requests two fields: email and passwords**

        Mocking:

        - None

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - validate that the current page contains a text input element with id #email 
        - validate that this #email element has a label with the text "Email"
        - validate that the current page contains a text input element with id #password
        - validate that this #password element has a label with the text "Password"
        """

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # validate that the email form exists and has correct label
        self.assert_element('#email',timeout=default_timeout)
        self.assert_text('Email','label[for=email]',timeout=default_timeout)
        # validate that the password form exists and has correct label
        self.assert_element('#password',timeout=default_timeout)
        self.assert_text('Password','label[for=password]',timeout=default_timeout)

    def test_login_postrequest(self, *_):
        """
        **Test Case R1.5 - The login form can be submitted as a POST request to the current URL (/login)**

        Mocking:

        - None

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - validate that the current page has a form element
        - validate that this form element has the attribute method="post"
        """

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')

        # validate that the current page has a form element
        self.assert_element('form',timeout=default_timeout)
        # validate that this form element has the attribute method="post"
        method = self.get_attribute('form','method',timeout=default_timeout)
        self.assert_equal(method,'post')

    def test_login_forms_required(self, *_):
        """
        **Test Case R1.6 - Email and password both cannot be empty**

        Mocking:

        - None

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - validate that the #email element has the 'required' attribute
        - validate that the #password element has the 'required' attribute
        """

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # validate that the input elements have the required attribute
        email_required = self.get_attribute('#email','required',timeout=default_timeout)
        self.assert_not_equal(email_required,None)
        password_required = self.get_attribute('#password','required',timeout=default_timeout)
        self.assert_not_equal(email_required,None)
    
    @patch('qa327.backend.login_user', return_value=None)
    def test_login_email_validation(self, *_):
        """
        **Test Case R1.7 - Email has to follow addr-spec defined in RFC 5322**

        Mocking:

        - Mock backend.login_user to return None (indicating a failed login)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter an invalid email into the element #email
        - enter a valid password into the element #password
        - click element input[type="submit"]
        - validate that the current page is still the /login page
        - repeat the previous five steps with all the invalid_emails
        """

        # open /logout
        self.open(base_url + '/logout')
        
        # test all invalid emails
        for invalid_input in invalid_emails:
            # enter invalid email and valid everything else
            self.open(base_url + '/login')
            self.type("#email", invalid_input)
            self.type('#password',valid_password)
            # submit the forms
            self.click('input[type="submit"]')
            # validate that we are redirected to /login with appropriate error message
            current_url = self.driver.current_url
            self.assert_equal(current_url,base_url+'/login')
            message = self.get_text('#message',timeout=default_timeout)
            self.assert_equal(message,"email format incorrect",msg=invalid_input)
        
    @patch('qa327.backend.login_user', return_value=None)
    def test_login_password_validation(self, *_):
        """
        **Test Case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character**

        Mocking:

        - Mock backend.login_user to return None (indicating a failed login)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter a valid email into the element #email
        - enter an invalid password into the element #password
        - click element input[type="submit"]
        - validate that the current page is still the /login page
        - repeat the previous five steps with all the invalid_passwords
        """

        # open /logout
        self.open(base_url + '/logout')
        
        # test all invalid passwords
        for invalid_input in invalid_passwords:
            # enter invalid password and valid everything else
            self.open(base_url + '/login')
            self.type("#email", valid_email)
            self.type('#password',invalid_input)
            # submit the forms
            self.click('input[type="submit"]')
            # validate that we are redirected to /login with appropriate error message
            current_url = self.driver.current_url
            self.assert_equal(current_url,base_url+'/login')
            message = self.get_text('#message',timeout=default_timeout)
            self.assert_equal(message,"password format incorrect",msg=invalid_input)

    @patch('qa327.backend.login_user', return_value=test_user)
    def test_login_success(self, *_):
        """
        **Test Case R1.10 - If email/password are correct, redirect to /**

        Mocking:

        - Mock backend.login_user to return a test_user instance

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - validate that the current page is /
        """

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter test_user's credentials
        self.type("#email", valid_email)
        self.type('#password',valid_password)
        # submit the forms
        self.click('input[type="submit"]')
        # validate that the current page is /
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/')

    @patch('qa327.backend.login_user', return_value=None)
    def test_login_failure(self, *_):
        """
        **Test Case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'**

        Mocking:

        - Mock backend.login_user to return None (indicating a failed login)

        Actions:

        - open /logout (to invalidate any logged-in sessions that may exist)
        - open /login
        - enter test_user's email into element #email
        - enter wrong_password into element #password
        - click element input[type="submit"]
        - validate that the current page is /login with a #message element containing the text "email/password combination incorrect"
        - reload /login
        - enter wrong_email into element #email
        - enter test_user's password into element #password
        - click element input[type="submit"]
        - validate that the current page is /login with a #message element containing the text "email/password combination incorrect"
        """

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter test_user's email with the wrong password
        self.type("#email", valid_email)
        self.type('#password',wrong_password)
        # submit the forms
        self.click('input[type="submit"]')
        # validate that the current page is /login with a #message element containing the text "email/password combination incorrect"
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/login')
        self.assert_text("email/password combination incorrect",'#message')

        # open /logout
        self.open(base_url + '/logout')
        # open login page
        self.open(base_url + '/login')
        # enter test_user's password with the wrong email
        self.type("#email", wrong_email)
        self.type('#password',valid_password)
        # submit the forms
        self.click('input[type="submit"]')
        # validate that the current page is /login with a #message element containing the text "email/password combination incorrect"
        current_url = self.driver.current_url
        self.assert_equal(current_url,base_url+'/login')
        self.assert_text("email/password combination incorrect",'#message')