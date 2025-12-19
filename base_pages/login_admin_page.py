from selenium.webdriver.common.by import By


class Login_Admin_Page:
    username = "username"
    password = "password"
    login_btn = "[type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, email):
        self.driver.find_element(By.ID, self.username).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_btn).click()
