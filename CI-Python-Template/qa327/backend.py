from qa327.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

"""
This file defines all backend logic that interacts with database and other services
"""


def get_user(email):
    """
    Get a user by a given email
    :param email: the email of the user
    :return: a user that has the matched email address
    """
    user = User.query.filter_by(email=email).first()
    return user


def login_user(email, password):
    """
    Check user authentication by comparing the password
    :param email: the email of the user
    :param password: the password input
    :return: the user if login succeeds
    """
    # if this returns a user, then the name already exists in database
    user = get_user(email)
    if not user or not check_password_hash(user.password, password):
        return None
    return user


def register_user(email, name, password, password2):
    """
    Register the user to the database
    :param email: the email of the user
    :param name: the name of the user
    :param password: the password of user
    :param password2: another password input to make sure the input is correct
    :return: an error message if there is any, or None if register succeeds
    """

    hashed_pw = generate_password_hash(password, method='sha256')
    # store the encrypted password rather than the plain password
    new_user = User(email=email, name=name, password=hashed_pw, balance=0)

    db.session.add(new_user)
    db.session.commit()
    return None

def set_balance(email,newBalance):
    """
    Changes the balance of the user associated with email
    :param email: the email of the user
    :param newBalance: the value that the user's balance will be set to
    :return: an error message if there is any, or None if balance changes succeed
    """
    user = get_user(email)
    user.balance = newBalance
    db.session.commit()
    return None

def get_all_tickets():
    tickets=Ticket.query.filter(Ticket.expiration_date >=datetime.date.today())
    return tickets

def sell_tickets(name,quantity,price,expiration_date):
    """
    skeleton for /sell post
    """
    return None

def buy_tickets(name,quantity):
    """
    skeleton for /buy post
    """
    return None

def update_tickets(name,quantity,price,expiration_date):
    """
    skeleton for /update post
    """
    return None
