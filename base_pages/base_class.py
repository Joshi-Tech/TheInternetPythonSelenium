from selenium.webdriver.common.by import By
from selenium import webdriver


class Base_Class:

    page_url = "https://the-internet.herokuapp.com"
    page_title = "h1"
    home_page_heading = "h2"
    heading = "h3"

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get(self.page_url)

    def get_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.heading).text