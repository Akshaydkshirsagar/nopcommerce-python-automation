
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_nopcommerce_homepage(driver_setup):
    driver = driver_setup
    driver.get("http://localhost:8090/")

    wait = WebDriverWait(driver, 60)

    # Wait until the page has a title
    wait.until(lambda d: d.title.strip() != "")

    actual_title = driver.title
    actual_url = driver.current_url

    print("Actual page title:", actual_title)
    print("Current URL:", actual_url)

    # Check the expected title
    assert actual_title == "Your store. Home page title", (
        f"Unexpected page title: {actual_title!r}; URL: {actual_url}"
    )

    assert actual_url == "http://localhost:8090/"
