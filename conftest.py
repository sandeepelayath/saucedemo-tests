import pytest
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page):
    """A browser page already logged in as the standard user."""
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    return page

