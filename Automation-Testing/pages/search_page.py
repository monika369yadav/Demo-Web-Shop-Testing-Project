"""
Search Page — locators and actions for the store-wide Search feature.
Maps to manual Test Case: TC-015 (search returns no results — known bug BUG-003)
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    URL = "https://demowebshop.tricentis.com/search"

    # Locators
    SEARCH_KEYWORD_FIELD = (By.ID, "q")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "input.button-1.search-button")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".search-results .no-result")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, ".product-item")

    def open(self):
        self.driver.get(self.URL)

    def search_for(self, keyword):
        self.type_text(self.SEARCH_KEYWORD_FIELD, keyword)
        self.click(self.SEARCH_BUTTON)

    def has_no_results_message(self):
        return self.is_visible(self.NO_RESULTS_MESSAGE)

    def get_result_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_ITEMS))
