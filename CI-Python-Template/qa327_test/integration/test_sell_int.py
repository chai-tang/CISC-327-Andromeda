import pytest
from seleniumbase import BaseCase
from qa327.models import db, User, Ticket

from qa327_test.conftest import base_url


# integration testing: the test case interacts with the 
# browser, and test the whole system (frontend+backend).

@pytest.mark.usefixtures('server')
class Sold(BaseCase):

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

    def rem_ticket(self):
        """Remove a test ticket from the database"""
        testTicket=Ticket.query.filter_by(name='test sell int ticket').first()
        db.session.delete(testTicket)
        db.session.commit()
    
    def test_sell(self):
        """Test Buy"""
        
        self.register()
        self.login()
        self.open(base_url)

        # enter valid inputs
        self.type('#sell_name','test sell int ticket')
        self.type('#sell_quantity',50)
        self.type('#sell_price',20)
        self.type('#sell_expiration_date',20221225)
        # submit the form
        self.click('#sell-submit')
        # validate that the tickets listed message is displayed
        message = self.get_text('#message')
        self.assert_equal("Tickets added to listing",message)        
        
        #cleanup database
        self.logout()
        self.rem_ticket()
        new_user = User.query.filter_by(email="testregisterint@email").first()
        db.session.delete(new_user)
        db.session.commit()
