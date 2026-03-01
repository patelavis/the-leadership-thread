from playwright.sync_api import Page


class SendMessage:

    def __init__(self, page: Page):
        self.page = page
        self.contact_name = page.get_by_test_id("ContactName")
        self.contact_email = page.get_by_test_id("ContactEmail")
        self.contact_phone = page.get_by_test_id("ContactPhone")
        self.contact_subject = page.get_by_test_id("ContactSubject")
        self.contact_description = page.get_by_test_id("ContactDescription")
        self.submit_button = page.get_by_role("button", name="Submit")

    def load_page(self):
        self.page.goto("https://automationintesting.online/")

    def fill_form(
        self, name: str, email: str, phone: str, subject: str, description: str
    ):
        self.contact_name.fill(str(name))
        self.contact_email.fill(str(email))
        self.contact_phone.fill(str(phone))
        self.contact_subject.fill(str(subject))
        self.contact_description.fill(str(description))

    def submit(self):
        self.submit_button.click()

    def is_success_visiable(self):
        return self.page.locator("section#contact").is_visible()

    def get_success_message(self):
        message_text = self.page.locator("section#contact").inner_text()
        return message_text

    def is_error_visiable(self):
        return self.page.locator("div.alert.alert-danger").is_visible()

    def get_error_message(self):
        message_text = self.page.locator("div.alert.alert-danger").inner_text()
        return message_text
