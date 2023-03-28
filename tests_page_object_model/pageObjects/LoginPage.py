class LoginPage:
    def __init__(self, page):
        self.page = page
        self._login = page.locator("div > #username")
        self._password = page.locator("div > #password")

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def log_in(self, login_login, login_password):
        self._login.fill(login_login)
        self._password.fill(login_password)
        self.page.locator("div > #submit").click()

    def log_out(self):
        self.page.locator(".wp-block-button__link").click()

    @property
    def login_button(self):
        return self._login
