# Assignment 1 : Frontend Test Cases

| Specification | Test Case ID | Purpose of Test Case |
|---------------|--------------|----------------------|
| If the user hasn't logged in, show the login page | R1.1 | |
| the login page has a message that by default says 'please login' | R1.2 | |
| If the user has logged in, redirect to the user profile page | R1.3 | |
| The login page provides a login form which requests two fields: email and passwords | R1.4 | |
| The login form can be submitted as a POST request to the current URL (/login) | R1.5 | |
| Email and password both cannot be empty | R1.6 | |
| Email has to follow addr-spec defined in RFC 5322  | R1.7 | |
| Password has to meet the required complexity | R1.8 | |
| For any formatting errors, render the login page and show the message 'email/password format is incorrect.' | R1.9 | |
| If email/password are correct, redirect to / | R1.10 | |
| Otherwise, redict to /login and show message 'email/password combination incorrect' | R1.11 | |
|---------------|--------------|----------------------|
| If the user has logged in, redirect back to the user profile page / | R2.1 | |
| otherwise, show the user registration page | R2.2 | |
| the registration page shows a registration form requesting: email, user name, password, assword2 | R2.3 | |
| The registration form can be submitted as a POST request to the current URL (/register) | R2.4 | |
| Email, password, password2 all have to satisfy the same required as defined in R1 | R2.5 | |
| Password and password2 have to be exactly the same | R2.6 | |
| User name has to be non-empty, alphanumeric-only, and space allowed only if it is not the first or the last character. | R2.7 | |
| User name has to be longer than 2 characters and less than 20 characters. | R2.8 | |
| For any formatting errors, redirect back to /login and show message 'format is incorrect' | R2.9 | |
| If the email already exists, show message 'this email has been ALREADY used' | R2.10 | |
| If no error, create a new user, set the balance to 5000, and go back to the /login page  | R2.11 | |
|---------------|--------------|----------------------|
| If the user is not logged in, redirect to login page | R3.1 | |
| This page shows a header 'Hi {}'.format(user.name) | R3.2 | |
| This page shows user balance. | R3.3 | |
| This page shows a logout link, pointing to /logout | R3.4 | |
| This page lists all available tickets. | R3.5 | |
| This page contains a form that a user can submit new tickets for sell. | R3.6 | |
| This page contains a form that a user can buy new tickets. | R3.7 | |
| The ticket-selling form can be posted to /sell | R3.8 | |
| The ticket-buying form can be posted to /buy | R3.9 | |
| The ticket-update form can be posted to /update | R3.10 | |
|---------------|--------------|----------------------|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R4.1 | |
| The name of the ticket is no longer than 60 characters | R4.2 | |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R4.5 | |
| Price has to be of range [10, 100] | R4.6 | |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R4.7 | |
| For any errors, redirect back to / and show an error message | R4.8 | |
| The added new ticket information will be posted on the user profile page | R4.9 | |
|---------------|--------------|----------------------|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R5.1 | |
| The name of the ticket is no longer than 60 characters | R5.2 | |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R5.3 | |
| Price has to be of range [10, 100] | R5.4 | |
| Date must be given in the format YYYYMMDD (e.g. 20200901) | R5.5 | |
| The ticket of the given name must exist | R5.6 | |
| For any errors, redirect back to / and show an error message | R5.7 | |
|---------------|--------------|----------------------|
| The name of the ticket has to be alphanumeric-only, and space allowed only if it is not the first or the last character. | R6.1 | |
| The name of the ticket is no longer than 60 characters | R6.2 | |
| The quantity of the tickets has to be more than 0, and less than or equal to 100. | R6.3 | |
| The ticket name exists in the database and the quantity is more than the quantity requested to buy | R6.4 | |
| The user has more balance than the ticket price * quantity  + service fee (35%) + tax (5%) | R6.5 | |
| For any errors, redirect back to / and show an error message | R6.6 | |
|---------------|--------------|----------------------|
| Logout will invalid the current session and redirect to the login page. | R7.1 | 
|---------------|--------------|----------------------|
| For any other requests except the ones above, the system should return a 404 error | R8.1 | |


**How did your team organize the documentations of the test cases (e.g. where did you store the test case markdown file for each team member).**

All the test cases are stored in a folder called 'Test Cases'. The test cases in this folder are divided into markdown files based on the category of cases they cover. For example, the R1 /login test cases are in a folder called 'login_tests.md'. 

Josh: R1 and R2 (/login and /register)
Evan: R3 and R4 (/ and /sell)
Alina: R5 and R6 (/update and /buy)
Sam: R7 and R8 (/logout and /*)

**Your understanding of how the chosen testing framework works to test the frontend, including your understandings of when and how the test cases will be running directly on GitHub.**

-answer-

**How are you going to organize different test case code files? (a folder for a specification?)**

Test case code files will be organized similarly to the test case markdown files: A single folder will contain all the frontend test cases, divided into separate appropriately named files according to the category of tests implemented.