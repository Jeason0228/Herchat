from re import sub
import random, string
from time import sleep
from pymongo import MongoClient
from datetime import datetime, date
from five_sims import *
from name import get_surname_name
from stem import Signal, response
from stem.control import Controller
import threading

TOTAL_COUNT = 0
locker = threading.Lock()
country_code = {
    "usa": "US",
    "china": "CN",
    "france": "FR"
}


def get_ip():
    ip = requests.get('https://api.ipify.org').text
    print('My public IP address is: {}'.format(ip))

def email_account(fullname, domain):
    subfix = f"@{domain}.uu.me"
    code = "zi"
    rand_num = randint(1, 10)
    if rand_num <= 3:
        account = fullname + code
    elif rand_num <= 7:
        account = code + fullname
    else:
        charset = [c for c in fullname]
        rand_id = randint(1, len(charset))
        charset.insert(rand_id - 1, code)
        account = ''.join(charset)
    return account + subfix


def save_info(domain, country):
    global TOTAL_COUNT
    mongo_client = MongoClient()

    person_db = mongo_client.person_info
    person_page= person_db.person



    balance = get_balance()
    print(balance)


    for i in range(250):
        if TOTAL_COUNT >= 1200:
            break
        else:
            # get_ip()
            person_dict = {}
            surname, name, fullname = get_surname_name()
            person_dict["surname"] = surname
            person_dict["name"] = name
            person_dict["phone_country"] = country_code[country]
            person_dict["prefer"] = "faubourg"
            person_dict["email"] = email_account(fullname, domain)
            person_dict["passport_id"] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(9))
            # person_dict["phone_number"] = "111"
            number_info = buy_number(country)
            
            order_id = number_info["id"]
            phone = number_info["phone"]

            person_dict["phone_number"] = phone
            person_dict["nummber_info"] = number_info
            person_dict["date"] = datetime.now()
            redirct_url = send_rdv_infos(person_dict)
            person_dict["url"] = redirct_url

            person_page.insert_one(person_dict)

            sms = get_sms(order_id)
            try:
                code = sms[0]["code"]
                # print(code)
                if send_sms_code(redirct_url, code):
                    finished_order(order_id)
                    with locker:
                        TOTAL_COUNT += 1
            except IndexError as e:
                print("sms problem, finished the order and continue")
                cancel_order(order_id)



