class Departure:
    stopName = None
    busDepartureTime = None

    def __init__(self, stopName, busDepartureTime):
        self.stopName = stopName
        self.busDepartureTime = busDepartureTime

    def get_stopName(self):
        return self.stopName

    def set_stopName(self, stopName):
        self.stopName = stopName

    def get_busDepartureTime(self):
        return self.busDepartureTime

    def set_busDepartureTime(self, busDepartureTime):
        self.busDepartureTime = busDepartureTime
