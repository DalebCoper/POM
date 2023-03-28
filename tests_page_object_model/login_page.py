from playwright.sync_api import expect
from pageObjects.LoginPage import LoginPage


def test_login_positive(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.log_in("student", "Password123")

    expect(page.locator(".post-title")).to_have_text("Logged In Successfully")


def test_login_negative_username(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.log_in("WrongUsername", "WrongPassword")

    expect(page.locator(".show")).to_have_text("Your username is invalid!")


def test_login_negative_password(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.log_in("student", "WrongPassword")

    expect(page.locator(".show")).to_have_text("Your password is invalid!")


def test_login_logout(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.log_in("student", "Password123")
    login_page.log_out()

    expect(login_page.login_button).to_be_visible()
