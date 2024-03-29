from flask import Flask
from flask import render_template, redirect, request
from pymongo import MongoClient
from datetime import datetime, date
from flask import jsonify
from multiprocessing import Pool

import os
import json
from wtforms.fields.core import SelectField
from libs.save_info import *
from libs.excel_parse import *
from libs.user_dao import *
from libs.sms_receive import *
# from libs.detect import *
import pandas as pd
from flask import send_file

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
# Flask-WTF requires an encryption key - the string can be anything


# MONGO_URI = "mongodb://127.0.0.1"
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)
SUBMITTED = False
SUBMITTED_DATE = None


class NameForm(FlaskForm):
    domain = StringField('域名', validators=[DataRequired()])
    country = SelectField('国家', validators=[DataRequired()], choices=[
                          ("china", "China"), ("usa", "USA")])
    submit = SubmitField('Submit')


@app.route("/", methods=['GET', 'POST'])
def hello():
    global SUBMITTED_DATE, SUBMITTED, TOTAL_COUNT
    form = NameForm()
    message = ""
    if SUBMITTED_DATE is not None and date.today() > SUBMITTED_DATE:
        SUBMITTED = False
        TOTAL_COUNT = 0

    if form.validate_on_submit():
        if not SUBMITTED:
            domain = form.domain.data
            country = form.country.data
            # empty the form field
            form.domain.data = ""
            form.country.data = ""
            xl = []
            try:
                for i in range(4):
                    x = threading.Thread(
                        target=save_info, args=(domain, country))
                    x.start()
                    xl.append(x)

                SUBMITTED = True
                SUBMITTED_DATE = date.today()
            except:
                print("Error: unable to start thread")
                TOTAL_COUNT = 0
            return "running..."
        else:
            return "already submitted.."

    return render_template("index.html", form=form)


@app.route("/run/<domain>/<country>/<number>/")
def run(domain, country, number):
    xl = []
    try:
        for i in range(4):
            x = threading.Thread(
                target=save_info, args=(domain, country, number))
            x.start()
            xl.append(x)

        for x in xl:
            x.join()
        TOTAL_COUNT = 0

    except:
        print("Error: unable to start thread")
        TOTAL_COUNT = 0
    return "runing..."


@app.route("/count")
def count():
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    all_count = rdv_page.find({"date": {"$lt": end, "$gte": start}}).count()
    failed_count = len(get_all_failed(rdv_page))
    code_sent = len(get_all_successed(rdv_page))
    return str(date.today()) + f" 总数：{all_count}, 失败: {failed_count}, 成功: {code_sent}"


@app.route("/send/<sim_line>/")
def send(sim_line):
    all_user = get_all_user_by_line(person_page, sim_line)
    # _div = [all_user[i:i+4] for i in range(0, len(all_user), 4)]
    count = 0
    for p in all_user:
        count += send_request(p)
    fialed = len(all_user) - count
    # for sub_list in _div:
    #     _slept = randrange(50)
    #     sleep(_slept)
    #     # print(len(sub_list))
    #     with Pool(4) as p:
    #         p.map(send_request, sub_list)
    # with Pool(16) as p:
    #     p.map(send_request, all_user)
    # x.start()
    # x.join()
    # send_request(person_db, all_user)
    return f"sim line {sim_line} sent, {fialed} failed."

@app.route("/resend/<sim_line>/")
def resend(sim_line):
    all_user = get_all_failed_by_line(person_page, sim_line)
    # _div = [all_user[i:i+4] for i in range(0, len(all_user), 4)]
    count = 0
    for p in all_user:
        count += send_request(p)
    fialed = len(all_user) - count
    return f"sim line {sim_line} sent, {fialed} failed."

@app.route("/update")
def update():
    all_user = get_all_users(person_page)
    _div = [all_user[i:i+16] for i in range(0, len(all_user), 16)]
    for i, sub_list in enumerate(_div):
        # _slept = randrange(50)
        # sleep(_slept)
        # print(len(sub_list))
        print(i + 1)
        for p in sub_list:
            p["sim_line"] = i + 1
            person_page.replace_one({"_id":p["_id"]}, p,upsert=True)
    # with Pool(16) as p:
    #     p.map(send_request, all_user)
    # x.start()
    # x.join()
    # send_request(person_db, all_user)
    return "running..."



# @app.route("/resend")
# def resend():
#     all_user = get_all_failed(rdv_page)
    
#     _div = [all_user[i:i+16] for i in range(0, len(all_user), 16)]
#     # print(len(_div))
#     for sub_list in _div:
#         _slept = randrange(50)
#         sleep(_slept)
#         # print(len(sub_list))
#         with Pool(16) as p:
#             p.map(resend_request, sub_list)
#     # print(len(all_user))
#     # resend_request(all_user[0], rdv_page)
#     # with Pool(1) as p:
#     #     p.map(resend_request, all_user)
#     # x.start()
#     # x.join()
#     # send_request(person_db, all_user)
#     return "resending..."

@app.route("/detect")
def detect():
    all_rdv = get_all_successed(rdv_page)
    # rdv_object = rdv_page.find_one({"rdv_list": {"$elemMatch": {"phone_number": "33769142022"}}})
    # send_sms(rdv_page, "33758145465")
    for p in all_rdv:

        url = p["url"].replace("/register/", "/")
        print(url)
        detect_ok(url, p)
        # sleep(100)
    # print(rdv_object)
    return "dict(rdv_object)"


@app.route("/test")
def test():
    # rdv_object = rdv_page.find_one({"rdv_list": {"$elemMatch": {"phone_number": "33769142022"}}})
    send_sms(rdv_page, "33758145465")
    # print(rdv_object)
    return "dict(rdv_object)"


@app.route("/sms_input/<telephone_num>/<sms_text>/<date>/<sms_port>/", methods=['GET'])
def sms_input(telephone_num, sms_text, date, sms_port):
    print(telephone_num, sms_text, date, sms_port)
    save_sms_code(rdv_page, telephone_num, sms_text, sms_port, date)
    send_sms(rdv_page, telephone_num)
    resp = jsonify(success=True)
    return resp


@app.route("/upload", methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # print(request.files['file'])
        f = request.files['file']
        f.save(os.path.join("./assects/uploads", f.filename))
        people_list, data_file = parse_excel(f)
        insert_user(db_page=person_page, person_list=people_list)
        return data_file.to_html()
    return '''
    <!doctype html>
    <title>Upload an excel file</title>
    <h1>Excel file upload (csv, tsv, csvz, tsvz only)</h1>
    <form action="" method=post enctype=multipart/form-data>
    <p><input type=file name=file><input type=submit value=Upload>
    </form>
    '''


@app.route("/csv")
def csv():
    start = datetime.combine(date.today(), datetime.min.time())
    end = datetime.combine(date.today(), datetime.max.time())
    # Make a query to the specific DB and Collection
    cursor = rdv_page.find({"date": {"$lt": end, "$gte": start}, "status":True, "code_sent":True})

    # Expand the cursor and construct the DataFrame
    df = pd.DataFrame(list(cursor))

    # Delete the _id
    if '_id' in df:
        del df['_id']
    df.to_csv('person.csv', index=False)

    return send_file("person.csv", as_attachment=True)
