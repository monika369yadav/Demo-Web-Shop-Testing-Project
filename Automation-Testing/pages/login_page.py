"""
Login Page — locators and actions for the Login page.
Maps to manual Test Cases: TC-008 (invalid login), TC-009 (valid login)
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://demowebshop.tricentis.com/login"

    # Locators
    EMAIL = (By.ID, "Email")
    PASSWORD = (By.ID, "Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input.button-1.login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".message-error")
    ACCOUNT_EMAIL_LINK = (By.CSS_SELECTOR, ".account")

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.type_text(self.EMAIL, email)
        self.type_text(self.PASSWORD, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def get_logged_in_email(self):
        return self.get_text(self.ACCOUNT_EMAIL_LINK)

    def is_logged_in(self):
        return self.is_visible(self.ACCOUNT_EMAIL_LINK)
