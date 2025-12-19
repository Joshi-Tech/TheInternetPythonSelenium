from selenium.webdriver.common.by import By
from base_pages.base_class import Base_Class

class Geo_Location_Page(Base_Class):
    id = "demo"
    where_am_i_btn = "button[onclick='getLocation()']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_long_and_lat_text(self):
        return self.driver.find_element(By.ID, self.id).text

    def click_where_am_i_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.where_am_i_btn).click()
