from re import sub
import random, string
from time import sleep
from pymongo import MongoClient
from datetime import datetime, date
from libs.five_sims import *
from libs.name import get_surname_name
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

def send_request(person_db, person_list):
    global TOTAL_COUNT

    all_rdv_object = {
        "date": datetime.now(),
        "prefer": "faubourg",
    }

    rdv_list = []
    for person in person_list:
        rdv = person.copy()
        _id = rdv.pop("_id")
        rdv["prefer"] = all_rdv_object["prefer"]
        rdv["date"] = datetime.now()
        rdv["phone_number"] = "33"+ str(person["phone_number"])
        print(rdv)
        redirct_url = send_rdv_infos(rdv)
        rdv["url"] = redirct_url
        rdv_page = person_db.rdv
        if redirct_url and len(redirct_url) >= len("https://rendezvousparis.hermes.com/client/register/"):
            rdv["status"] = True
        else:
            rdv["status"] = False
            print("rdv request sent failed")
        rdv_list.append(rdv)
    all_rdv_object["rdv_list"] = rdv_list
    rdv_page.insert_one(all_rdv_object)


def send_sms(rdv_page, phone_number):
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    # Make a query to the specific DB and Collection
    todey_rdv = rdv_page.find_one({"date": {"$lt": end, "$gte": start}})
    rdv_list = todey_rdv["rdv_list"]
    tried =0
    # while True:
    # print("waiting for sms...")
    new_rdv = rdv_page.find_one({"rdv_list": {"$elemMatch": {"phone_number": str(phone_number), "status": True, "have_code": True}}})
    person = new_rdv["rdv_list"][0]
    code = person.get("code", None)
    redirct_url = person.get("redirct_url", None)
    if code is not None:
        if send_sms_code(redirct_url, code):
            print("code sent")
    else:
        tried += 1
        print("retring...")
        if tried > 5:
            print("no code reveived")


def save_info(domain, country, number):
    global TOTAL_COUNT
    mongo_client = MongoClient()

    person_db = mongo_client.person_info
    person_page= person_db.person



    balance = get_balance()
    print(balance)


    for i in range(number):
        if TOTAL_COUNT >= number:
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
            # number_info = buy_number(country)
            
            # order_id = number_info["id"]
            # phone = number_info["phone"]

            # person_dict["phone_number"] = phone
            # person_dict["nummber_info"] = number_info
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



# save_info("rgmail", "usa")