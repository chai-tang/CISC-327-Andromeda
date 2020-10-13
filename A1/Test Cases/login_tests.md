# Test Cases for /login

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='Test_Frontend99!',
    password=generate_password_hash('test_frontend')
)

wrong_email = 'wrong_email@test.com'
wrong_password = 'WrongP4ss!'

test_tickets = [
    {'name': 't1', 'price': '100'}
]

valid_email = 'valid_email@test.com'

valid_password = '123ABCxyz*'

invalid_emails = [
    'has space@test.com',
    '.startswithperiod@test.com',
    'consecutive..periods@test.com',
    'has\backslash@test.com',
    'has"double"quotes@test.com',
    'wacky)(brackets@test.com',
    '%special&chars#!*^$@gmail.com',
    '😘😘😘@test.com',
    'veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylongemail@test.com',
    '@test.com',
    'nodomain.com',
    '',
    'local@domain',
    'local@-hyphens-.com',
    'local@$special#chars!%^&*.com',
    'local@unscore_domain.com',
    'local@😂😂😂.com',
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
    '',
    '*almostVALID*',
    'almostVALID123',
    '*ALMOSTVALID123*',
    '*almostvalid123*'
]

```

**Test Case R1.1 - If the user hasn't logged in, show the login page**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /
- validate that the current page is the /login page


**Test Case R1.2 - the login page has a message that by default says 'please login'**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- validate that the current page contains a #message element with text "please login"


**Test Case R1.3 - 	If the user has logged in, redirect to the user profile page**

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /login again
- validate that the current page is /


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

**Test Case R1.5 - The login form can be submitted as a POST request to the current URL (/login)**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- validate that the current page has a form element
- validate that this form element has the attribute method="post"

**Test Case R1.6 - Email and password both cannot be empty**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- validate that the #email element has the 'required' attribute
- validate that the #password element has the 'required' attribute
- (later test cases R1.7 and R1.8 will attempt empty inputs)


**Test Case R1.7 - Email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation)**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter an invalid email into the element #email
- enter a valid password into the element #password
- click element input[type="submit"]
- validate that the current page is still the /login page
- repeat the previous five steps with all the invalid_emails

**Test Case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter a valid email into the element #email
- enter an invalid password into the element #password
- click element input[type="submit"]
- validate that the current page is still the /login page
- repeat the previous five steps with all the invalid_passwords


**Test Case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'**

Mocking:

- None

Actions:

- after each invalid email/password test in R1.7 and R1.8:
- validate that the current page is /login with a #message element containing the text "email/password format is incorrect."


**Test Case R1.10 - If email/password are correct, redirect to /**

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- validate that the current page is /


**Test Case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'**

Mocking:

- Mock backend.get_user to return a test_user instance

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

