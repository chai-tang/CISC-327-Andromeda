from flask import render_template, request, session, redirect, url_for
from qa327 import app
import qa327.backend as bn
import re

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder. 
"""


@app.route('/register', methods=['GET'])
def register_get():
    # templates are stored in the templates folder
    return render_template('register.html', message='Please register')


@app.route('/register', methods=['POST'])
def register_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    password2 = request.form.get('password2')
    login_message = "Please login"

    # regex's to check the inputs against
    # please note that the email pattern doesn't actually work for all RFC5322 emails
    # if you can find a regex that does please replace it and then remove this comment, thanks
    passwordPattern = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*([!-/]|[:-@])).{6,}")
    emailPattern = re.compile("([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\[[\t -Z^-~]*])")
    usernamePattern = re.compile("^[\w][\w| ]{0,18}[\w]$")

    # check that both passwords match
    if password != password2:
        return render_template('register.html', message="passwords do not match")

    # check that the forms all match the required patterns using regular expressions
    elif not(emailPattern.match(email)):
        login_message="email format is incorrect"
    elif not(passwordPattern.match(password)):
        login_message="password format is incorrect"
    elif not(usernamePattern.match(name)):
        login_message="username format is incorrect"

    # if all forms are correct, attempt to register the user
    else:
        user = bn.get_user(email)
        # if the user already exists, send an error message
        if user:
            return render_template('register.html', message="this email has been ALREADY used")
        # if the registration fails for some reason (register_user doesn't return none) send an error message
        elif bn.register_user(email, name, password, password2) != None:
            return render_template('register.html', message="failed to register new user")
        # if no errors occur, set balance to 5000
        else:
            login_message = "Registration successful, please login now"
            if bn.set_balance(email,5000) != None:
                login_message = "Registration successful, but failed to set new balance"
    
    # return to login with the appropriate message
    #return render_template('login.html', message=login_message)
    #return redirect('/login')
    return redirect(url_for('login_get', message=login_message))


@app.route('/login', methods=['GET'])
def login_get():
    # if a message was passed to this function, display that as message. else, display 'Please login'
    passed_message = request.args.get('message')
    if passed_message == None:
        passed_message = 'Please login'
    return render_template('login.html', message=passed_message)


@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    user = bn.login_user(email, password)
    if user:
        session['logged_in'] = user.email
        """
        Session is an object that contains sharing information 
        between browser and the end server. Typically it is encrypted 
        and stored in the browser cookies. They will be past 
        along between every request the browser made to this services.

        Here we store the user object into the session, so we can tell
        if the client has already login in the following sessions.

        """
        # success! go back to the home page
        # code 303 is to force a 'GET' request
        return redirect('/', code=303)
    else:
        passwordPattern = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*([!-/]|[:-@])).{6,}")
        emailPattern = re.compile("([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\[[\t -Z^-~]*])")
        if (not(passwordPattern.match(password))):
            return render_template('login.html', message='password format incorrect')
        elif (not(emailPattern.match(email))):
            return render_template('login.html', message='email format incorrect')
        else:
            return render_template('login.html', message='email/password combination incorrect')


@app.route('/logout')
def logout():
    if 'logged_in' in session:
        session.pop('logged_in', None)
    return redirect('/')


def authenticate(inner_function):
    """
    :param inner_function: any python function that accepts a user object

    Wrap any python function and check the current session to see if 
    the user has logged in. If login, it will call the inner_function
    with the logged in user object.

    To wrap a function, we can put a decoration on that function.
    Example:

    @authenticate
    def home_page(user):
        pass
    """

    def wrapped_inner():

        # check did we store the key in the session
        if 'logged_in' in session:
            email = session['logged_in']
            user = bn.get_user(email)
            if user:
                # if the user exists, call the inner_function
                # with user as parameter
                return inner_function(user)
        else:
            # else, redirect to the login page
            return redirect('/login')

    # return the wrapped version of the inner_function:
    return wrapped_inner


@app.route('/')
@authenticate
def profile(user):
    # authentication is done in the wrapper function
    # see above.
    # by using @authenticate, we don't need to re-write
    # the login checking code all the time for other
    # front-end portals
    tickets = bn.get_all_tickets()
    return render_template('index.html', user=user, tickets=tickets)
