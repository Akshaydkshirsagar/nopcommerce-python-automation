from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_nopcommerce_homepage(driver_setup):
    print("Test started")

    driver_setup.get("http://localhost:8090")

    WebDriverWait(driver_setup, 30).until(
        EC.title_contains("Your store. Home page title")
    )

    print("Actual page title:", driver_setup.title)
    print("Current URL:", driver_setup.current_url)

    assert driver_setup.title == "Your store. Home page title"
    assert driver_setup.current_url == "http://localhost:8090/"
