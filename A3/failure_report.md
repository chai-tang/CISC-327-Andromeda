# Assignment 3 Failure Report

## Section 1: Changes made to Test Cases

Summary of all changes made to test cases / test data since assignment 1 submission:

| Test Case Number 	| Purpose of Test Case(s) | Changes Made   	     | Reason for Changes  	 |
|------------------	|-----------------------  |--------------------- |---------------------- |
|R2.5|Validate email and password inputs in /register|Split into three sub tests: 2.5.1 checks forms are required, 2.5.2 checks email validation, 2.5.3 checks password validation|This specification had too many requirements for just a single test case. Splitting it into multiple smaller cases makes the testing process here much cleaner.|
|R2.5 & R2.7|Validatation of input forms in /register|Removed all test data with emojis. Removed \*almostVALID\* from invalid_passwords test data. Removed local@domain from invalid_emails test data.|Emojis kept crashing the pytest runs, so they had to be removed. I manually tested emojis in the relevant input forms, and they were rejected (as they should be). \*almostVALID\* is actually a valid password, and local@domain is a completely valid email. I've removed these from the test data lists.|
|R2.7 & R2.8|Validate username inputs in /register|Merged 2.7 and 2.8 into one test case|The R2.7 test data for invalid usernames already included names of invalid length, so having a separate test case for R2.8 was redundant.|
|R2.1-11|Testing /register|Adding mocking for backend.register_user to every test case|These are just frontend tests, so user registration should be mocked. This also means that new users don't have to be removed from the database.|
|R2.11|Validate that new users can be registered|Removed testing for login and balance. Adding mocking for backend.set_balance|This case is only supposed to test the /register frontend, so the part that tries to login and check the balance was well outside the intended scope of this test case. That will be covered in backend testing.|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|

## Section 2: Test Case Failures

Documentation for every test case that failed, and the resulting fixes made:

### R1 Login Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|

### R2 Register Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|R2.5.2|Email input validation|Multiple invalid emails were accepted|Completely changed the email validation regex to fit RFC5322 better. Added a length checking regex to email validation process.|
|R2.3|Check that input forms and labels exist|Text element containing "Confirm password" was not labelled "for=password2"|Changed the label to have attribute "for=password2"|
|R2.1|Validate that users who are logged in get redirected to homepage when attempting to access /register|This functionality was not added in the prototype|Added a 'logged_in' check to register_get in frontend.py that redirects to homepage if the user is already logged in.|
|R2.6|Validate that both passwords must be the same|Passwords not matching error does not redirect to /login as the specifications require, instead just showing an error message while staying on the /register page|Added a redirect to /login with appropriate error message to the passwords not matching check. I'm aware this change makes the product even less user friendly, but that's what the specifications say so we're going with it.|
|                  	|                      	|                  	|            	|

### R3 Homepage Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|

### R7 Logout Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|

### R8 /* Tests:

| Test Case Number 	| Purpose of Test Case 	| Cause of Failure 	| Fixes Made 	|
|------------------	|----------------------	|------------------	|------------	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|
|                  	|                      	|                  	|            	|

