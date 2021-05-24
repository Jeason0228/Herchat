import requests
import json
import time
import numpy as np
from pprint import pprint
from hermes_auth import get_captcha_challenge_sel, get_datadome, captcha_pass_anti, captcha_pass
from pymongo import MongoClient
from datetime import datetime
from mail import send_mail
from product_utils import find_new_products
# from geetest_session import GSession

mongo_client = MongoClient()

products_db = mongo_client.products_update
products = products_db.products

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
    dome = get_datadome()
    product_list_request = requests.get(
        BACK_END_URL,
        cookies={
            "datadome": dome,
            "ECOM_SESS": cookie["ECOM_SESS"],
        },
        headers={
            **base_headers,
            "Host": "bck.hermes.com",
            "Accept": "application/json, text/plain, */*",
            "Origin": ORIGIN_URL,
            "Referer": REFER_URL,
            "Cookie": "datadome=%s" % (dome),
        },
    )
    if product_list_request.status_code == 200:
        return product_list_request.json()
    elif product_list_request.status_code == 403:
        print(product_list_request.json()["url"])
        challenge = get_captcha_challenge_sel(BACK_END_URL)
        # gss.get_php()
        print(challenge)
        captcha_pass_anti(challenge, BACK_END_URL ,product_list_request.json()["url"])

        # raise ConnectionRefusedError("Session may be expired, try to re-launch the cookies.")

ecom_cookie = load_cookies()




for i in range(20):
    print("{} times".format(i))
    prod = get_products_list(ecom_cookie)
# print(prod)
# time.sleep(5)
# if products is not None and products.estimated_document_count() != 0:
#     last_update = products.find().sort("update_time", -1).limit(1)[0]
#     old_total = last_update["total"]
# else:
#     old_total = 0

# while True:
#     wait_time = np.random.randint(5, 10)
#     print("Wait %d seconds." % wait_time)
#     time.sleep(wait_time)
#     try:

#         product_list_json = get_products_list(ecom_cookie)
#         new_total = product_list_json["total"]
#         print("Find {} products at {}".format(new_total, datetime.now()))
#         if new_total != old_total:
#             print("Find new products.")
#             product_list = { key: product_list_json[key] for key in ["total", "products"] }
#             product_list.update({
#                 "update_time": datetime.now()
#             })
#             products.insert_one(product_list)

#             # Find new product info
#             old_products = products.find_one(sort=[("update_time", -1)])
#             new_products_info = find_new_products(old_products=old_products, new_products=product_list_json)
#             # Send mail
#             send_mail(info = {
#                 "old_total": old_total,
#                 "new_total": new_total,
#                 "new_products": new_products_info,
#                 "update_time": product_list["update_time"]
#             })
#             old_total = new_total
#         else:
#             print("No new products added.")
#     except ConnectionRefusedError as e:
#         print(e)
#         request_ecom_cookies()
        # ecom_cookie = load_cookies()
        # ecom_cookie.update({"datadome": get_datadome().split("=")[1]})
        # break