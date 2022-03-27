from Departure import Departure
from Passenger import Passenger
from Ticket import Ticket
from Timetable import Timetable

print('Sprawdzanie o której godzinie odjeżdża autobus')
odjazd1 = Departure('Muchobór Wielki', '11:17')
odjazd2 = Departure('Muchobór Mały', '15:59')
odjazd3 = Departure('Jerozolimska', '7:07')
odjazd4 = Departure('Grunwaldzka', '8:21')
odjazd5 = Departure('Wrocławska', '12:21')
odjazd6 = Departure('Plac Słowiański', '15:51')
dziecko = Passenger(Passenger.CONST_CHILDREN)
student = Passenger(Passenger.CONST_STUDENTS)
weteran = Passenger(Passenger.CONST_WETERANS)
biletDziecka = Ticket(dziecko.get_relief())
biletStudenta = Ticket(student.get_relief())
biletWeterana = Ticket(weteran.get_relief())

tablicaRozkladow = Timetable([odjazd1, odjazd2, odjazd3, odjazd4, odjazd5, odjazd6])
tablicaRozkladow.list_departures()

print("Godzina Odjazdu Grunwaldzka: ", tablicaRozkladow.get_departure_by_value(odjazd4).get_busDepartureTime())
print("Cena biletu dla dziecka: ", biletDziecka.get_ticketPrice())
print("Cena biletu dla studenta: ", biletStudenta.get_ticketPrice())
