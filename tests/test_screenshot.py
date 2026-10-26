from utilities.screenshot import capture_screenshot

def test_screenshot_example(driver_setup):
    driver_setup.get("http://localhost:8090")
    screenshot_path=capture_screenshot(driver_setup,"homepage")
    print(f"screenshot saved at:{screenshot_path}")
    assert screenshot_path.exists()