class Passenger:
    # 0 - none
    # 1 - children under 4 - 100%
    # 2 - students - 50%
    # 3 - weterans - 90%
    # 3 - handicapped - 98%
    CONST_NONE = 0
    CONST_CHILDREN = 1
    CONST_STUDENTS = 2
    CONST_WETERANS = 3
    CONST_HANDICAPPED = 4

    relief = None

    def __init__(self, relief: int):
        self.set_relief(relief)

    def get_relief(self):
        return self.relief

    def set_relief(self, relief: int):
        if (relief == self.CONST_NONE):
            self.relief = 0
        if (relief == self.CONST_CHILDREN):
            self.relief = 100
        if (relief == self.CONST_STUDENTS):
            self.relief = 50
        if (relief == self.CONST_WETERANS):
            self.relief = 90
        if (relief == self.CONST_HANDICAPPED):
            self.relief = 98
        else:
            print('There is no such relief with given number, please try again.')

    def get_const_none(self):
        return self.CONST_NONE

    def get_const_children(self):
        return self.CONST_CHILDREN

    def get_const_students(self):
        return self.CONST_STUDENTS

    def get_const_weterans(self):
        return self.CONST_WETERANS

    def get_const_handicapped(self):
        return self.CONST_HANDICAPPED
