# Assignment 1 : Frontend Test Cases

| Specification | Test Case ID | Purpose of Test Case |
|---------------|--------------|----------------------|
| If the user hasn't logged in, show the login page | R1.1 | Check that /login is the default page when not logged in |
| the login page has a message that by default says 'please login' | R1.2 | Check that the login page displays the correct login prompt |
| If the user has logged in, redirect to the user profile page | R1.3 | Check that users who are already logged in cant login again |
| The login page provides a login form which requests two fields: email and passwords | R1.4 | Check that the user can enter their email and password |
| The login form can be submitted as a POST request to the current URL (/login) | R1.5 | Check that the login forms can use the post method |
| Email and password both cannot be empty | R1.6 | Check that the login forms cant be submitted when empty |
| Email has to follow addr-spec defined in RFC 5322  | R1.7 | Check that non RFC5322 conforming inputs cant be submitted as emails |
| Password has to meet the required complexity | R1.8 | Check that any strings failing to meet the complexity requirements cant be submitted as passwords |
| For any formatting errors, render the login page and show the message 'email/password format is incorrect.' | R1.9 | Check that the login message changes whenever a formatting error occurs |
| If email/password are correct, redirect to / | R1.10 | Check that registered users are able to login properly |
| Otherwise, redict to /login and show message 'email/password combination incorrect' | R1.11 | Check that login fails if the wrong email/password is entered, and that the login message changes to reflect this error |
|-|-|-|
| If the user has logged in, redirect back to the user profile page / | R2.1 | Check that already logged in users cant register again |
| otherwise, show the user registration page | R2.2 | Check that non-logged in users are able to reach the registration page |
| the registration page shows a registration form requesting: email, user name, password, password2 | R2.3 | Check that the required input forms exist on this page |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.4 | Check that the registration forms can use the post method |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5 | Check that registration fails if any of the forms have been filled with invalid inputs |
| Password and password2 have to be exactly the same | R2.6 | Check that registration fails if the password form inputs are not identical |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.7 | Check that registration fails if the username fails to meet the requirements |
| User name has to be longer than 2 characters and less than 20 characters. | R2.8 | Check that registration fails if the username fails to meet minimum/maximum length requirements |
| For any formatting errors, redirect back to /login and show message 'format is incorrect' | R2.9 | Ensure that the correct error message is shown when registration fails |
| If the email already exists, show message 'this email has been ALREADY used' | R2.10 | Check that the user cannot register with an email that has already been registered |
| If no error, create a new user, set the balance to 5000, and go back to the /login page  | R2.11 | Check that the app is able to register new users |
|-|-|-|
| If the user is not logged in, redirect to login page | R3.1 | Check that the user cannot access the page when not logged in |
| This page shows a header 'Hi {}'.format(user.name) | R3.2 | Check that the page shows the user who they are logged in as |
| This page shows user balance. | R3.3 | Check that the user can see their balance |
| This page shows a logout link, pointing to /logout | R3.4 | Check that the user can log out|
| This page lists all available tickets. | R3.5 | Ensure that content displays correctly |
| This page contains a form that a user can submit new tickets for sell. | R3.6 | Check that there is a for for submitting new tickets |
| This page contains a form that a user can buy new tickets. | R3.7 | Check that there is a form for buying tickets |
| The ticket-selling form can be posted to /sell | R3.8 | Check that the selling form works |
| The ticket-buying form can be posted to /buy | R3.9 | Check that the buying form works |
| The ticket-update form can be posted to /update | R3.10 | Check that the user can update tickets through the selling form |
|-|-|-|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R4.1 | Ensures the ticket name fits the requirements |
| The name of the ticket is no longer than 60 characters | R4.2 | Ensures the ticket is not too long |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R4.5 | Check that there are tickets available, and that there are not too many |
| Price has to be of range [10, 100] | R4.6 | Check that the ticket is priced correctly |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R4.7 | Ensure that the date is formatted correctly |
| For any errors, redirect back to / and show an error message | R4.8 | Ensure the app can handle errors |
| The added new ticket information will be posted on the user profile page | R4.9 | Check that the new ticket is added to the list of available tickets |
|-|-|-|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R5.1 | Ensures that ticket name is alphanumeric-only and has no leading or trailing spaces. |
| The name of the ticket is no longer than 60 characters | R5.2 | Ensures that ticket name does not exceed maximum length.|
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R5.3 | Ensures that the ticket quantity is in the valid range.|
| Price has to be of range [10, 100] | R5.4 | Ensures that the ticket price is in the valid range.|
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R5.5 | Ensures that the ticket expiration date is in the valid format.|
| The ticket of the given name must exist | R5.6 | Ensures that the ticket name exists in the database.|
| For any errors, redirect back to / and show an error message | R5.7 | Check that an error message is displayed if any of the above requirements are not met.|
|-|-|-|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R6.1 | Ensures that ticket name is alphanumeric-only and has no leading or trailing spaces.|
| The name of the ticket is no longer than 60 characters | R6.2 | Ensures that ticket name does not exceed maximum length.|
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R6.3 | Ensures that the ticket quantity is in the valid range.|
| The ticket name exists in the database and the quantity is more than the quantity requested to buy | R6.4 | Ensures that the ticket name exists in the database and the quantity available is greater than the quantity requested.|
| The user has more balance than the ticket price * quantity  + service fee (35%) + tax (5%) | R6.5 | Ensures that the user has enough funds available to purchase the ticket.|
| For any errors, redirect back to / and show an error message | R6.6 | Check that an error message is displayed if any of the above requirements are not met.|
|-|-|-|
| Logout will invalid the current session and redirect to the login page. | R7.1 | 
|-|-|-|
| For any other requests except the ones above, the system should return a 404 error | R8.1 | |


**How did your team organize the documentations of the test cases (e.g. where did you store the test case markdown file for each team member).**

All the test cases are stored in a folder called 'Test Cases'. The test cases in this folder are divided into markdown files based on the category of cases they cover. For example, the R1 /login test cases are in a folder called 'login_tests.md'. 

Josh: R1 and R2 (/login and /register)

Evan: R3 and R4 (/ and /sell)

Alina: R5 and R6 (/update and /buy)

Sam: R7 and R8 (/logout and /*)

**Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.**

Test cases will be automatically run on whenever a pull request is made, checking if the new additions will cause the app to fail any test cases.

**How are you going to organize different test case code files? (a folder for a specification?)**

Test case code files will be organized similarly to the test case markdown files: A single folder will contain all the frontend test cases, divided into separate appropriately named files according to the category of tests implemented.
