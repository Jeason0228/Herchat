from libs.utils import base_headers

import requests

import pandas as pd

def parse_excel(file):
    df = pd.read_excel(file)
    person_list = []
    for index, row in df.iterrows():
        person_list.append(row)
    return person_list

def detect_ok(url, p):

    rdv_response = requests.get(
            url,
            headers={
                **base_headers,
                "Host": "rendezvousparis.hermes.com",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                
            }
        )
    # print("Last name" in rdv_response.text)
    
    if "we are extremely sorry that we were not able to fulfill your request this time" not in rdv_response.text and "Last name" not in rdv_response.text:
        print(p)
