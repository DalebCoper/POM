from playwright.sync_api import Page, expect


def test_checkboxes(page: Page) -> None:
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    page.get_by_role("checkbox").nth(0).set_checked(True)
    page.get_by_role("checkbox").nth(1).set_checked(False)

    expect(page.get_by_role("checkbox").nth(0)).to_be_checked()
    expect(page.get_by_role("checkbox").nth(1)).not_to_be_checked()
