#!/usr/bin/env python
from flask import Flask
from flask import render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

#mongo
app.config["MONGO_URI"] = "mongodb://192.168.137.128:27017/temperature"
mongo = PyMongo(app)

# Defining routes to return correct views. 
@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')
# Defines view for route /get_one_temp_api
# Function will return one temp reading from the DB as a JSON object in the browser.
@app.route("/get_one_temp_api")
def temp1():
    one_temp = mongo.db.temperature.find_one()
    #print(temp_reading)
    return str(one_temp)

# Defines view for route /get_ten_temps_api
# Function will return ten temps from the DB as JSON objects in the browser.
@app.route("/get_ten_temps_api")
def temp10():
    temps = ""
    ten_temps = mongo.db.temperature.find().limit(10)
    for temp in ten_temps:
        temps=temps+str(temp)
        print(temps)
    return temps

# Defines view for route /recent_temps
# Function will return the HTML view from temps.html.
@app.route("/recent_temps")
def recent():
    temps = mongo.db.temperature.find().limit(10)
    
    return render_template('temps.html',temps=temps)

# Runs the app and allows all connections
if __name__ == '__main__':
    app.run(host='0.0.0.0')     # open for everyonepy