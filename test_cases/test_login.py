import time

from selenium.webdriver.common.by import By

from base_pages.login_admin_page import Login_Admin_Page
from test_cases.base_test_class import Test_Base_test_Class


class Test_Login:
    page_title = "The Internet"
    email_address = 'tomsmith'
    password = "SuperSecretPassword!"

    def test_user_on_login_page(self):
        self.driver = Test_Base_test_Class().launch_page("login_page")
        if self.driver.title == self.page_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_user_login_successfully(self):
        self.driver = Test_Base_test_Class().launch_page("login_page")
        login_admin = Login_Admin_Page(self.driver)
        login_admin.enter_username(self.email_address)
        login_admin.enter_password(self.password)
        login_admin.click_login_button()
        time.sleep(3)
        title_text = self.driver.find_element(By.CSS_SELECTOR, "[class='example']>h4").text.strip()
        flash_text = "Welcome to the Secure Area. When you are done click logout below."
        if title_text == flash_text:
            assert True
            self.driver.quit()
        else:
            self.driver.quit()
            assert False
