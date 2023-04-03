from playwright.sync_api import expect
from pageObjects.Exceptions import Exceptions


def test_no_such_element_exception(page) -> None:
    exceptions_page = Exceptions(page)
    exceptions_page.navigate()
    exceptions_page.add_element()

    expect(page.locator("#confirmation")).to_have_text("Row 2 was added")


def test_element_not_interactable_exception(page) -> None:
    exceptions_page = Exceptions(page)
    exceptions_page.navigate()
    exceptions_page.add_save_element("text to input")

    expect(page.locator("#confirmation")).to_have_text("Row 2 was saved")
