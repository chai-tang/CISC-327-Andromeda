# Assignment 5 Failure Report

## Section 1: Changes made to Test Cases

Summary of all changes made to test cases / test data since assignment 1 submission:

| Test Case Number 	| Purpose of Test Case(s) | Changes Made   	     | Reason for Changes  	 |
|------------------	|-----------------------  |--------------------- |---------------------- |
|R4|Test ticket selling|Added mocking for bn.login_user and bn.sell_tickets to most test cases|Users must be logged in to sell tickets, so the login process must be mocked to conduct these tests. Ticket selling method must also be mocked, for obvious reasons|
|R5|Test ticket updating|Added mocking for bn.login_ugser and bn.update_tickets to most test cases|Same reasoning as above|
|R6|Test ticket buying|Added mocking for bn.login_user and bn.buy_tickets to most test cases|Same reasoning as above|
|R4.6|Test that failures during ticket selling display error messages|Removed this test case entirely|Error message validation has been merged into the relevant test cases, so there is no longer any need for this to be a separate test case.|
|R5.7|Test that failures during ticket updating display error messages|Removed this test case entirely|Same reasoning as above|
|R6.6|Test that failures during ticket buying display error messages|Removed this test case entirely|Same reasoning as above|
|R6.5|Test that users must have enough balance to buy tickets|Added testing for a successful (valid) purchase. Added mocking for bn.set_balance|In A1 this only tested for failure, but now it also tests for success as to improve coverage. Also, it now mocks set_balance as it should.|

## Section 2: Test Case Failures

Documentation for every test case that failed, and the resulting fixes made:

### R4 Sell Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|R4.X|Testing ticket selling|All test cases had issues with submitting forms due to lack of unique identifiers for different submit buttons on the homepage|Added unique ID's for each of the submit buttons in index.html|
|R4.1|Validating that ticket names must be alphanumeric to be sold|Ticket with an illegal name "t3:" was accepted|Updated the ticket name validation regex in frontend.py|
|R4.3|Validating maximum quantity of tickets that can be sold|Ticket with an illegal quantity '101' was accepted|Updated the ticket quantity validation regex in frontend.py|
|R4.4|Validating that ticket price is in range [10, 110]|Ticket with an illegal price '111' was accepted|Updated the ticket price validation regex in frontend.py|
|R4.7|Validating that newly posted tickets are displayed on the homepage|Test was unable to find the new ticket information on the homepage due to lack of unique identifier|Added class="ticket" to the ticket elements in index.html|

### R5 Update Tests:
| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|R5.1|Validating that ticket names must be alphanumeric|The update method in frontend has no name validation|Added name validation using regex, same as in /sell. Technically this isn't really needed because it shouldn't even be possible to sell a ticket with an illegal name, but if the specifications ask for this functionality then we have to have it. Also made input validation occur earlier in this method.|
|R5.7|Validating that tickets must exist to be updated|Mocking get_all_tickets() threw a number of errors due to /update implementation in frontend|Changed the way that /update finds the desired ticket in frontend. See the "A5 setup" pull request for details.|

### R6 Buy Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|----|----|----|---|
|R6.1|Validating that ticket names must be alphanumeric|The buy method in frontend has no name validation|Added name validation using regex, same as in /sell. Also made input validation occur earlier in this method.|
|R6.4|Validating that ticket name must exist to be purchased|"No such ticket __" message did not display the name of the desired ticket after a failed purchase|Fixed the error message to properply display the buy_name when said ticket could not be found|
|R6.4-5|Validating that tickets must exist / be affordable by user to be purchased|Mocking get_all_tickets() threw a number of errors due to /buy implementation in frontend|Changed the way that /buy finds the desired tickets in frontend. See the "A5 setup" pull request for details.|

### Integration Tests:

| Test Case Number | Purpose of Test Case | Cause of Failure | Fixes Made |
|----|----|----|---|
|R6.X|Testing ticket purchase|Directly adding tickets to the database caused an exception. |Repeated the sell process to add desired test ticket before buying said ticket. |
