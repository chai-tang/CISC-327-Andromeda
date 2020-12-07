import pytest
from seleniumbase import BaseCase
from qa327.models import db, User, Ticket

from qa327_test.conftest import base_url


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class Bought(BaseCase):

    def register(self):
        """Register a new user"""
        self.open(base_url + '/register')
        self.type("#email", "testregisterint@email")
        self.type("#name", "tester")
        self.type("#password", "qqQQ!!")
        self.type("#password2", "qqQQ!!")
        self.click('input[type="submit"]')

    def login(self):
        """Login with test user credentials"""
        self.open(base_url + '/login')
        self.type("#email", "testregisterint@email")
        self.type("#password", "qqQQ!!")
        self.click('input[type="submit"]')

    def logout(self):
        """Logout the user"""
        self.open(base_url+'/logout')

    def add_ticket(self):
        """Add a test ticket to the database"""
        testTicket = Ticket(name='test buy int ticket',email='testbuyint@email',quantity=99,price=50,expiration_date=20221225)
        db.session.add(testTicket)
        db.session.commit()
        
    def rem_ticket(self):
        """Remove a test ticket from the database"""
        testTicket=Ticket.query.filter_by(name='test buy int ticket').first()
        db.session.delete(testTicket)
        db.session.commit()
    
    def test_buy(self):
        """Test Buy"""
        
        self.register()
        self.login()
        self.open(base_url)
 
        # enter valid inputs to sell a ticket
        self.type('#sell_name','test buy int ticket')
        self.type('#sell_quantity',50)
        self.type('#sell_price',20)
        self.type('#sell_expiration_date',20221225)
        # submit the form
        self.click('#sell-submit')
           
        self.open(base_url)
 
        # enter valid inputs to buy the ticket
        self.type('#buy_name','test buy int ticket')
        self.type('#buy_quantity',1)
        # submit the form
        self.click('#buy-submit')
        # validate that the tickets purchased message is displayed
        message = self.get_text('#message')
        self.assert_equal("Tickets purchased",message)
        
        #cleanup database
        self.logout()
        self.rem_ticket()
        new_user = User.query.filter_by(email="testregisterint@email").first()
        db.session.delete(new_user)
        db.session.commit()
