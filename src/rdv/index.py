from flask import Flask
from flask import render_template
from pymongo import MongoClient
from datetime import datetime, date
from save_info import *
import pandas as pd
from flask import send_file

app = Flask(__name__)
mongo_client = MongoClient()

person_db = mongo_client.person_info
person_page= person_db.person

@app.route("/run")
def run():
            
    try:
        for i in range(4):
            x = threading.Thread(target=save_info)
            x.start()
        
    except:
        print("Error: unable to start thread")
    return "runing..."

@app.route("/count")
def count():
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    return str(date.today()) + " 总数：" + str(person_page.find({"date": {"$lt": end, "$gte": start}}).count())

@app.route("/csv")
def csv():
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    # Make a query to the specific DB and Collection
    cursor = person_page.find({"date": {"$lt": end, "$gte": start}})

    # Expand the cursor and construct the DataFrame
    df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if '_id' in df:
        del df['_id']
    df.to_csv('person.csv', index=False)

    return send_file("person.csv", as_attachment=True)