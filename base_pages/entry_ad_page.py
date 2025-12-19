from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_pages.base_class import Base_Class


class Entry_Ad_Page(Base_Class):
    modal_title = ".modal-title > h3"
    modal_text = ".modal-body > p"
    modal_footer = ".modal-footer>p"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_modal_head_text(self):
        # wait for modal to appear
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.modal_title))
        )
        return self.driver.find_element(By.CSS_SELECTOR, self.modal_title).text

    def get_modal_main_text(self):
        WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, self.modal_text))
        )
        return self.driver.find_element(By.CSS_SELECTOR, self.modal_text).text

    def click_modal_footer(self):
        wait = WebDriverWait(self.driver, 10)

        # Wait for the modal footer element to be clickable
        footer = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.modal_footer)))

        # Sometimes headless needs scroll into view before click
        self.driver.execute_script("arguments[0].scrollIntoView(true);", footer)

        footer.click()
