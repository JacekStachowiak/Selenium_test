import pytest
import random
from address_page import AddressPage
from my_account_page import MyAccountPages

@pytest.mark.usefixtures('setup')
class TestUpdateAddress:
  
    def test_update_address(self):
        email = str(random.randint(1,10000)) + 'testeroprogramowania@gmial.com'
        my_account_pages = MyAccountPages(self.driver)
        my_account_pages.open_page()
        my_account_pages.log_in('testeroprogramowania@gmail.com', 'testeroprogramowania')
        address_page = AddressPage(self.driver)
        address_page.edit_address()
        address_page.set_personal_data('Jack123', 'Stach123')
        address_page.select_country('Poland')
        address_page.set_address('Dworcowa 5', '66-540', 'Kraków')
        address_page.set_phone_number('444 666 777')
        address_page.save_address()
        
        assert 'Address changed successfully.' in address_page.get_message_text()
