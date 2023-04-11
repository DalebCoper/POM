class Exceptions:
    def __init__(self, page):
        self.page = page
        self.add_button = page.locator("#add_btn")
        self.text_to_input = page.locator("#row2 > .input-field")
        self.save_added_element = page.locator("#row2 > #save_btn")
        self.edit_button = page.locator("#edit_btn")
        self.text_to_edit = page.locator(".input-field")
        self.save_edited_element = page.locator("#save_btn")

    def navigate(self):
        self.page.goto("https://practicetestautomation.com/practice-test-exceptions/")

    def add_element(self):
        self.add_button.click()

    def add_save_element(self, text):
        self.add_button.click()
        self.text_to_input.fill(text)
        self.save_added_element.click()

    def edit_text(self, text):
        self.edit_button.click()
        self.text_to_edit.fill(text)
        self.save_edited_element.click()

#testing