from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Add_Remove_Element_Page(Base_Class):
    heading = "h3"
    add_element_btn = "[class='example']>button"
    delete_btn = "[class='added-manually']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # def get_heading(self):
    #     heading_text = self.driver.find_element(By.XPATH, self.heading).text
    #     return heading_text

    def click_add_element_btn(self):
        self.driver.find_element(By.CSS_SELECTOR, self.add_element_btn).click()

    def is_delete_btn_displayed(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.delete_btn).is_displayed()
