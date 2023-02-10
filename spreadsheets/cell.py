from spreadsheets.color import Color


class Cell:

    def __init__(self, value="", color=Color()):
        self.__value = value
        self.__color = color

    def get_value(self):
        pass

    def set_value(self, value):
        pass

    def get_color(self):
        pass

    def set_color(self, color):
        pass

    def to_int(self):
        pass

    def to_double(self):
        pass

    def to_date(self):
        pass

    def reset(self):
        pass

    def __eq__(self, other):
        if isinstance(other, str):
            return self.__value == other
        if isinstance(other, Cell):
            return self.__value == other.__value and self.__color == other.__color

