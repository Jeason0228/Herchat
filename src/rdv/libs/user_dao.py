from datetime import datetime, date


def check_phone_number(phone):
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

def get_all_user_by_line(db_page, sim_line):
    person_list = list(db_page.find({"sim_line": sim_line}))
    return person_list

def get_all_failed_by_line(rdv_page, sim_line):
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    failed_list = list(rdv_page.find({"$or": [{"sim_line": sim_line, "code_sent": False, "date": {"$lt": end, "$gte": start}}, {"sim_line": sim_line, "status": False, "date": {"$lt": end, "$gte": start}}, {
                       "sim_line": sim_line, "have_code": False, "date": {"$lt": end, "$gte": start}}]}))

    return failed_list

def get_all_failed(rdv_page):
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    failed_list = list(rdv_page.find({"$or": [{"code_sent": False, "date": {"$lt": end, "$gte": start}}, {"status": False, "date": {"$lt": end, "$gte": start}}, {
                       "have_code": False, "date": {"$lt": end, "$gte": start}}]}))

    return failed_list

def get_all_successed(rdv_page):
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    failed_list = list(rdv_page.find({"code_sent": True, "date": {"$lt": end, "$gte": start}}))

    return failed_list
