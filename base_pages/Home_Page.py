from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Home_Page(Base_Class):
    heading = ".heading"
    page_url = "https://the-internet.herokuapp.com"

    def click_a_link(self, link):
        click_link = self.driver.find_element(By.XPATH, "//a[text()='" + link + "']")
        self.logger.info(f"Clicked on link: {click_link.text}")
        click_link.click()
