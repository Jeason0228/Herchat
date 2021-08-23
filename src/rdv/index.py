from flask import Flask
from flask import render_template, redirect
from pymongo import MongoClient
from datetime import datetime, date

from wtforms.fields.core import SelectField
from save_info import *
import pandas as pd
from flask import send_file

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'
app.config['TEMPLATES_AUTO_RELOAD'] = True
Bootstrap(app)
SUBMITTED = False
SUBMITTED_DATE = None

mongo_client = MongoClient()

person_db = mongo_client.person_info
person_page= person_db.person

class NameForm(FlaskForm):
    domain = StringField('域名', validators=[DataRequired()])
    country = SelectField('国家', validators=[DataRequired()], choices=[("china", "China") ,("usa", "USA")])
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
                    x = threading.Thread(target=save_info, args=(domain, country))
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

@app.route("/run/<domain>/<country>/")
def run(domain, country):
    xl = []
    try:
        for i in range(4):
            x = threading.Thread(target=save_info, args=(domain, country))
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