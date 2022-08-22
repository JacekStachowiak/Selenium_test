import random
import pytest
from my_account_page import MyAccountPages

@pytest.mark.usefixtures('setup')
class TestCreateAccount:
    
    def test_create_account_failed(self):
        my_account_pages = MyAccountPages(self.driver)
        my_account_pages.open_page()
        my_account_pages.create_account('testeroprogramowania@gmail.com', 'testeroprogramowania')
        
        msg = 'An account is already registered with your email address. Please log in.'
        assert msg in my_account_pages.get_error_msg()

    def test_create_account_passed(self):
        email = str(random.randint(0, 10000)) + 'testeroprogramowania@gmail.com'
        my_account_pages = MyAccountPages(self.driver)
        my_account_pages.open_page()
        my_account_pages.create_account(email, 'testeroprogramowania')
              
        assert my_account_pages.is_logout_link_displayed()  
