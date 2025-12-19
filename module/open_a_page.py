from base_pages.Add_Remove_Element import Add_Remove_Element_Page
from base_pages.Context_Menu_Page import Context_Menu_Page
from base_pages.Home_Page import Home_Page
from base_pages.checkboxes_page import Checkboxes_page
from base_pages.digest_authentication_page import Digest_authentication_page
from base_pages.drag_and_drop_page import Drag_And_Drop_page
from base_pages.drop_down_page import Dropdown_page
from base_pages.entry_ad_page import Entry_Ad_Page
from base_pages.geo_location_page import Geo_Location_Page
from base_pages.hover_page import Hover_Page
from base_pages.login_admin_page import Login_Admin_Page
from test_cases.base_test_class import Test_Base_test_Class


def open_a_specific_page(page_name):
    driver = Test_Base_test_Class().launch_page(page_name)
    home_page = Home_Page(driver)
    match page_name:
        case "Add/Remove Elements":
            home_page.click_a_link("Add/Remove Elements")
            page = Add_Remove_Element_Page(driver)
        case "Checkboxes":
            home_page.click_a_link("Checkboxes")
            page = Checkboxes_page(driver)
        case "Context Menu":
            home_page.click_a_link("Context Menu")
            page = Context_Menu_Page(driver)
        case "digest_auth":
            home_page.click_a_link("digest_auth")
            page = Digest_authentication_page(driver)
        case "Drag and Drop":
            home_page.click_a_link("Drag and Drop")
            page = Drag_And_Drop_page(driver)
        case "Dropdown":
            home_page.click_a_link("Dropdown")
            page = Dropdown_page(driver)
        case "Entry Ad":
            home_page.click_a_link("Entry Ad")
            page = Entry_Ad_Page(driver)
        case "Geolocation":
            home_page.click_a_link("Geolocation")
            page = Geo_Location_Page(driver)
        case "Hovers":
            home_page.click_a_link("Hovers")
            page = Hover_Page(driver)
        case "login_page":
            home_page.click_a_link("login_page")
            page = Login_Admin_Page(driver)
        case _:
            raise ValueError(f"Unknown page name: {page_name}")
    return driver, page
