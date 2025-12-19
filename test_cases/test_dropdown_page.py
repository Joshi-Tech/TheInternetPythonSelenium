from base_pages.drop_down_page import Dropdown_page
from module.open_a_page import open_a_specific_page


class Test_Dropwdown_page:
    selected_element = "[selected='selected']"

    def test_select_from_dropdown(self):
        driver, page = open_a_specific_page("Dropdown")
        dropdown_page = Dropdown_page(driver)
        option = dropdown_page.select_from_dropdown()
        assert option == "Option 1"
        driver.close()
