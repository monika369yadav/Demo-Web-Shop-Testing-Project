"""
Test Suite: Login
Covers manual Test Cases: TC-009 (valid login), TC-008 (invalid password)

Note: Uses a fixed, pre-registered test account. Before running these tests,
register this email once manually (or via test_register.py) so it exists
in the system.
"""

import pytest
from pages.login_page import LoginPage

TEST_EMAIL = "mona10august@gmail.com"   # must already be a registered account
TEST_PASSWORD = "Test@1234"             # replace with the real password used at registration


def test_login_fails_with_incorrect_password(driver):
    """TC-008: Verify login fails with incorrect password."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(TEST_EMAIL, "WrongPassword123")

    error_message = login_page.get_error_message()
    assert "credentials provided are incorrect" in error_message.lower()


def test_login_succeeds_with_correct_credentials(driver):
    """TC-009: Verify successful login with correct credentials."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    assert login_page.is_logged_in()
    assert TEST_EMAIL in login_page.get_logged_in_email()
