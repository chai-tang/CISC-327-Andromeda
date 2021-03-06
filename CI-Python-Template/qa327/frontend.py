from flask import render_template, request, session, redirect, url_for
from qa327 import app
import qa327.backend as bn
import re
import datetime
import sys

"""
This file defines the front-end part of the service.
It elaborates how the services should handle different
http requests from the client (browser) through templating.
The html templates are stored in the 'templates' folder.
"""


@app.route('/register', methods=['GET'])
def register_get():

    # if the user is logged in already, redirect to home page
    if 'logged_in' in session:
        return redirect('/', code=303)

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
    emailPattern = re.compile("([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?(\.[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?)*|\[((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|IPv6:((((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){6}|::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){5}|[0-9A-Fa-f]{0,4}::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){4}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):)?(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){3}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,2}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){2}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,3}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,4}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,5}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,6}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)|(?!IPv6:)[0-9A-Za-z-]*[0-9A-Za-z]:[!-Z^-~]+)])")
    lengthPattern = re.compile("^.{1,63}$")
    usernamePattern = re.compile("^[\w][\w| ]{0,18}[\w]$")

    # check that both passwords match
    if password != password2:
        login_message="password format is incorrect"

    # check that the forms all match the required patterns using regular expressions
    elif not(emailPattern.match(email)) or not(lengthPattern.match(email)):
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

    # if the user is logged in already, redirect to home page
    if 'logged_in' in session:
        return redirect('/', code=303)

    # if a message was passed to this function, display that as message. else, display 'Please login'
    passed_message = request.args.get('message')
    if passed_message == None:
        passed_message = 'Please login'
    return render_template('login.html', message=passed_message)


@app.route('/login', methods=['POST'])
def login_post():

    # get the user's form inputs
    email = request.form.get('email')
    password = request.form.get('password')
    # attempt to login with those user credentials
    user = bn.login_user(email, password)

    # if bn.login_user succeeds, add that user's email to the session (as 'logged_in')
    # then redirect them to the homepage
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

    # if login failed, check what the error was and display an appropriate error message
    else:
        # use these regex's to validate that the user's form inputs match the required format
        passwordPattern = re.compile("(?=.*[a-z])(?=.*[A-Z])(?=.*([!-/]|[:-@])).{6,}")
        emailPattern = re.compile("([!#-'*+/-9=?A-Z^-~-]+(\.[!#-'*+/-9=?A-Z^-~-]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?(\.[0-9A-Za-z]([0-9A-Za-z-]{0,61}[0-9A-Za-z])?)*|\[((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|IPv6:((((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){6}|::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){5}|[0-9A-Fa-f]{0,4}::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){4}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):)?(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){3}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,2}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){2}|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,3}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,4}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,5}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3})|(((0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}):){0,6}(0|[1-9A-Fa-f][0-9A-Fa-f]{0,3}))?::)|(?!IPv6:)[0-9A-Za-z-]*[0-9A-Za-z]:[!-Z^-~]+)])")
        lengthPattern = re.compile("^.{1,63}$")
        # if there was a formatting issue, display which form wasn't accepted
        if (not(passwordPattern.match(password))):
            return render_template('login.html', message='password format incorrect')
        elif not(emailPattern.match(email)) or not(lengthPattern.match(email)):
            return render_template('login.html', message='email format incorrect')

        # for any others issues, assume that the given email and password did not match that of an existing account
        else:
            return render_template('login.html', message='email/password combination incorrect')


@app.route('/logout', methods=['GET'])
def logout():
    # check if there is a user currently logged_in in this session
    # if there is, set 'logged_in' to None to log them out
    if 'logged_in' in session:
        session.pop('logged_in', None)

    # always redirect to homepage
    # since the user is logged out at this point, this should immediately redirect to /login
    return redirect('/', code=303)


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
            return redirect('/login', code=303)

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
    welcome_header='Hi {}!'.format(user.name)
    alltickets = bn.get_all_tickets()
    currdate=int(datetime.datetime.now().strftime("%Y%m%d"))
    tickets=[]
    for ticket in alltickets:
        if ticket.expiration_date>currdate:
            tickets.append(ticket)
    return render_template('index.html', welcome_header=welcome_header, user=user, balance=user.balance, tickets=tickets)


@app.errorhandler(404)
def other_requests(error):
    # returns a 404 error for any other requests
    return render_template('404.html', message='404 ERROR: The requested URL was not found on the server.'), 404

@app.route('/sell',methods=['POST'])
def sell_post():
    # Always check if the user is logged in
    if 'logged_in' not in session:
        return redirect('/login', code=303)

    # get the ticket information from the user's form inputs
    sell_name=request.form.get('sell_name')
    sell_quantity=request.form.get('sell_quantity')
    sell_price=request.form.get('sell_price')
    sell_expiration_date=request.form.get('sell_expiration_date')
    # get the currently logged in user
    email=session['logged_in']
    user=bn.get_user(email)

    # some regex's to validate the inputs
    namepattern=re.compile("^[a-zA-Z0-9][a-zA-z0-9 ]{0,58}[a-zA-Z0-9]$")
    quantitypattern=re.compile("^(100|[1-9][0-9]?)$")
    pricepattern=re.compile("(100)|(^[1-9][0-9]$)")
    datepattern=re.compile("([2-9][0-9][0-9][0-9])(([0][1-9])|([1][0-2]))(([0][1-9])|([1-2][0-9])|([3][0-1]))")

    # use the regex's to validate that the ticket info is in acceptable format
    # display appropriate error messages for any formatting errors
    if not(namepattern.match(sell_name)):
        return render_template('index.html',message='Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space. ', balance=user.balance, tickets=bn.get_all_tickets())
    elif not(quantitypattern.match(sell_quantity)):
        return render_template('index.html',message='Ticket quantity must be between 1 and 100. ', balance=user.balance, tickets=bn.get_all_tickets())
    elif not(pricepattern.match(sell_price)):
        return render_template('index.html',message='Ticket price must be between 10 and 100. ', balance=user.balance, tickets=bn.get_all_tickets())
    elif not(datepattern.match(sell_expiration_date)):
        return render_template('index.html',message='Expiration date must be in form YYYYMMDD. ', balance=user.balance, tickets=bn.get_all_tickets())
    
    # if the inputs are formatted correctly, attempt to sell the ticket
    else:
        sell_error_message=bn.sell_tickets(sell_name,session['logged_in'],sell_quantity,sell_price,sell_expiration_date)
    # if bn.sell_tickets fails, display the error message it returns
    if sell_error_message!=None:
        return render_template('index.html',message=sell_error_message, balance=user.balance, tickets=bn.get_all_tickets())
    # else, display that the ticket has successfully been posted
    return render_template('index.html',message='Tickets added to listing', balance=user.balance, tickets=bn.get_all_tickets())

@app.route('/buy',methods=['POST'])
def buy_post():
    # Always check if the user is logged in
    if 'logged_in' not in session:
        return redirect('/login', code=303)

    # get the ticket information from the user's form inputs
    buy_name=request.form.get('buy_name')
    buy_quantity=request.form.get('buy_quantity')
    # attempt to retrieve the tickets with that name from backend
    buyticket = None
    all_tickets = bn.get_all_tickets()
    for ticket in all_tickets:
        if ticket.name == buy_name:
            buyticket = ticket
    #buyticket=bn.get_all_tickets().filter_by(name=buy_name).first()

    # regex's to validate the user's form input
    namepattern=re.compile("^[a-zA-Z0-9][a-zA-z0-9 ]{0,58}[a-zA-Z0-9]$")
    quantitypattern=re.compile("^(100|[1-9][0-9]?)$")

    # get the currently logged in user
    email=session['logged_in']
    user=bn.get_user(email)

    # validate the inputs
    if not(namepattern.match(buy_name)):
         return render_template('index.html',message='Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.', balance=user.balance, tickets=bn.get_all_tickets()) 
    elif not(quantitypattern.match(buy_quantity)):
        return render_template('index.html',message='Ticket quantity must be between 1 and 100',balance=user.balance, tickets=bn.get_all_tickets())

    # if the tickets could not be retrieved, display an appropriate error message
    if buyticket==None:
        return render_template('index.html',message='No such ticket {}'.format(buy_name), balance=user.balance, tickets=bn.get_all_tickets())
    elif buyticket.quantity<int(buy_quantity):
        return render_template('index.html',message='Not enough tickets. ', balance=user.balance, tickets=bn.get_all_tickets())
    elif buyticket.price * int(buy_quantity) > user.balance:
        return render_template('index.html',message='Not enough balance to purchase tickets. ', balance=user.balance, tickets=bn.get_all_tickets())
    
    # if the tickets were successfully retrieved, attempt to buy the tickets
    else:
        buy_error_message=bn.buy_tickets(buy_name,buy_quantity)
    # if bn.buy_tickets fails, display the error message it returns
    if buy_error_message!=None:
        return render_template('index.html',message=buy_error_message, balance=user.balance, tickets=bn.get_all_tickets())
    # else, update the user's balance based on the price of the tickets purchased
    user.balance-=buyticket.price*int(buy_quantity)
    bn.set_balance(email,user.balance)

    # display that the tickets have succesfully been purchased
    return render_template('index.html',message='Tickets purchased', balance=user.balance, tickets=bn.get_all_tickets())

@app.route('/update',methods=['POST'])
def update_post():
    # Always check if the user is logged in
    if 'logged_in' not in session:
        return redirect('/login', code=303)

    # get the ticket information from the user's form inputs
    update_name=request.form.get('update_name')
    update_quantity=request.form.get('update_quantity')
    update_price=request.form.get('update_price')
    update_expiration_date=request.form.get('update_expiration_date')

    # get the currently logged in user
    email=session['logged_in']
    user=bn.get_user(email)

    # some regex's to validate the user's form inputs
    namepattern=re.compile("^[a-zA-Z0-9][a-zA-z0-9 ]{0,58}[a-zA-Z0-9]$")
    quantitypattern=re.compile("^(100|[1-9][0-9]?)$")
    pricepattern=re.compile("(100)|(^[1-9][0-9]$)")
    datepattern=re.compile("([2-9][0-9][0-9][0-9])(([0][1-9])|([1][0-2]))(([0][1-9])|([1-2][0-9])|([3][0-1]))")

    # use the regex's to validate that their form inputs match the required format
    # if they don't, display the appropriate error message
    if not(namepattern.match(update_name)):
         return render_template('index.html',message='Ticket name must be alphanumeric, between 1 and 60 characters, and not start or end with a space.', balance=user.balance, tickets=bn.get_all_tickets()) 
    elif not(quantitypattern.match(update_quantity)):
         return render_template('index.html',message='Quantity must be between 1 and 100', balance=user.balance, tickets=bn.get_all_tickets())
    elif not(pricepattern.match(update_price)):
        return render_template('index.html',message='Price must be between 10 and 100', balance=user.balance, tickets=bn.get_all_tickets())
    elif not(datepattern.match(update_expiration_date)):
        return render_template('index.html',message='Expiration date must be in form YYYYMMDD', balance=user.balance, tickets=bn.get_all_tickets())

    # attempt to retrieve the user's desired tickets
    update_ticket = None
    all_tickets = bn.get_all_tickets()
    for ticket in all_tickets:
        if ticket.name == update_name:
            update_ticket = ticket
    #update_ticket=bn.get_all_tickets().filter_by(name=update_name).first()

    # if the tickets could not be retrieved, display an appropriate error message
    if update_ticket==None:
        return render_template('index.html',message='No such ticket {}. '.format(update_name), balance=user.balance, tickets=bn.get_all_tickets())
    
    # if the tickets were successfully retrieved, attempt to update said tickets

    # if the user left any non-required forms blank, assume that those values will stay the same
    if update_quantity=='':
        update_quantity=update_ticket.quantity
    if update_price=='':
        update_price=update_ticket.price
    if update_expiration_date=='':
        update_expiration_date=update_ticket.expiration_date

    # check that the user is the owner of the tickets they want to update, and return an error message if they aren't
    if update_ticket.email!=email:
        return render_template('index.html',message='Can only update your own tickets. ', balance=user.balance, tickets=bn.get_all_tickets())
    
    # if no errors have occurred thus far, attempt to update the tickets
    else:
        update_error_message=bn.update_tickets(update_name,update_quantity,update_price,update_expiration_date)
    # if bn.update_tickets fails, display the error message it returns
    if update_error_message!=None:
        return render_template('index.html',message=update_error_message, balance=user.balance, tickets=bn.get_all_tickets())
    # else, display that the tickets have been succesfully updated
    return render_template('index.html',message='Listing updated', balance=user.balance, tickets=bn.get_all_tickets())
