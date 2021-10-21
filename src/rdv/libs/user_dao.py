from datetime import datetime

def check_phone_number(phone):
    print(phone)
    if len(phone) == 10 and phone[0] == "0":
        return phone[1:]
    else:
        return phone

def insert_user(db_page, person_list):
    for person in person_list:
        person.update({
            "date": datetime.now(),
            "phone_number": check_phone_number(str(person["phone_number"]))
        })
        db_page.insert_one(person)

def get_all_users(db_page):
    person_list = list(db_page.find())
    
    return person_list