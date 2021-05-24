def diff_product_list(list_a, list_b):
    return [x for x in list_a if x not in list_b]

def find_new_products(old_products, new_products):

    # TODO: Optimize this method

    old_list = old_products["products"]["items"]
    new_list = new_products["products"]["items"]

    old_sku = set([item["sku"] for item in old_list])
    new_sku = set([item["sku"] for item in new_list])

    diff_sku = new_sku ^ old_sku

    diff_list = []

    for p in new_list:
        if p["sku"] in diff_sku:
            diff_list.append(p)

    return diff_list

def decompose_product_info(product):
    sku = product["sku"]
    title = product["title"]
    url = "https://www.hermes.com/fr/fr%s" % product["url"]
    price = product["price"] 

    return {
        "sku": sku,
        "title": title,
        "url": url,
        "price": price
    }

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
    print(decompose_product_info(all_products["products"]["items"][0]))
