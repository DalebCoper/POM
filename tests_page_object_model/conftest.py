class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login = page.locator("div > #username")
        self.password = page.locator("div > #password")

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-login/")

    def login(self, login_login, login_password):
        self.login.fill(login_login)
        self.password.fill(login_password)
        self.page.locator("div > #submit").click()
