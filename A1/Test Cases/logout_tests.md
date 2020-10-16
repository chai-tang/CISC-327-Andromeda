# Test Cases for /logout

Test data:

```
test_user = User(
    email='test_frontend@test.com',
    name='test_frontend',
    password=generate_password_hash('test_frontend')
)
```

**Test Case R7.1 - Logout will invalidate the current session and redirect to the login page**

Mocking:

- None

Actions:

- The user visits or submit a form to /logout
- The server invalidate any user sessions if they exist. If the user is already logged out, there are no sessions to invalidate
- The page redirects to /login

**Test Case R7.2 - After logout, the user shouldn't be able to access restricted pages**

Additional test data:

```
test_tickets = [
    {'name': 't1', 'quantity': 1, 'contact': 'seller@test.com', 'price': 100},
    {'name': 't2', 'quantity': 100, 'contact': 'seller2@test.com', 'price': 10}
]
```

Mocking:

- None

Actions:

- The user visits `/`
- The page should redirect to `/login`
- The user visits `/register`
- The page should go to `/register`, no redirects
- The user visits `/login`
- The page should go to `/login`, no redirects
- The user visits `/logout`
- The server should have no user sessions to invalidate, so the page should redirect to `/login`
- The user sends a `POST` request manually containing a valid user and tickets to `/buy`
- The page should redirect to `/login`. Nothing should be done to the backend.
- The user sends a `POST` request manually containing a valid user and tickets to `/sell`
- The page should redirect to `/login`. Nothing should be done to the backend.
- The user sends a `POST` request manually containing a valid user and tickets to `/update`
- The page should redirect to `/login`. Nothing should be done to the backend.
