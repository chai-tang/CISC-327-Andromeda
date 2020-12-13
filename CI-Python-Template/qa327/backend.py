from qa327.models import db, User, Ticket
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

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
    # Store the encrypted password rather than the plain password
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
    if newBalance < 0:
        return "Cannot set balance to less than zero"
    user.balance = newBalance
    db.session.commit()
    return None

def get_all_tickets():
    """
    Fetch all unexpired tickets
    :return: a list of all unexpired tickets
    """
    tickets=Ticket.query.filter(Ticket.expiration_date >=datetime.date.today().strftime("%Y%m%d"))
    return tickets

def sell_tickets(name,email,quantity,price,expiration_date):
    """
    Add ticket to listing
    :param name: the name of the ticket
    :param quantity: the number of tickets to sell
    :param price: the price of each ticket in dollars
    :param expiration_date: the day the tickets expire
    :return: an error message if there is any, or None if ticket listing succeeds
    """
    new_ticket=Ticket(name=name,email=email,quantity=quantity,price=price,expiration_date=expiration_date)
    db.session.add(new_ticket)
    db.session.commit()
    return None

def buy_tickets(name,quantity):
    """
    Reduce number of an available ticket by an integer
    :param name: the name of the ticket to purchase
    :param quantity: the number of tickets to purchase
    :return: an error message if there is any, or None if purchase succeeds
    """
    buyticket=Ticket.query.filter_by(name=name).first()
    buyticket.quantity=buyticket.quantity-int(quantity)
    db.session.commit()
    return None

def update_tickets(name,quantity,price,expiration_date):
    """
    Change a listing of a ticket
    :param name:
    :param quantity:
    :param price:
    :param expiration_date:
    :return: an error message if there is any, or None if update succeeds
    """
    ticket=Ticket.query.filter_by(name=name).first()
    ticket.quantity=quantity
    ticket.price=price
    ticket.expiration_date=expiration_date
    db.session.commit()
    return None
