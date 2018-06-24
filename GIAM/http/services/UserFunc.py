import http as h
from http.models.Users import Users


def user(userDict):
    name = userDict["name"]
    location = userDict["location"]
    actualAppTime = h.nextAppTime
    currentLocation = location
    # add pitney bowes api for estmating time from current location
    estimateReachTime = ""
    user = Users(name, location, actualAppTime, currentLocation, estimateReachTime, False)
    h.appList[name]= user



def getStatus(name):
    user = h.appList[name]
    # get current location pitney bowes api

    # get time to reach storeLocation

    return