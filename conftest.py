# This file manages shared pytest fixtures.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utilities.screenshot import capture_screenshot



@pytest.fixture
def driver_setup():
    options = Options()
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    try:
        yield driver
    finally:
        driver.quit()



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot when the test execution fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver_setup")

        if driver:
            test_name = item.name.replace("[", "_").replace("]", "")

            try:
                screenshot_path = capture_screenshot(driver, test_name)
                print(f"\nScreenshot saved: {screenshot_path}")
            except Exception as error:
                print(f"\nCould not capture screenshot: {error}")