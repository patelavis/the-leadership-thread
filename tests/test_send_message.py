from pages.send_message import SendMessage
from fixtures.test_data import VALID_CONTACT


def test_valid_contact_submisstion(page):
    home = SendMessage(page=page)

    home.load_page()

    home.fill_form(
        name=VALID_CONTACT.get("name"),
        email=VALID_CONTACT.get("email"),
        phone=VALID_CONTACT.get("phone"),
        subject=VALID_CONTACT.get("subject"),
        description=VALID_CONTACT.get("description"),
    )

    home.submit()

    page.wait_for_timeout(2000)

    message = (
        home.get_success_message()
        if home.is_success_visiable()
        else home.get_error_message()
    )

    assert "Thanks for getting in" in message


def test_invalid_contact_submisstion(page):
    home = SendMessage(page=page)

    home.load_page()
    home.fill_form(
        name=VALID_CONTACT.get("name", "A"),
        email="1",
        phone="",
        subject="",
        description="",
    )

    home.submit()
    alert = page.locator("div.alert.alert-danger")
    alert.wait_for(state="visible")

    assert alert.is_visible()
