from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from configuration.logger_config import get_logger


class Dropdown_page:
    dropdown = "dropdown"

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_logger(self.__class__.__name__)

    def select_from_dropdown(self):
        select = Select(self.driver.find_element(By.ID, self.dropdown))
        select.select_by_visible_text("Option 1")
        text = select.first_selected_option.text
        self.logger.info(f"Text selected from the dropdown: {text}")
        return text
