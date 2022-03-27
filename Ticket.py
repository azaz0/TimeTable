import Passenger


class Ticket(Passenger.Passenger):
    ticketPrice = 9.99

    def __init__(self, relief: int):
        super().__init__(relief)
        self.ticketPrice = self.ticketPrice - (self.ticketPrice * (relief / 100))

    def get_ticketPrice(self):
        return self.ticketPrice
