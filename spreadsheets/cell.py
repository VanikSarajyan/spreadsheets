from spreadsheets.color import Color


class Cell:

    def __init__(self, value="", color=Color()):
        self.__value = value
        self.__color = color

    def get_value(self):
        return ""

    def set_value(self, value):
        pass

    def get_color(self):
        pass

    def set_color(self, color):
        pass

    def to_int(self):
        return 0

    def to_double(self):
        return 0.0

    def to_date(self):
        pass

    def reset(self):
        pass
