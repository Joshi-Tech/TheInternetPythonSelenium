from selenium.webdriver.common.by import By

from configuration.logger_config import get_logger


class Digest_authentication_page:
    username = "admin"
    password = "admin"
    page_text_element = "[class='example']>p"

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def get_page_auth_text(self):
        auth_text: str = self.driver.find_element(By.CSS_SELECTOR, self.page_text_element).text
        self.logger.info(f"Auth text can be seen: {auth_text}")
        return auth_text
