import pandas as pd
import re


def save_sms_code(rdv_page, phone_number, text, com, date):
    codes = re.findall(r'\d+', text)
    print(codes)
    if len(codes) > 0:
        # rdv_object = rdv_page.find_one()
        print("update")
        rdv_page.update_one({"rdv_list": {"$elemMatch": {"phone_number": str(phone_number), "status": True}}},
        { "$set": { "rdv_list.$.code": codes[0], "rdv_list.$.have_code": True} })
        return True
    else:
        print("SMS error, no code in the text")


