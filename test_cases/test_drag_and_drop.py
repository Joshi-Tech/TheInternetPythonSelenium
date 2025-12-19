from selenium.webdriver.common.by import By

from base_pages.drag_and_drop_page import Drag_And_Drop_page
from module.open_a_page import open_a_specific_page


class Test_Drag_and_Drop:

    def test_get_heading(self):
        driver, page = open_a_specific_page("Drag and Drop")
        page_title = driver.find_element(By.CSS_SELECTOR, "h3").text
        if page_title == "Drag and Drop":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_perform_drag_and_drop(self):
        driver, page = open_a_specific_page("Drag and Drop")
        drag_and_drop = Drag_And_Drop_page(driver)
        drag_and_drop.drop_column()
        # Validation
        column_a_header = driver.find_element(
            By.CSS_SELECTOR, "#column-a header"
        ).text

        assert column_a_header == "B"
        driver.close()
