"""This is my covid tracker app"""
from flask import Flask
from flask import render_template, request
import urllib.request, json
import urllib.parse

APP = Flask(__name__)

@APP.route("/")
def layout(name=None):
    """This is my root page"""
    return render_template('layout.html', name=name)

@APP.route("/result", methods=['GET', 'POST'])
def result():
    """This is my results page"""
    state = request.form['state']
    county = request.form['county']
    sex = request.form['sex']
    age = request.form['age']
    modified_age = urllib.parse.quote(request.form['age'])
    race = request.form['race']

   
    
    url = "https://data.cdc.gov/resource/n8mc-b4w4.json?res_state="+ state + "&res_county=" + county + "&sex=" + sex + "&race=" + race  + "&age_group=" + modified_age 

    response = urllib.request.urlopen(url)

    data = response.read()

    dict1 = json.loads(data)
    case_count = len(dict1)
    #return render_template('result.html', cdc=dict1["results"])
    return render_template('result.html', case_count=case_count, state=state, county=county, sex=sex, age=age, race=race, dict1=dict1)

