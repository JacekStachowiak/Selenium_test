from selenium.webdriver.common.keys import Keys
from locators import MyAccountPage

class MyAccountPages:
    
    def __init__(self, driver):
        self.driver = driver
        self.username_input = MyAccountPage.username_input
        self.password_input = MyAccountPage.password_input
        self.reg_email_input = MyAccountPage.reg_email_input
        self.reg_password_input = MyAccountPage.reg_password_input
        self.logout_link = MyAccountPage.logout_link
        self.err_msg = MyAccountPage.err_msg
    
    def open_page(self):
        self.driver.get('http://seleniumdemo.com/?page_id=7/')
          
    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.password_input).send_keys(Keys.ENTER)
    
    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input).send_keys(email)
        self.driver.find_element(*self.reg_password_input).send_keys(password)
        self.driver.find_element(*self.reg_password_input).send_keys(Keys.ENTER)
    
    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()
    
    def get_error_msg(self):
        return self.driver.find_element(*self.err_msg).text
            
        
            

    
 