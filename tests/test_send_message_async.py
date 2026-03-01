# from pages.send_message_async import SendMessage
# import pandas as pd
# import pytest


# @pytest.mark.asyncio
# async def test_valid_contact_submisstion(page):

#     df = pd.read_excel("fixtures/inputs.xlsx")

#     df["Status"] = None
#     df["Message"] = None

#     home = SendMessage(page=page)

#     for i, row_data in df.iterrows():

#         try:
#             await home.load_page()

#             await home.fill_form(
#                 name=row_data.get("name", ""),
#                 email=row_data.get("email", ""),
#                 phone=row_data.get("phone", ""),
#                 subject=row_data.get("subject", ""),
#                 description=row_data.get("description", ""),
#             )

#             await home.submit()

#             await page.wait_for_load_state("networkidle")

#             if await home.is_success_visiable():
#                 df.loc[i, "Status"] = "Pass"
#                 df.loc[i, "Message"] = await home.get_success_message()
#             elif await home.is_error_visiable():
#                 df.loc[i, "Status"] = "Pass"
#                 df.loc[i, "Message"] = await home.get_error_message()
#             else:
#                 df.loc[i, "Status"] = "Fail"
#         except Exception as e:
#             df.loc[i, "Status"] = "Fail"
#             df.loc[i, "Message"] = str(e)

#     df.to_excel("Output_result.xlsx", index=False)
