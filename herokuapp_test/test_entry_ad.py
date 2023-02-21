from playwright.sync_api import Page, expect


def test_entry_ad(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/entry_ad")

    expect(page.locator(".modal")).to_be_visible()
