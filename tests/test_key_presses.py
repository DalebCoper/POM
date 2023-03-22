from playwright.sync_api import Page, expect


def test_key_presses_shift(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.locator("#target").click(modifiers=["Shift"])

    expect(page.locator("#result")).to_have_text("You entered: SHIFT")

def test_key_presses_C(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/key_presses")
    page.locator("#target").press("C")

    expect(page.locator("#result")).to_have_text("You entered: C")

