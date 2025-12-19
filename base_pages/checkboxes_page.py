from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Checkboxes_page (Base_Class):

    heading="h3"
    checkbox="[type='checkbox']"

    # def __init__(self, driver):
    #     self.driver = driver

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkbox(self):
       return self.driver.find_elements(By.CSS_SELECTOR, self.checkbox)

    # def get_heading(self):
    #     return self.driver.find_element(By.CSS_SELECTOR, self.heading).text