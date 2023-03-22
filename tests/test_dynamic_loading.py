from playwright.sync_api import Page, expect


def test_dynamic_loading_ele_hidden(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

    page.locator("#start > Button").click()
    expect(page.locator("#finish")).to_have_text("Hello World!")


def test_dynamic_loading_ele_render_after(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")

    page.locator("#start > Button").click()
    expect(page.locator("#finish")).to_have_text("Hello World!", timeout=6000)
