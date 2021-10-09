import re
from time import sleep, time
import requests
from requests import api
from libs.utils import api_key
from libs.rdv_page import send_rdv_infos
from libs.sms_code import send_sms_code
from random import randint


headers = {
    'Authorization': 'Bearer ' + api_key,
    'Accept': 'application/json',
}

def get_balance():

    response = requests.get('https://5sim.net/v1/user/profile', headers=headers)
    return response.json()["balance"]

def cancel_order(order_id):
    response = requests.get(f'https://5sim.net/v1/user/cancel/{order_id}', headers=headers)
    print("order canceled")
    return response.status_code == 200

def buy_number(country):
    operator = 'any'
    product = 'other'

    response = requests.get('https://5sim.net/v1/user/buy/activation/' + country + '/' + operator + '/' + product, headers=headers)
    print(response.json())
    return response.json()

def get_sms(order_id):
    sleep(15)
    response = requests.get(f'https://5sim.net/v1/user/check/{order_id}', headers=headers)
    print(response.json()["sms"])
    return response.json()["sms"]

def finished_order(order_id):
    response = requests.get(f'https://5sim.net/v1/user/finish/{order_id}', headers=headers)
    print("order finished")
    return response.status_code == 200

# person = {
#     "surname": "PENG",
#     "name": "Hanyuan",
#     "phone_country": "GB",
#     "email": f"kutauzherchat{randint(10, 100)}@snapmail.cc",
#     "passport_id": f"9918040{randint(100, 999)}",
#     "prefer": "faubourg"
# }
# print(person)
# balance = get_balance()
# print(balance)

# if balance > 0:
#     from excel_parse import parse_excel
#     person_list = parse_excel('data/Book1.xlsx')
#     for p in person_list:
#         print(p)
#         number_info = buy_number()
#         order_id = number_info["id"]
#         print(order_id)
#         phone = number_info["phone"]
#         p["phone_country"] = "GB"
#         p["phone_number"] = phone
#         redirct_url = send_rdv_infos(p)
#         sms = get_sms(order_id)
#         code = sms[0]["code"]
#         print(code)
#         # redirct_url = "https://rendezvousparis.hermes.com/client/register/T5REM9"
#         if send_sms_code(redirct_url, code):
#             finished_order(order_id)






