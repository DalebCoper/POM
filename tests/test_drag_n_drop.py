from playwright.sync_api import Page, expect


def test_drag_n_drop(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/drag_and_drop")
    page.drag_and_drop("#column-a", "#column-b")

    expect(page.locator("#column-a")).to_have_text("B")
    expect(page.locator("#column-b")).to_have_text("A")
