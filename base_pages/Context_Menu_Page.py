from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Context_Menu_Page (Base_Class):

    square_box="hot-spot"

    def __init__(self, driver):
        super().__init__(driver)

    def right_click_On_Context_Menu(self):
       element= self.driver.find_element(By.ID,self.square_box)
       actions = ActionChains(self.driver)
       actions.context_click(element).perform()
       alert = self.driver.switch_to.alert
       return alert.text