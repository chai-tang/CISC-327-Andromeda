# Test Cases for `/*`

Test data:

```
valid_paths = [
    '/',
    '/login',
    '/register',
    '/logout',
    '/buy',
    '/sell',
    '/update'
]

invalid_paths = [
    '/asdfasdfasdfdasdf',
    '/%20',
    '/-------'
]

invalid_paths_special = [
    '/.htaccess',
    '/.htpasswd',
    '/.htblablabla'
]

```

**Test Case R8 - For any other requests, the system should return a 404 error**

Mocking:

- None

Actions:

- The user visits a valid path in `valid_paths`
- The page should go to the corresponding path. If a redirection is needed, the page should redirect to the page needed
- The user visits an invalid path in `invalid_paths`
- The page should show an error message and the browser should receive an `HTTP 404` response
- The user visits an invalid path in `invalid_paths_special`
- Depending on the server configuration, the browser might receive an `HTTP 403` and it's okay
