# Test Cases for /update

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

valid_date = 20201222

invalid_date = '2020 12 22'

```

**Test Case R5.1 - The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R5.2 - The name of the ticket is no longer than 60 characters**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R5.3 - The quantity of the tickets has to be more than 0, and less than or equal to 100**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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


**Test Case R5.4 - Price has to be of range [10, 100]**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R5.5 - Date must be given in the format YYYYMMDD (e.g. 20200901)**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

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

**Test Case R5.6 - The ticket of the given name must exist**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

Actions:

- open /
- enter a name that does not exist in list of all available tickets into the element #name
- click element input[type="submit"]
- validate that it causes an error
- enter a name that does exist in list of all available tickets into the element #name
- click element input[type="submit"]
- validate that it does not cause an error

**Test Case R5.7 - For any errors, redirect back to / and show an error message**

Mocking:

- Mock backend.get_user to return a test_user instance
- Mock backend.get_tickets to return a list of all available tickets

Actions:

- open /
- for any of the above test cases that cause an error
- validate that the current page is /
- validate that the current page contains a #message element with the text "Error: Invalid Ticket Update"