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

-insert detailed test plan here-