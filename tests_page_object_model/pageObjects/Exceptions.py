class Exceptions:
    def __init__(self, page):
        self.page = page
        self._text_to_input = page.locator("#row2 > .input-field")

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-exceptions/")

    def add_element(self):
        self.page.locator("div > #add_btn").click()

    def add_save_element(self, text):
        self.page.locator("#add_btn").click()
        self._text_to_input.fill(text)
        self.page.locator("#row2 > #save_btn").click()
