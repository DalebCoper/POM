from playwright.sync_api import expect
from pageObjects.LoginPage import LoginPage


def test_login_positive(page) -> None:
    page = page
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.log_in("student", "Password123")

    expect(page.locator(".post-title")).to_have_text("Logged In Successfully")
