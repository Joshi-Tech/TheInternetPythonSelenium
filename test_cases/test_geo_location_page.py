import time

from module.open_a_page import open_a_specific_page


class Test_Geo_Location_Page:

    def test_get_main_text(self):
        driver, page = open_a_specific_page("Geolocation")
        geo_location_text = page.get_long_and_lat_text()
        if geo_location_text == "Click the button to get your current latitude and longitude":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_get_main_text1(self):
        driver, page = open_a_specific_page("Geolocation")
        # Click the button
        page.click_where_am_i_btn()
        time.sleep(3)  # Wait for coordinates to load
        text = page.get_long_and_lat_text()
        assert "Latitude" in text and "Longitude" in text
        driver.close()
