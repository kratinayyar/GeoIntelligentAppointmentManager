class Users(object):

    def __init__(self, name, location, actualAppTime, currentLocation, estimateReachTime, autoCheckIn):
        self.name = name
        self.location = location
        self.actualAppTime = actualAppTime
        self.currentStatus = ""
        self.currentLocation = currentLocation
        self.estimateReachTime = estimateReachTime
        self.autoCheckIn = autoCheckIn