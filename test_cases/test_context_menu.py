from base_pages.Context_Menu_Page import Context_Menu_Page
from module.open_a_page import open_a_specific_page


class Test_Context_Menu:

    def test_context_menu(self):
        driver, page = open_a_specific_page("Context Menu")
        context_menu = Context_Menu_Page(driver)
        alert_text = context_menu.right_click_On_Context_Menu()
        alert_heading_text = "You selected a context menu"
        if alert_text == alert_heading_text:
            assert True
            driver.quit()
        else:
            driver.quit()
            assert False

    def test_context_menu_heading(self):
        driver, page = open_a_specific_page("Context Menu")
        context_menu = Context_Menu_Page(driver)
        heading_text = context_menu.get_heading()
        if heading_text == heading_text == "Context Menu":
            assert True
            driver.close()
        else:
            driver.close()
            assert False
