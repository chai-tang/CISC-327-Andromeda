# Test Cases for /buy

Test Data:
```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)

test_tickets = [
    {'name': 't1', 'quantity': 1, 'contact': 'seller@test.com', 'price': 100},
    {'name': 't2', 'quantity': 100, 'contact': 'seller2@test.com', 'price': 10}
]

valid_names = [
    't3',
	't3 Name'
]

invalid_names = [
    ' t3',
	't3:',
    't3 '
]

lenghty = 'veryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryveryverylongname'

non_lenghty = 'notverylongname'

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

```

**Test Case R6.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R6.2 - The name of the ticket is no longer than 60 characters**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R6.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R6.4 - The ticket name exists in the database and the quantity is more than the quantity requested to buy**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R6.5 - The user has more balance than the ticket price * quantity + service fee (35%) + tax (5%)**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

Actions:

- open / 
- enter a valid name into element #name
- enter a valid quantity into element #quantity
- click element input[type="submit"]
- validate that the user balance is greater than the ticket price * quantity + service fee (35%) + tax (5%)

**Test Case R6.6 - For any errors, redirect back to / and show an error message**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

Actions:

- open /
- for any of the above test cases that cause an error
- validate that the current page is /
- validate that the current page contains a #message element with the text "Error: Invalid Ticket Purchase"