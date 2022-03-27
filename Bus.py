class Bus:
    busLine = None

    def __init__(self, busLine):
        self.busLine = busLine

    def get_busLine(self):
        return self.busLine

    def set_busLine(self, busLine):
        self.busLine = busLine
