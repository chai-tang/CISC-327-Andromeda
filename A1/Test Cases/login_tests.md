# Test Cases for Login and Register

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_tickets = [
    {'name': 't1', 'price': '100'}
]

```

**Test Case R1.1 - If the user hasn't logged in, show the login page**

-some text idk-

**Test Case R1.2 - the login page has a message that by default says 'please login'**

-some text idk-

**Test Case R1.3 - 	If the user has logged in, redirect to the user profile page**

-some text idk-

**Test Case R1.4 - The login page provides a login form which requests two fields: email and passwords**

-some text idk-


**Test Case R1.5 - The login form can be submitted as a POST request to the current URL (/login)**

-some text idk-


**Test Case R1.6 - Email and password both cannot be empty**

-some text idk-


**Test Case R1.7 - Email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for a human-friendly explanation)**

-some text idk-


**Test Case R1.8 - Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, and at least one special character**

-some text idk-


**Test Case R1.9 - For any formatting errors, render the login page and show the message 'email/password format is incorrect.'**

-some text idk-


**Test Case R1.10 - If email/password are correct, redirect to /**

-some text idk-


**Test Case R1.11 - Otherwise, redict to /login and show message 'email/password combination incorrect'**

-some text idk-

