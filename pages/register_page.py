
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RegisterPage:

    # Locators variables
    GENDER_MALE = (By.CSS_SELECTOR, "input#gender-male")
    GENDER_FEMALE = (By.CSS_SELECTOR, "input#gender-female")
    FIRST_NAME = (By.CSS_SELECTOR, "input#FirstName")
    LAST_NAME = (By.CSS_SELECTOR, "input#LastName")
    EMAIL = (By.CSS_SELECTOR, "input#Email")
    COMPANY_NAME= (By.CSS_SELECTOR, "input#Company")
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, "input#NewsLetterSubscriptions_0__IsActive")
    PASSWORD = (By.CSS_SELECTOR, "input#Password")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "input#ConfirmPassword")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button#register-button")
    SUCCESS_MESSAGE=(By.XPATH,"//div[normalize-space()='Your registration completed']")
    CONFIRM_PASSWORD_ERROR=(By.CSS_SELECTOR,"span#ConfirmPassword-error")
    FIRST_NAME_ERROR=(By.ID,"FirstName-error")

    def __init__(self,driver):
        self.driver=driver

    # wait methods
    def _wait_for_visibility_of_element(self,locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))

    def _wait_for_element_clickable(self,locator):
        return WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))


    #url navigation method
    def open(self):
        self.driver.get("http://localhost:8090/register")

    # register form interaction methods
    def select_gender_male(self):
        male_radio=self._wait_for_element_clickable(self.GENDER_MALE)
        male_radio.click()

    def select_gender_female(self):
        female_radio=self._wait_for_element_clickable(self.GENDER_FEMALE)
        female_radio.click()

    def enter_first_name(self,first_name):
        name=self._wait_for_visibility_of_element(self.FIRST_NAME)
        name.clear()
        name.send_keys(first_name)

    def enter_last_name(self,last_name):
        surname=self._wait_for_visibility_of_element(self.LAST_NAME)
        surname.clear()
        surname.send_keys(last_name)

    def enter_email(self,email):
        email_id=self._wait_for_visibility_of_element(self.EMAIL)
        email_id.clear()
        email_id.send_keys(email)

    def enter_company(self,company):
        company_name=self._wait_for_visibility_of_element(self.COMPANY_NAME)
        company_name.clear()
        company_name.send_keys(company)

    def set_newsletter_subscription(self):
           newsletter_checkbox= self._wait_for_element_clickable(self.NEWSLETTER_CHECKBOX)
           if not newsletter_checkbox.is_selected():
               newsletter_checkbox.click()
           
    def unset_newsletter_subscription(self):
        newsletter_checkbox= self._wait_for_element_clickable(self.NEWSLETTER_CHECKBOX)
        if newsletter_checkbox.is_selected():
            newsletter_checkbox.click()
                   
    def enter_password(self,password):
        password_enter=self._wait_for_visibility_of_element(self.PASSWORD)
        password_enter.clear()
        password_enter.send_keys(password)

    def enter_confirm_password(self,confirm_password):
        confirmed_password=self._wait_for_visibility_of_element(self.CONFIRM_PASSWORD)
        confirmed_password.clear()
        confirmed_password.send_keys(confirm_password)

    def click_register(self):
        register_button=self._wait_for_element_clickable(self.REGISTER_BUTTON)
        register_button.click()



    #getter methods to validate entered value

    #helper method
    def _get_input_value(self,locator):
        element=self._wait_for_visibility_of_element(locator)
        return element.get_attribute("value")

    def _get_selected_status(self,locator):
        element=self._wait_for_visibility_of_element(locator)
        return element.is_selected()

    def is_gender_male_selected(self):
        return self._get_selected_status(self.GENDER_MALE)

    def is_gender_female_selected(self):
        return self._get_selected_status(self.GENDER_FEMALE)
    
    def get_first_name(self):
        return self._get_input_value(self.FIRST_NAME)


    def get_last_name(self):
        return self._get_input_value(self.LAST_NAME)

    def get_email(self):
        return self._get_input_value(self.EMAIL)

    def get_company(self):
        return self._get_input_value(self.COMPANY_NAME)

    def is_newsletter_subscribed(self):
        return self._get_selected_status(self.NEWSLETTER_CHECKBOX)
    
    def is_newsletter_unsubscribed(self):
        return not(self._get_selected_status(self.NEWSLETTER_CHECKBOX))
    
    def get_password(self):
        return self._get_input_value(self.PASSWORD)

    def get_confirmed_password(self):
        return self._get_input_value(self.CONFIRM_PASSWORD)

    def get_success_message(self):
        message=self._wait_for_visibility_of_element(self.SUCCESS_MESSAGE)
        return message.text

    def get_confirm_password_error(self):
        message=self._wait_for_visibility_of_element(self.CONFIRM_PASSWORD_ERROR)
        return message.text

    def get_first_name_error(self):
        message=self._wait_for_visibility_of_element(self.FIRST_NAME_ERROR)
        return message.text

    

    
    

    


    
