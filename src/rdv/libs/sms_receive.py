import pandas as pd
import re


def save_sms_code(rdv_page, phone_number, text, com, date):
    codes = re.findall(r'\d+', text)
    print(codes)
    if len(codes) > 0:
        rdv_page.update_one( {"phone_number": phone_number, "status": True} ,{ "$set": { "code": codes[0]} })
        return True
    else:
        print("SMS error, no code in the text")


