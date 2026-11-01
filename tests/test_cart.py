import pytest
from playwright.sync_api import expect


@pytest.mark.smoke
def test_add_item_updates_cart_badge(logged_in_page):
    """REQ-003: Adding an item shows a cart count of 1."""
    page = logged_in_page
    page.locator('[data-test="add-to-cart-sauce-labs-backpack"]').click()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

