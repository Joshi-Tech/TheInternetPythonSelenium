from base_pages.Add_Remove_Element import Add_Remove_Element_Page
from module.open_a_page import open_a_specific_page


class Test_Add_Remove_Element:

    def test_get_page_title(self):
        driver, page = open_a_specific_page("Add/Remove Elements")
        page_heading = Add_Remove_Element_Page(driver).get_heading()
        if page_heading == "Add/Remove Elements":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_is_delete_button(self):
        driver, page = open_a_specific_page("Add/Remove Elements")
        add_remove_element = Add_Remove_Element_Page(driver)
        add_remove_element.click_add_element_btn()
        add_remove_element.is_delete_btn_displayed()
        if add_remove_element.is_delete_btn_displayed() is True:
            assert True
            driver.close()
        else:
            driver.close()
            assert False
