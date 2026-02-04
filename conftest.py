import os
from datetime import datetime

import pytest
import allure


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # only on test failure
    if rep.when == "call" and rep.failed:

        driver = None

        # if you ever use a driver fixture in future
        driver = item.funcargs.get("driver", None)

        # your current style: self.driver stored on test class instance
        if driver is None and hasattr(item, "instance") and hasattr(item.instance, "driver"):
            driver = item.instance.driver

        if driver is None:
            return  # nothing we can screenshot

        # ensure folder exists
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = f"{item.name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", file_name)

        # save locally
        driver.save_screenshot(screenshot_path)

        # attach to allure
        allure.attach(
            driver.get_screenshot_as_png(),
            name=file_name,
            attachment_type=allure.attachment_type.PNG
        )
