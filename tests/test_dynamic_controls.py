from playwright.sync_api import Page, expect


def test_dynamic_controls(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")

    page.locator("#checkbox-example > button").click()
    expect(page.locator("#checkbox-example #message")).to_have_text("It's gone!")

    page.locator("#checkbox-example > button").click()
    expect(page.locator("#checkbox-example #message")).to_have_text("It's back!")
