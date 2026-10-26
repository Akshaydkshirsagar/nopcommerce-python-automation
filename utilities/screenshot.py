from pathlib import Path
from datetime import datetime 

SCREENSHOT_DIR=Path(__file__).resolve().parents[1]/"screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

def capture_screenshot(driver, test_name):

    timestamp=datetime.now().strftime("%Y%m%d_at_%H%M%S")
    file_apth=SCREENSHOT_DIR/f"{test_name}_{timestamp}.png"
    driver.save_screenshot(str(file_apth))

    return file_apth