import re
from playwright.sync_api import expect
from pageObjects.LoginPage import LoginPage

valid_username = "student"
valid_password = "Password123"
invalid_username = "WrongUsername"
invalid_password = "WrongPassword"


def test_login_positive(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(valid_username, valid_password)

    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")
    expect(page.locator("body")).to_have_text(re.compile("Congratulations|successfully logged in"))
    expect(page.locator(".wp-block-button__link")).to_be_enabled()


def test_login_negative_username(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(invalid_username, invalid_password)

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator(".show")).to_have_text("Your username is invalid!")


def test_login_negative_password(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(valid_username, invalid_password)

    expect(page.locator("#error")).to_be_visible()
    expect(page.locator(".show")).to_have_text("Your password is invalid!")


def test_login_logout(page) -> None:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(valid_username, valid_password)
    login_page.logout()

    expect(login_page.login_button).to_be_visible()
