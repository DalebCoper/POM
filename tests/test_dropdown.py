from playwright.sync_api import Page, expect


def test_dropdown_opt_1(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option(index=1)

    expect(page.locator("#dropdown")).to_have_value("1")


def test_dropdown_opt_2(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator("#dropdown").select_option(index=2)

    expect(page.locator("#dropdown")).to_have_value("2")
