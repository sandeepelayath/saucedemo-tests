import re

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_valid_user_can_log_in(page: Page):
    """REQ-001: A valid user can log in and see the product list."""
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile(r".*/inventory\.html"))
    expect(page.locator(".title")).to_have_text("Products")


@pytest.mark.parametrize(
    "user, pwd, message",
    [
        ("standard_user", "wrong_password", "do not match"),
        ("locked_out_user", "secret_sauce", "locked out"),
        ("standard_user", "", "Password is required"),
        ("", "secret_sauce", "Username is required"),
    ],
)
def test_invalid_login_shows_error(page: Page, user, pwd, message):
    """REQ-002: Invalid or blocked logins are rejected with a clear message."""
    login = LoginPage(page)
    login.open()
    login.login(user, pwd)
    expect(login.error).to_contain_text(message)

