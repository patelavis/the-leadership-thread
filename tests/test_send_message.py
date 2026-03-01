from pages.send_message import SendMessage
from fixtures.test_data import VALID_CONTACT
import pandas as pd


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


def test_sync_message_from_excel(page):

    df = pd.read_excel("fixtures/inputs.xlsx")

    df["Status"] = None
    df["Message"] = None

    home = SendMessage(page=page)

    for i, row_data in df.iterrows():
        try:
            home.load_page()

            home.fill_form(
                name=row_data.fillna("").get("name"),
                email=row_data.fillna("").get("email"),
                phone=row_data.fillna("").get("phone"),
                subject=row_data.fillna("").get("subject"),
                description=row_data.fillna("").get("description"),
            )

            home.submit()

            page.wait_for_load_state("networkidle")

            if home.is_success_visiable():
                df.loc[i, "Status"] = "Pass"
                df.loc[i, "Message"] = home.get_success_message()
            elif home.is_error_visiable():
                df.loc[i, "Status"] = "Pass"
                df.loc[i, "Message"] = home.get_error_message()
            else:
                df.loc[i, "Status"] = "Fail"
        except Exception as e:
            df.loc[i, "Status"] = "Fail"
            df.loc[i, "Message"] = str(e)

    df.to_csv("__test_result.csv")
