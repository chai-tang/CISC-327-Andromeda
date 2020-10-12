#Test Cases for /sell

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
'''

**Test Case R4.1 - The name of the ticket must be alphanumeric with space allowed only if it is not the first character**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- enter an invalid name into the #name field of the #sell_tickets form
- enter a valid quantity into the #quantity field of the #sell_tickets form
- enter a valid price into the #price field of the #sell_tickets form
- enter a valid date into the #expiration_date field of the #sell_tickets form
- click element input[type="submit"]
- repeat above steps for each invalid and valid name

**Test Case R4.2 - The name of the ticket must be no longer than 60 characters
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- enter a too long name into the #name field of the #sell_tickets form
- enter a valid quantity into the #quantity field of the #sell_tickets form
- enter a valid price into the #price field of the #sell_tickets form
- enter a valid date into the #expiration_date field of the #sell_tickets form
- click element input[type="submit"]
- repeat above steps for a valid name

**Test Case R4.3 - The quantity of the tickets has to be more than 0 and less than or equal to 100**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- enter an invalid quantity into the #quantity field of the #sell_tickets form
- enter a valid name into the #name field of the #sell_tickets form
- enter a valid price into the #price field of the #sell_tickets form
- enter a valid date into the #expiration_date field of the #sell_tickets form
- click element input[type="submit"]
- repeat above steps for each invalid and valid quantity

**Test Case R4.4 - The price must be in the range [10,100]**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- enter an invalid price into the #price field of the #sell_tickets form
- enter a valid name into the #name field of the #sell_tickets form
- enter a valid quantity into the #quantity field of the #sell_tickets form
- enter a valid date into the #expiration_date field of the #sell_tickets form
- click element input[type="submit"]
- repeat above steps for each invalid and valid price

**Test Case R4.5 - The date must be given in the format YYYYMMDD**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- enter an invalid date into the #expiration_date field of the #sell_tickets form
- enter a valid name into the #name field of the #sell_tickets form
- enter a valid quantity into the #quantity field of the #sell_tickets form
- enter a valid price into the #price field of the #sell_tickets form
- click element input[type="submit"]
- repeat above steps for a valid date

**Test Case R4.6 - For any errors, redirect back to / and show an error message**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
Actions:
- open /
- enter an invalid name into the #name field of the #sell_tickets form
- enter a valid quantity into the #quantity field of the #sell_tickets form
- enter a valid price into the #price field of the #sell_tickets form
- enter a valid date into the #expiration_date field of the #sell_tickets form
- click element input[type="submit"]
- verify that the current page is /
- verify that the current page contains a #message element with the text "Error: Invalid Ticket Sale"

**Test Case R4.7 - The added new ticket information will be posted on the user profile page**
Mocking:
- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets
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
