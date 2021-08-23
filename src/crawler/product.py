import requests
import json
import time
import numpy as np
from pprint import pprint

BACK_END_URL = "https://bck.hermes.com/products?locale=fr_fr&category=WOMENBAGSBAGSCLUTCHES&sort=relevance"
ORIGIN_URL = "https://www.hermes.com"
REFER_URL = "https://www.hermes.com/"

base_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:88.0) Gecko/20100101 Firefox/88.0",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
}

def load_cookies(path="../json/ecom_sess.json"):
    with open(path, "r") as file:
        return json.load(file)

def get_products_list(cookie):

    product_list_request = requests.get(
        BACK_END_URL,
        cookies={
            "datadome": cookie["datadome"],
            "ECOM_SESS": cookie["ecom_sess"],
        },
        headers={
            **base_headers,
            "Host": "bck.hermes.com",
            "Accept": "application/json, text/plain, */*",
            "Origin": ORIGIN_URL,
            "Referer": REFER_URL,
            "Cookie": "datadome=%s; ECOM_SESS=%s" % (cookie["datadome"], cookie["ecom_sess"]),
            "TE": "Trailers",
        },
    )
    return product_list_request.json()

ecom_cookie = load_cookies()

while True:
    wait_time = np.random.randint(10, 20)
    print("Wait %d seconds." % wait_time)
    time.sleep(wait_time)
    product_list_json = get_products_list(ecom_cookie)
    print(product_list_json["total"])