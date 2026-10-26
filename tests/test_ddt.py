import json
import pytest
from pathlib import Path
from pages.register_page import RegisterPage
from utilities.test_data_generator import generate_unique_email
from utilities.logger import get_logger
logger = get_logger(__name__)

DATA_FILE=(Path(__file__).resolve().parents[1]/"test_data"/"register_data.json")

with open(DATA_FILE,encoding="utf8") as file:
    REGISTER_DATA=json.load(file)

@pytest.mark.parametrize("test_data",REGISTER_DATA,ids=[case["test_case"] for case in REGISTER_DATA])
def test_registration(driver_setup,test_data):

    logger.info("Starting the test %s",test_data["test_case"])

    rp=RegisterPage(driver_setup)
    
    rp.open()
    logger.info("registration page opened")

    if test_data["gender"]=="male":
        rp.select_gender_male()
    elif test_data["gender"]=="female":
        rp.select_gender_female()
    else:
        pytest.fail(f"Unsupported gender: {test_data['gender']}")

    rp.enter_first_name(test_data["first_name"])
    rp.enter_last_name(test_data["last_name"])

    email=test_data["email"]
    if test_data["expected_result"]=="success":
        email=generate_unique_email(email)
    rp.enter_email(email)

    rp.enter_company(test_data["company"])

    if test_data["newsletter"]:
        rp.set_newsletter_subscription()
    else:
        rp.unset_newsletter_subscription()

    rp.enter_password(test_data["password"])
    rp.enter_confirm_password(test_data["confirm_password"])

            
    if test_data["gender"]=="male":
        assert rp.is_gender_male_selected(), "desired gender is not selected"
    elif test_data["gender"]=="female":
        assert rp.is_gender_female_selected(), "desired gender is not selected"

    assert rp.get_first_name()==test_data["first_name"],"wrong first name"
    assert rp.get_last_name()==test_data["last_name"],"wrong last name"
    assert rp.get_email()==email,"wrong email id"
    assert rp.get_company()==test_data["company"],"erong company name"

    if test_data["newsletter"]:
        assert rp.is_newsletter_subscribed(),"newsletter subscription not selected"
    else:
        assert rp.is_newsletter_unsubscribed(),"newsletter subscription not selected"
    assert rp.get_password()==test_data["password"],"wrong password"
    assert rp.get_confirmed_password()==test_data["confirm_password"],"wrong confirmed password"
    rp.click_register()
    logger.info("Register button clicked.")

    if test_data["expected_result"]=="success":
        assert rp.get_success_message() == "Your registration completed","invalid message"
        logger.info("registration successful")

    elif test_data["expected_result"]=="password_mismatch":
    
        assert rp.get_confirm_password_error()=="The password and confirmation password do not match.","wrong password mistmatch message"
        logger.info("Password mismatch validation successful")
    
    elif test_data["expected_result"]=="required_field_error":
        assert rp.get_first_name_error()=="First name is required.", "wrong required fiel error message"
        logger.info("required field validation")
    else:
        pytest.fail(f"unsupported expected result :, {test_data["expected_result"]}")
                
    
