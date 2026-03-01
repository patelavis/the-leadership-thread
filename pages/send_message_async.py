from playwright.async_api import Page


class SendMessage:

    def __init__(self, page: Page):
        self.page = page

    async def load_page(self):
        await self.page.goto("https://automationintesting.online/")

    async def fill_form(
        self, name: str, email: str, phone: str, subject: str, description: str
    ):
        await self.contact_name.fill(name)
        await self.contact_email.fill(email)
        await self.contact_phone.fill(phone)
        await self.contact_subject.fill(subject)
        await self.contact_description.fill(description)

    async def submit(self):
        await self.submit_button.click()

    async def is_success_visiable(self):
        return await self.page.locator("section#contact").is_visible()

    async def get_success_message(self):
        return await self.page.locator("section#contact").inner_text()

    async def is_error_visiable(self):
        return await self.page.locator("div.alert.alert-danger").is_visible()

    async def get_error_message(self):
        return await self.page.locator("div.alert.alert-danger").inner_text()
