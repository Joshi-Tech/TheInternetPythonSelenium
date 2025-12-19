from selenium.webdriver.common.by import By

from test_cases.base_test_class import Test_Base_test_Class


class Test_Home_Page:

    def test_home_page_heading(self):
        self.driver = Test_Base_test_Class().launch_page("home_page")
        home_page_heading = self.driver.find_element(By.CSS_SELECTOR, "h1").text
        page_heading = "Welcome to the-internet"
        if home_page_heading == page_heading:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
