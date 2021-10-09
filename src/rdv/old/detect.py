from utils import base_headers
from sms_code import send_sms_code
import requests
from recaptcha import g_response
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def parse_excel(file):
    df = pd.read_excel(file)
    person_list = []
    for index, row in df.iterrows():
        person_list.append(row)
    return person_list

def detect(url, p):

    rdv_response = requests.get(
            url,
            headers={
                **base_headers,
                "Host": "rendezvousparis.hermes.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                
            }
        )
    if "we are extremely sorry that we were not able to fulfill your request this time" not in rdv_response.text:
        print(p)

plist = parse_excel("/Users/PENGHanyuan/Downloads/person_2.xlsx")
for p in plist:
    url = plist[2]["url"].replace("/register/", "/")
    detect(url, p)
