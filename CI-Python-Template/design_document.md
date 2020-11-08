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
|logout             |Logs out the current user session and redirects to /, which then redirects to /login|
|authenticate       |A wrapper function. Redirects the user to the login page if not logged in.|
|profile            |Handles GET method for /. Renders the profile page.|
|sell_post         	|Handles POST method for /sell. Adds new tickets with the backend using form inputs. Checks for errors in input formatting and listing process.|
|buy_post          	|Handles POST method for /buy. Reduces number of available tickets and user balance using form inputs. Checks for errors in input formatting and ticket purchase process.|
|update_post        |Handles POST method for /update. Changes the parameters of any ticket the user is selling. Checks for errors in input formatting relisting process.|

**Backend Methods**

| Method Name     	| Description and Purpose      	|
|-----------------	|------------------------------	|
|get_user           |Given an email, returns the user associated with that email|
|login_user         |Checks that a given email/password pair match that of an existing user. Returns the user if it does, or None if it doesn't|
|register_user      |Given an email, name, and password, creates a new entry on the database with those values (creates a new user). Hashes the password first. Defaults that user's balance to 0.|
|set_balance        |Given an email and an integer, changes the balance of the user associated with that email to said integer.|
|get_all_tickets    |Retrieves all tickets with an expiration date later than the current day.|
|sell_tickets      	|Given a name, email, quantity, price and expiration date, generates a new ticket and adds it to the database. Returns None if successful.|
|buy_tickets       	|Given a name and a quantity, reduces the amount of the named ticket by the quantity. Returns None if successful.|
|update_tickets    	|Given a name, quantity, price and expiration date, changes the parameters of the named ticket to the given parameters. Returns None if successful.|

**Database Classes**

| Class Name      	| Description and Purpose      	|
|-----------------	|------------------------------	|
|User               |Defines the values of the user database, such that every user entry has exactly one of each value. Values include: id (integer), email (string), password (string), name (string) and balance (integer).|
|Ticket            	|Defines the values of the ticket database, such that every ticket entry has exactly one of each value. Values include: id (integer), name (string), email (string), quantity (integer), price (integer) and expiration_date (integer).                               	|

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
- Each level of testing will have its own folder, named accordingly
- Each folder will contain a number of testing files for testing specific parts of the project relevant to that level

**Order of Test Cases**

1. Frontend Unit Testing (mocking backend)
2. Backend Unit Testing
3. Integration Testing
4. System Testing

**Tools & Techniques**

- Github Actions (For CI and regression testing)
- Pytest (for use with github actions)
- Unit testing, with mocking

**Environments**

- Local environments: Servers run locally on each teammate's personal computer. Includes both mac and windows machines, primarily using Google Chrome.
- Github "cloud" environment: Github servers used when using Github actions. Will primarily use their Linux services.

**Responsibility**

- This project is a collaborative effort, in that all teammates are equally responsible for the quality of the software.
- When resolving specific issues/bugs, teammates are responsible for the part of the codebase they developped:
- R1 & R2: Joshua 
- R3 & R4: Evan 
- R5 & R6: Alina
- R7 & R8: Sam

**Budget Management**

- Github Actions will be done only when a pull request is reviewed by another teammate
- All pull requests (and subsequent testing) MUST be reviewed by at least one other teammate before merging
- These reviews will include checking how many minutes are left for the given period, and evaluating how much of that time can be spared
- Avoiding making too many minor pull requests when possible, prioritizing the use of fewer but larger pulls.
- Primarily using Linux minutes (in Github Actions) to maximize time efficiency 
- $0 spending limit on actions to prevent going over allocated time limits
