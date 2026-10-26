from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_nopcommerce_homepage(driver_setup):
    print("Test started")

    driver.get("http://localhost:8090")

    WebDriverWait(driver, 30).until(
        EC.title_contains("Your store. Home page title")
    )

    print("Actual page title:", driver.title)
    print("Current URL:", driver.current_url)

    assert driver.title == "Your store. Home page title"
    assert driver.current_url == "http://localhost:8090/"
