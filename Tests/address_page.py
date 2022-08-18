from selenium.webdriver.support.select import Select
from locators import AddressLocators
class AddressPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = AddressLocators.first_name_input
        self.last_name_input = AddressLocators.last_name_input
        self.addresses_link = AddressLocators.addresses_link
        self.edit_link = AddressLocators.edit_link
        self.company_ID = AddressLocators.company_ID
        self.country_select = AddressLocators.country_select
        self.street_input = AddressLocators.street_input
        self.postcode_input = AddressLocators.postcode_input
        self.city_input = AddressLocators.city_input
        self.phone_input = AddressLocators.phone_input
        self.save_button = AddressLocators.save_button
        self.message = AddressLocators.message
    
    def edit_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()
       
    def set_personal_data(self, first_name, last_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        
    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country_select))
        select.select_by_visible_text(country)
    
    def set_address(self, street, postcode, city):
        self.driver.find_element(*self.street_input).send_keys(street)
        self.driver.find_element(*self.postcode_input).clear()
        self.driver.find_element(*self.postcode_input).send_keys(postcode)
        self.driver.find_element(*self.city_input).send_keys(city)
            
    def set_phone_number(self, number):
        self.driver.find_element(*self.phone_input).send_keys(number)
    
    def save_address(self):
        self.driver.find_element(*self.save_button).click()
    
    def get_message_text(self):
        return self.driver.find_element(*self.message).text
                        
            
        