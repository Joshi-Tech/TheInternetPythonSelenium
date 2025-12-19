from module.open_a_page import open_a_specific_page


class Test_Hover_Over_Page:

    def test_get_heading(self):
        driver, page = open_a_specific_page("Hovers")
        if page.get_heading() == "Hovers":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_get_text(self):
        driver, page = open_a_specific_page("Hovers")
        if page.get_page_text() == "Hover over the image for additional information":
            assert True
            driver.close()
        else:
            driver.close()
            assert False

    def test_move_object(self):
        driver, page = open_a_specific_page("Hovers")

        expected_users = ["name: user1", "name: user2", "name: user3"]

        for index, expected in enumerate(expected_users):
            print(index, " : ", expected)
            text = page.move_object(index)
            assert text == expected

        driver.close()
