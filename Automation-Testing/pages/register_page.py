"""
Register Page — locators and actions for the Register page.
Maps to manual Test Cases: TC-006 (duplicate email), TC-007 (valid registration)
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegisterPage(BasePage):
    URL = "https://demowebshop.tricentis.com/register"

    # Locators
    GENDER_FEMALE = (By.ID, "gender-female")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    CONFIRM_PASSWORD = (By.ID, "ConfirmPassword")
    REGISTER_BUTTON = (By.ID, "register-button")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".result")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".validation-summary-errors")

    def open(self):
        self.driver.get(self.URL)

    def register(self, first_name, last_name, email, password):
        self.click(self.GENDER_FEMALE)
        self.type_text(self.FIRST_NAME, first_name)
        self.type_text(self.LAST_NAME, last_name)
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)
        self.type_text(self.CONFIRM_PASSWORD, password)
        self.click(self.REGISTER_BUTTON)

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
