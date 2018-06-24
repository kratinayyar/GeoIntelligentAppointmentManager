class Store(object):

    def __init__(self, location,  numSeats, numServers, avgServiceTime, autoCheckInR, saveSpotR, businessClosingTime):
        #constructor
        self.location = location
        self.numSeats = numSeats
        self.numServers = numServers
        self.averageServiceTime = avgServiceTime
        self.autoCheckInR = autoCheckInR
        self.saveSpotR = saveSpotR
        self.businessClosingTime = businessClosingTime

    # def getSeats(self):
    #     pass