
from pages.register_page import RegisterPage
from utilities.test_data_generator import generate_unique_email

class TestRegisterPage:

    def test_successful_register_process(self,driver_setup):
        rp=RegisterPage(driver_setup)

        rp.open()
        rp.select_gender_male()
        rp.enter_first_name("Akshay")
        rp.enter_last_name("ksh")
        email=generate_unique_email()
        rp.enter_email(email)
        rp.enter_company("Infy")
        rp.set_newsletter_subscription()
        rp.enter_password("Test@123")
        rp.enter_confirm_password("Test@123")
        

        assert rp.is_gender_male_selected(), "desired gender is not selected"
        assert rp.get_first_name()=="Akshay","wrong first name"
        assert rp.get_last_name()=='ksh',"wrong last name"
        assert rp.get_email()==email,"wrong email id"
        assert rp.get_company()=="Infy","erong company name"
        assert rp.is_newsletter_subscribed(),"newsletter subscription not selected"
        assert rp.get_password()=='Test@123',"wrong password"
        assert rp.get_confirmed_password()=="Test@123","wrong confirmed password"
        rp.click_register()
        assert rp.get_success_message() == "Your registration completed","invalid message"


