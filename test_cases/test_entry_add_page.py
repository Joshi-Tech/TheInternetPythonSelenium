from base_pages.entry_ad_page import Entry_Ad_Page
from module.open_a_page import open_a_specific_page


class Test_Entry_Ad_Page:

    def get_entry_ad_page(self):
        driver, page = open_a_specific_page("Entry Ad")
        return Entry_Ad_Page(driver)

    def test_get_header_of_entry_ad_modal(self):
        driver, page = open_a_specific_page("Entry Ad")
        modal_heading = page.get_modal_head_text()
        if modal_heading == "THIS IS A MODAL WINDOW":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_get_main_text_from_modal(self):
        driver, page = open_a_specific_page("Entry Ad")
        main_text = page.get_modal_main_text()
        if main_text == "It's commonly used to encourage a user to take an action (e.g., give their e-mail address to sign up for something or disable their ad blocker).":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_get_heading_of_entry_ad_page(self):
        driver, page = open_a_specific_page("Entry Ad")
        page.click_modal_footer()
        heading = page.get_heading()
        if heading == "Entry Ad":
            assert True
            driver.close()
        else:
            driver.close()
            assert False
