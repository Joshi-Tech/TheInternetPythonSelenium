from selenium.webdriver.common.by import By

from configuration.logger_config import get_logger


class Login_Admin_Page:
    username = "username"
    password = "password"
    login_btn = "[type='submit']"

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def enter_username(self, email):
        user_name = self.driver.find_element(By.ID, self.username).send_keys(email)
        self.logger.info(f"User name added: {user_name}")

    def enter_password(self, password):
        self.logger.info(f"User password added")
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def click_login_button(self):
        self.logger.info(f"User click button")
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn).click()
