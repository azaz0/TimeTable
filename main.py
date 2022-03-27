from Departure import Departure
from Timetable import Timetable

print('Sprawdzanie o której godzinie odjeżdża autobus')
odjazd1 = Departure('Muchobór Wielki', '11:17')
odjazd2 = Departure('Muchobór Mały', '15:59')
odjazd3 = Departure('Jerozolimska', '7:07')
odjazd4 = Departure('Grunwaldzka', '8:21')
odjazd5 = Departure('Wrocławska', '12:21')
odjazd6 = Departure('Plac Słowiański', '15:51')

tablicaRozkladow = Timetable([odjazd1, odjazd2, odjazd3, odjazd4, odjazd5, odjazd6])
tablicaRozkladow.list_departures()
tablicaRozkladow.convertTimeToMinutes('11:17')