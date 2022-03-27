import datetime as DT


class Timetable:
    departures = []

    #departure: object || departure: list of objects
    def __init__(self, departure):
        self.departures.extend(departure)

    def get_departures(self):
        return self.departures

    def list_departures(self):
        for departure in self.departures:
            print("Nazwa przystanku: ", departure.get_stopName(), " Godzina odjazdu: ",
                  departure.get_busDepartureTime())

    def show_departure(self, index):
        print("Departure no. ", index)
        print(self.departures[index])

    def add_departure(self, Departure: object):
        self.departures = self.departures.append(Departure)

    def add_departures(self, departures):
        self.departures = self.departures.extend(departures)

    def remove_departure(self, Departure: object):
        self.departures.remove(Departure)

    def convertTimeToMinutes(self, time):
        t1 = DT.datetime.strptime(time, '%H:%M')
        t2 = DT.datetime(1900, 1, 1)
        print((t1-t2).total_seconds()/60)
