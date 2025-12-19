from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from base_pages.base_class import Base_Class


class Hover_Page(Base_Class):
    page_text = ".example > p"
    users = ".figure"
    user_text = ".figcaption h5"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_page_text(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.page_text).text

    def move_object(self, user: int):
        target_user = self.driver.find_elements(By.CSS_SELECTOR, self.users)[user]

        ActionChains(self.driver).move_to_element(target_user).perform()

        caption = target_user.find_element(By.CSS_SELECTOR, self.user_text)
        WebDriverWait(self.driver, 5).until(EC.visibility_of(caption))

        return caption.text.strip()
