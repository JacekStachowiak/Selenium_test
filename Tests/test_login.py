from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
from my_account_page import MyAccountPages

@pytest.mark.usefixtures('setup')
class TestLogIn:
    
    def test_log_in_passed(self):
        my_account_pages = MyAccountPages(self.driver)
        my_account_pages.open_page()
        my_account_pages.log_in('testeroprogramowania@gmail.com', 'testeroprogramowania')
      
        assert my_account_pages.is_logout_link_displayed()   

    def test_log_in_failed(self):
        my_account_pages = MyAccountPages(self.driver)
        my_account_pages.open_page()
        my_account_pages.log_in('testeroprogramowania@gmail.com1', 'testeroprogramowania123')  
        
        # czy zawiera się w ...
        assert 'ERROR: Incorrect username or password.' in my_account_pages.get_error_msg()  