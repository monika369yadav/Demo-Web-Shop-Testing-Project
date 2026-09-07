"""
Test Suite: Registration
Covers manual Test Cases: TC-007 (valid registration), TC-006 (duplicate email)
"""

import time
from pages.register_page import RegisterPage


def unique_email():
    """Generate a unique email so repeated test runs don't collide."""
    return f"qa.automation.{int(time.time())}@example.com"


def test_registration_with_valid_details(driver):
    """TC-007: Verify successful registration with valid, unique details."""
    register_page = RegisterPage(driver)
    register_page.open()

    email = unique_email()
    register_page.register("Mona", "Singh", email, "Test@1234")

    success_message = register_page.get_success_message()
    assert "Your registration completed" in success_message


def test_registration_fails_with_duplicate_email(driver):
    """TC-006: Verify registration fails when email already exists."""
    register_page = RegisterPage(driver)
    email = unique_email()

    # Step 1: Register once so this email exists in the system
    register_page.open()
    register_page.register("Mona", "Singh", email, "Test@1234")
    assert "Your registration completed" in register_page.get_success_message()

    # Step 2: Log out, then try registering again with the SAME email
    register_page.logout()
    register_page.open()
    register_page.register("Mona", "Singh", email, "Test@1234")

    error_message = register_page.get_error_message()
    assert "already exists" in error_message.lower()
