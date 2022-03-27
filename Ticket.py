class Ticket:
    ticketPrice=9.99

    def __init__(self, Passenger):
        self.ticketPrice=self.ticketPrice-(self.ticketPrice*(Passenger.get_relief()/100))

    def get_ticketPrice(self):
        return self.ticketPrice