# Test Cases for /register

Test Data:
```
test_user = User(
    email='valid_email@test.com',
    name='validuser',
    password=generate_password_hash('123ABCxyz*')
)

test_tickets = [
    {'name': 't1', 'price': '100'}
]

valid_email = 'valid_email@test.com'

valid_password = '123ABCxyz*'
valid_password2 = '456DEFpqr#'

valid_username = 'validuser'

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

invalid_usernames = [
    'special!@#$%^&*char',
    ' firstspace',
    'lastspace ',
    '',
    '\backslash',
    'double"quotes"',
    '😂😂😂😂',
    'a',
    'more_than_twenty_characters_long'
]

new_email = 'new@test.com'
new_name = 'mr new'
new_password = 'New123!'

new_user = User(
    email='new@test.com',
    name='mr new',
    password='New123!'
)

```

**Test Case R2.1 - If the user has logged in, redirect back to the user profile page /**

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /login
- enter test_user's email into element #email
- enter test_user's password into element #password
- click element input[type="submit"]
- open /register
- validate that the current page is /


**Test Case R2.2 - otherwise, show the user registration page**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- validate that the current page is /register


**Test Case R2.3 - the registration page shows a registration form requesting: email, user name, password, password2**

Mocking:

- None

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


**Test Case R2.4 - The registration form can be submitted as a POST request to the current URL (/register)**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- validate that the current page has a form element
- validate that this form element has the attribute method="post"


**Test Case R2.5 - Email, password, password2 all have to satisfy the same required as defined in R1**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- validate that the #email, #password and #password2 elements all have the 'required' attribute
- for each of #email and #password/#password2:
- open /register
- fill all other input fields with valid inputs
- enter an invalid input into this field
- click element input[type="submit"]
- validate that the current page is /login with a #message element containing the text '{} format is incorrect.'.format(the_corresponding_attribute)
- do this for all the invalid_emails and invalid_passwords


**Test Case R2.6 - 	Password and password2 have to be exactly the same**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- fill the #email and #name fields with valid inputs
- enter valid_password into the #password element
- enter valid_password2 into the #password2 element
- click element input[type="submit"]
- validate that the current page is /login with a #message element containing the text '{} format is incorrect.'.format(the_corresponding_attribute)


**Test Case R2.7 - User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character.**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- for each name in invalid_usernames:
- fill the #email, #password and #password2 fields with valid inputs
- enter an invalid username into the #name element
- click element input[type='submit']
- validate that the current page is /login with a #message element containing the text '{} format is incorrect.'.format(the_corresponding_attribute)

**Test Case R2.8 - User name has to be longer than 2 characters and less than 20 characters.**

Mocking:

- None

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- for each name in invalid_usernames:
- fill the #email, #password and #password2 fields with valid inputs
- enter a username that is more than 20 characters long into the #name element
- click element input[type='submit']
- validate that the current page is still /register
- reload /register
- fill the #email, #password and #password2 fields with valid inputs
- enter a username that is less than 2 characters long into the #name element
- click element input[type='submit']
- validate that the current page is /login with a #message element containing the text '{} format is incorrect.'.format(the_corresponding_attribute)

**Test Case R2.9 - For any formatting errors, redirect back to /login and show message '{} format is incorrect.'.format(the_corresponding_attribute)**

Mocking:

- None

Actions:

- this requirement is covered in test cases R2.5-8 


**Test Case R2.10 - If the email already exists, show message 'this email has been ALREADY used'**

Mocking:

- Mock backend.get_user to return a test_user instance

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- enter test_user's email into the #email element
- enter valid inputs into all other fields
- click element input[type='submit']
- validate that the current page is still /register
- validate that the current page contains a #message element containing text "this email has been ALREADY used"


**Test Case R2.11 - If no error regarding the inputs following the rules above, create a new user, set the balance to 5000, and go back to the /login page**

Mocking:

- Mock backend.get_user to return a newly created user
- Mock backend.get_balance to return a user's balance on the / page

Actions:

- open /logout (to invalidate any logged-in sessions that may exist)
- open /register
- enter new_email, new_name and new_password into the appropriate input elements
- click element input['type=submit']
- validate that the current page is /login
- enter the new credentials into the appropriate input elements of /login
- validate that the current page is /
- validate that the current balance is 5000
- delete this new test user from the system to ensure this test works the next time it's run





