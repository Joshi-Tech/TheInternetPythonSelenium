from base_pages.checkboxes_page import Checkboxes_page
from module.open_a_page import open_a_specific_page


class Test_Checkboxes_Page:

    def test_get_alert_heading(self):
        driver, page = open_a_specific_page("Checkboxes")
        checkboxes_page = Checkboxes_page(driver)
        print(checkboxes_page.get_heading() + "**")

        if checkboxes_page.get_heading() == "Checkboxes":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_click_a_checkbox(self):
        driver, page = open_a_specific_page("Checkboxes")
        checkboxes_page = Checkboxes_page(driver)
        checkboxes_page.click_checkbox()[0].click()
        if checkboxes_page.click_checkbox()[0].is_selected() is True:
            assert True
            driver.close()
        else:
            driver.close()
            assert False
