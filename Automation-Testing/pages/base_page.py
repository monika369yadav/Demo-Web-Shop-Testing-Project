"""
Base Page — contains common methods reused across all page objects.
This is the foundation of the Page Object Model (POM) design pattern.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    # Shared header locator — appears on every page when logged in
    LOGOUT_LINK = (By.CSS_SELECTOR, "a.ico-logout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # waits up to 10 seconds for elements

    def logout(self):
        """Log the current user out via the header link (visible on any page)."""
        self.click(self.LOGOUT_LINK)

    def find(self, locator):
        """Wait until an element is visible, then return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        """Wait until an element is clickable, then click it."""
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Find a field, clear it, and type the given text."""
        field = self.find(locator)
        field.clear()
        field.send_keys(text)

    def get_text(self, locator):
        """Return the visible text of an element."""
        return self.find(locator).text

    def is_visible(self, locator):
        """Return True if element is visible, False if not found within timeout."""
        try:
            self.find(locator)
            return True
        except Exception:
            return False
