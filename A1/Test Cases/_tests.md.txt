# Test Cases for /

Test Data:
'''
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_tickets = [
    {'name': 't1', 'quantity': 1, 'contact': 'seller@test.com', 'price': 50},
	{'name': 't2', 'quantity': 1, 'contact': 'test_frontend@test.com', 'price':50}
]
'''
**Test Case R3.1 - If the user is not logged in, redirect to login page**
Mocking:
- None
Actions:
- open /
- validate that the current page is the /login page

**Test Case R3.2 - Show a header 'Hi {}'.format(user.name)**
Mocking:
- Mock backend.get_user to return a test_user instance
Actions:
- open /
- validate that the current page contains a #header element with text "Hi test_frontend" 

**Test Case R3.3 - Show user balance**
Mocking:
- Mock backend.get_user to return a test_user instance
Actions:
- open /
- validate that the current page contains a #message element with text "User Balance: $0.00"

**Test Case R3.4 - Show a logout link, lointing to /logout**
Mocking:
- Mock backend.get_user to return a test_user instance
Actions:
- open /
- validate that the current page contains a #link element
- validate that the #link element points to /logout

**Test Case R3.5 - Show all available tickets**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- validate that the current page contains a #table element
- validate that the #table element has a #tableheader element with text "Name"
- validate that the #table element has a #tableheader element with text "Quantity"
- validate that the #table element has a #tableheader element with text "Contact"
- validate that the #table element has a #tableheader element with text "Price"
- validate that the #table element has a #tabledata element with text 't1'
- validate that the #table element has a #tabledata element with text ''
- validate that the #table element has a #tabledata element with text ''
- validate that the #table element has a #tabledata element with text ''

**Test Case R3.6 - Show a form for submitting new tickets**
Mocking:
- Mock backend.get_user to return a test_user instance
Actions:
- open /
- validate that the current page contains a form element with label "Sell Tickets"
- validate that this form element has the field "Name"
- validate that this form element has the field "Quantity"
- validate that this form element has the field "Price"
- validate that this form element has the field "Expiration Date"

**Test Case R3.7 - Show a form for buying tickets**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- validate that the current page contains a form element with label "Buy Tickets"
- validate that this form element has the field "Name"
- validate that this form element has the field "Quantity"

**Test Case R3.8 - The ticket-selling form can be posted to /sell**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- validate that the current page contains a form element with label "Sell Tickets"
- validate that the form element has the attribute method="post"
- validate that the form element can be posted to /sell

**Test Case R3.9 - The ticket-buying form can be posted to /buy**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- validate that the current page contains a form element with label "Buy Tickets"
- validate that the form element has the attribute method="post"
- validate that the form element can be posted to /buy

**Test Case R3.10 - The ticket-update form can be posted to /update**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- validate that the current page contains a form element with label "Sell Tickets"
- validate that the form element has the attribute method="post"
- validate that the form element can be posted to /update
