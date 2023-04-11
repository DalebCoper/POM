from playwright.sync_api import expect
from pageObjects.Exceptions import Exceptions

Text_to_input = "text to input"


def test_add_element(page) -> None:
    exceptions_page = Exceptions(page)
    exceptions_page.navigate()
    exceptions_page.add_element()

    expect(page.locator("#confirmation")).to_have_text("Row 2 was added")


def test_save_added_element(page) -> None:
    exceptions_page = Exceptions(page)
    exceptions_page.navigate()
    exceptions_page.add_save_element(Text_to_input)

    expect(page.locator("#confirmation")).to_have_text("Row 2 was saved")


def test_edit_element(page) -> None:
    exceptions_page = Exceptions(page)
    exceptions_page.navigate()
    exceptions_page.edit_text(Text_to_input)

    expect(page.locator("#confirmation")).to_have_text("Row 1 was saved")
