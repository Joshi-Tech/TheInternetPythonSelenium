from base_pages.digest_authentication_page import Digest_authentication_page
from test_cases.base_test_class import Test_Base_test_Class


class Test_Digest_Auth_Page:

    def test_validate_digest_auth_page_text(self):
        self.driver = Test_Base_test_Class().launch_page("digest_auth")
        digest_auth = Digest_authentication_page(self.driver)
        page_text = digest_auth.get_page_auth_text()
        if page_text == "Congratulations! You must have the proper credentials.":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
