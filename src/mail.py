import smtplib
import ssl
from email.message import EmailMessage
from product_utils import decompose_product_info
port = 465  # For SSL
password = "Herchat0130"

# Create a secure SSL context
context = ssl.create_default_context()
sender_email = "herchat.server@gmail.com"
receiver_email = "penghanyuan@gmail.com"

message = EmailMessage()
message.set_content('This is my message')

message['Subject'] = 'Hermes update information'
message['From'] = sender_email
message['To'] = receiver_email


def send_mail(info):
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("herchat.server@gmail.com", password)

        text = """

        Hermes has an update at {}:
            - Old number of product: {},
            - New number of product: {},

        New product:
        """.format(info["update_time"], info["old_total"], info["new_total"])
        product_info_text = ""
        for p in info["new_products"]:
            decomposed_product = decompose_product_info(p)
            product_info_text += """
                - Sku: {},
                - Name: {},
                - Price: {} €,
                - Url: {}
            ---------------------------------------
            """.format(decomposed_product["sku"], decomposed_product["title"], decomposed_product["price"], decomposed_product["url"])
        text += product_info_text
        message.set_content(text)

        print("Sending mail.")
        server.send_message(message, sender_email, receiver_email)


if __name__ == "__main__":
    import requests
    import json
    import time
    import numpy as np
    from pprint import pprint
    from hermes_auth import request_ecom_cookies, get_datadome
    from pymongo import MongoClient
    from datetime import datetime

    mongo_client = MongoClient()

    products_db = mongo_client.products_update
    products = products_db.products

    all_products = products.find_one()
    send_mail({
                "old_total": 1,
                "new_total": 2,
                "new_products": [all_products["products"]["items"][0]],
                "update_time": 122
            })