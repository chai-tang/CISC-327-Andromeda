# Assignment 2 Design Document:

**Instructions:**

A design document in PDF or perferablly the markdown format for your project, giving the overall structure of your solution, showing the classes and methods as a diagram or table, with a brief (one sentence) description of the intention of each.

**Frontend Methods**

| Method Name     	| Description and Purpose      	|
|-----------------	|------------------------------	|
|register_get       |Handles GET methods for /register. Renders the default registration message.|
|register_post      |Handles POST methods for /register. Registers new users with the backend using form inputs. Checks for errors in input formatting and registration process.|
|login_get          |Handles GET methods for /login. Renders the default login message.|
|login_post         |Handles POST methods for /login. Logs users into the homepage after verifying that form inputs match an existing user, and checks for errors in formatting. |
|logout             |                              	|
|authenticate       |                              	|
|profile            |                              	|
|                 	|                              	|
|                 	|                              	|

**Backend Methods**

| Method Name     	| Description and Purpose      	|
|-----------------	|------------------------------	|
|get_user           |Given an email, returns the user associated with that email|
|login_user         |Checks that a given email/password pair match that of an existing user. Returns the user if it does, or None if it doesn't|
|register_user      |Given an email, name, and password, creates a new entry on the database with those values (creates a new user). Hashes the password first. Defaults that user's balance to 0.|
|set_balance        |Given an email and an integer, changes the balance of the user associated with that email to said integer.|
|get_all_tickets    |                              	|
|                 	|                              	|
|                 	|                              	|
|                 	|                              	|
|                 	|                              	|

**Database Classes**

| Class Name      	| Description and Purpose      	|
|-----------------	|------------------------------	|
|User               |Defines the values of the user database, such that every user entry has exactly one of each value. Values include: id (integer), email (string), password (string), name (string) and balance (integer).|
|                 	|                              	|
|                 	|                              	|
|                 	|                              	|

# Test Plan:

**Instructions:**

- Detailed Test Plan
  - How test cases of different levels (frontend, backend units, integration) are organized.
  - The order ot the test cases (which level first which level second).
  - Techniques and tools used for testing.
  - Environemnts (all the local environment and the cloud environment) for the testing.
  - Responsibility (who is responsible for which test case, and in case of failure, who should you contact)
  - Budget Management (you have limited CI action minutes, how to monitor, keep track and minimize unncessary cost)

**Test Case Organization**

- Test cases are organized within the qa327_test folder of the template, which is itself sorted into a number of subfolders
- Each level of testing (frontend, backend, and integration) will have its own folder
- Each folder  will contain a number of testing files for testing specific parts of the project relevant to that level

**Order of Test Cases**

1. Frontend (mocking backend)
2. Backend
3. Integration

**Tools & Techniques**

- Github Actions 
- Pytest

**Environments**

- Local environments: Tests done with servers run locally on each teammate's personal computer
- Github "cloud" environment: Tests done on the Github servers using Github actions. Will primarily use their Linux actions services.

**Responsibility**

- R1 & R2: Joshua 
- R3 & R4: Evan 
- R5 & R6: Alina
- R7 & R8: Sam

**Budget Management**

- Actions will be done only when a pull request is reviewed by another teammate
- All pull requests (and subsequent Github actions testing) thus MUST be reviewed by at least one other teammate before merging
- These reviews will include checking how many minutes are left for the given period, and evaluating how much of that time can be spared
- Avoiding making too many minor pull requests when possible, prioritizing the use of fewer but larger pulls.
- Primarily using Linux minutes to maximize time efficiency 
- $0 spending limit on actions to prevent going over allocated time limits

