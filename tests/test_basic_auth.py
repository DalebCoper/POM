from playwright.sync_api import Page, expect


def test_auth_positive(page: Page) -> None:
    page.goto("https://admin:admin@the-internet.herokuapp.com/basic_auth")

    expect(page.locator("#content p")).to_have_text("Congratulations! You must have the proper credentials.")


def test_auth_negative(page: Page) -> None:
    page.goto("https://wrongUN:wrongPW@the-internet.herokuapp.com/basic_auth")

    expect(page.locator("body")).to_have_text("Not authorized")


