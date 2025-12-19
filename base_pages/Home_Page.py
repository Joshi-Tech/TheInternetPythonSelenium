from selenium.webdriver.common.by import By

from base_pages.base_class import Base_Class


class Home_Page(Base_Class):
    heading = ".heading"
    page_url = "https://the-internet.herokuapp.com"

    # def __init__(self,driver):
    #     self.driver = driver

    # def launch_url(self):
    #     self.driver.get(self.page_url)

    def click_a_link(self, link):
        self.driver.find_element(By.XPATH, "//a[text()='" + link + "']").click()
