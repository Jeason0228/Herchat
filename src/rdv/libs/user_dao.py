from datetime import datetime

def insert_user(db_page, person_list):
    for person in person_list:
        person.update({
            "date": datetime.now()
        })
        db_page.insert_one(person)

def get_all_users(db_page):
    person_list = list(db_page.find())
    
    return person_list