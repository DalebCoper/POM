class LoginPage:
    def __init__(self, page):
        self.page = page
        self.input_login_selector = page.locator("#username")
        self.input_password_selector = page.locator("#password")

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, login_login, login_password):
        self.input_login_selector.fill(login_login)
        self.input_password_selector.fill(login_password)
        self.page.locator("#submit").click()

    def logout(self):
        self.page.locator(".wp-block-button__link").click()

    @property
    def login_button(self):
        return self.input_login_selector
