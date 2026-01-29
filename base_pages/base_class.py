from selenium.webdriver.common.by import By

from configuration.logger_config import get_logger


class Base_Class:
    page_url = "https://the-internet.herokuapp.com"
    page_title = "h1"
    home_page_heading = "h2"
    heading = "h3"

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def open_main_page(self, url):
        self.logger.info(f"Opening URL: {url}")
        self.driver.get(url)

    def get_heading(self):
        heading_text = self.driver.find_element(By.CSS_SELECTOR, self.heading).text
        self.logger.info(f"Heading text captured: {heading_text}")
        return heading_text
