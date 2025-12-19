from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Dropdown_page:
    dropdown = "dropdown"

    def __init__(self, driver):
        self.driver = driver

    def select_from_dropdown(self):
        select = Select(self.driver.find_element(By.ID, self.dropdown))
        select.select_by_visible_text("Option 1")
        return select.first_selected_option.text

