from selenium.webdriver.common.by import By


class Digest_authentication_page:
    username = "admin"
    password = "admin"
    page_text_element="[class='example']>p"

    def __init__(self,driver):
        self.driver = driver

    def get_page_auth_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.page_text_element).text