from flask import Flask, url_for
from flask import jsonify
import json
from flask import request
import http.services.StoreFunc as storeFuncs
import http as h
from http.services.UserFunc import user, getStatus

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'

@app.route("/store", methods =["POST"])
def postStore():
    print request.data
    print type(request.data)
    data = json.loads(request.data)
    print data['name']
    h.storeName = data["name"]
    h.storeLocation = data["location"]
    h.numSeats = data["numSeats"]
    h.numServers = data["numServers"]
    h.averageServiceTime = data["avgServiceTime"]
    h.autoCheckInR = data["autoCheckInR"]
    h.saveSpotR = data["saveSpotR"]
    h.storeClosingTime = data["storeClosingTime"]
    h.nextAppTime = data["storeOpeningTime"]
    h.storeOpeningTime =  data["storeOpeningTime"]
    return jsonify({})

@app.route("/store")
def getStore():
    return jsonify({"Store Name": h.storeName, "Store Location": h.storeLocation, "Number of Seats": h.numSeats, "Number of Servers": h.numServers,
                                  "Average Service Time": h.averageServiceTime, "Auto CheckIn Radius": h.autoCheckInR, "Save Spot radius": h.saveSpotR, "Closing Time": h.storeClosingTime})


@app.route("/user", methods =["POST"])
def postUser():
    data = json.loads(request.data)
    user(data)
    return("Saved your name in the appointment queue")

def getUserStatus(name):
    getStatus(name)
    return ""

app.run()


#
# @app.route('/login')
# def login():
#     return 'login'
#
#
# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(username)
#
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
