import os
import platform

from selenium import webdriver
from selenium.webdriver.common.by import By


# @pytest.fixture
# def driver():
#     driver = DriverFactory.get_driver("chrome")
#     yield driver
#     driver.quit()

class Test_Base_test_Class:
    page_url = "https://the-internet.herokuapp.com"
    login_page_url = "https://the-internet.herokuapp.com/login"
    digest_auth_url = "https://admin:admin@the-internet.herokuapp.com/digest_auth"
    geo_location_url = "https://the-internet.herokuapp.com/geo_location"
    page_title = "h1"
    page_title_h3 = "h3"

    def launch_page(self, page):
        # GitHub Actions automatically sets CI=true
        is_ci = os.getenv("CI", "false").lower() == "true"
        headless = os.getenv("HEADLESS", "false").lower() == "true" or is_ci

        options = webdriver.ChromeOptions()

        # Always good defaults
        options.add_argument("--window-size=1920,1080")

        # Linux/GitHub Actions stability flags
        if platform.system() == "Linux" or is_ci:
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--remote-debugging-port=9222")
            options.add_argument("--user-data-dir=/tmp/chrome-user-data")

        if headless:
            options.add_argument("--headless=new")

        self.driver = webdriver.Chrome(options=options)

        if page == "login_page":
            self.driver.get(self.login_page_url)
        elif page == "digest_auth":
            self.driver.get(self.digest_auth_url)
        else:
            self.driver.get(self.page_url)

        return self.driver

    def get_page_heading(self):
        return self.driver.find_element(By.CSS_SELECTOR, self.page_title_h3).text

    # def launch_page(self, page,driver):
    #     #self.driver = webdriver.Chrome()
    #     if page == "login_page":
    #         driver().get(self.login_page_url)
    #     elif page == "digest_auth":
    #         self.driver.get(self.digest_auth_url)
    #     elif page == "geo_location":
    #         options = Options()
    #         options.add_experimental_option("prefs", {
    #             "profile.default_content_setting_values.geolocation": 1  # 1 = Allow
    #         })
    #         self.driver = webdriver.Chrome(options)
    #         self.driver.get(self.page_url)
    #     else:
    #         self.driver.get(self.page_url)
    #     return self.driver
