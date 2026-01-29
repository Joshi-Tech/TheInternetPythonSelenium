from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Geo_Location_Page(Base_Class):
    id = "demo"
    where_am_i_btn = "button[onclick='getLocation()']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_long_and_lat_text(self):
        long_lang_element = self.driver.find_element(By.ID, self.id)
        self.logger.info(f"Longitude and latitude text can be seen: {long_lang_element.text}")
        return long_lang_element.text

    def click_where_am_i_btn(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.where_am_i_btn)
        self.logger.info(f"Where am i? button clicked: {element}")
        element.click()
