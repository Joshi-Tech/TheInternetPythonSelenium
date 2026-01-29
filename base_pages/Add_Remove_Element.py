from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Add_Remove_Element_Page(Base_Class):
    heading = "h3"
    add_element_btn = "[class='example']>button"
    delete_btn = "[class='added-manually']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_add_element_btn(self):
        self.logger.info(f"Add Element button clicked")
        self.driver.find_element(By.CSS_SELECTOR, self.add_element_btn).click()

    def is_delete_btn_displayed(self):
        add_remove_element = self.driver.find_element(By.CSS_SELECTOR, self.add_element_btn)
        self.logger.info(f"Add/Remove button displayed: {add_remove_element}")
        return add_remove_element.is_displayed()
