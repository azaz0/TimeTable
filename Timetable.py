import datetime as DT


class Timetable:
    departures = []
    frequency = None

    # departure: object || departure: list of objects
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

    def get_departure_by_value(self, Departure):
        for departure in self.departures:
            if (departure.get_stopName() == Departure.get_stopName()):
                return departure

    def add_departure(self, Departure: object):
        self.departures = self.departures.append(Departure)

    def add_departures(self, departures):
        self.departures = self.departures.extend(departures)

    def remove_departure(self, Departure: object):
        self.departures.remove(Departure)

    def convertTimeToMinutes(self, time):
        t1 = DT.datetime.strptime(time, '%H:%M')
        t2 = DT.datetime(1900, 1, 1)
        return ((t1 - t2).total_seconds() / 60)

    # Funkcja na częstotliwość:
    # dla wszystkich odjazdów - sortuje tabele od odjazdów o najmniejszym czasie do największego
    # aby posortować obiekty trzeba for departure in self.departures następnie wybrać element 'i' oraz 'i+', porównać i jeśli dany jest i+ o mniejszej wartości przesunąć w lewo
    # pobiera czas z indeksem 'i' oraz 'i+'
    # przelicza je na minuty
    # odejmuje od większego mniejszy
    # zbiera wynik do tabeli wyników
    # dodaje wszystkie do siebie
    # dzieli przez ilość indexów w tablicy
    # zwraca średni czas
    # def countDeparturesFrequency(self):

    # def countDeparturesFrequency(self):
    #     dayDeparturesTime=0
    #
    #     for departure in self.departures:
    #         dayDeparturesTime -= self.convertTimeToMinutes(departure.get_busDepartureTime())
    #
    #     self.frequency = dayDeparturesTime / len(self.departures)

    def get_frequency(self):
        return self.frequency
