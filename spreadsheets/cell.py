from spreadsheets.color import Color
from datetime import datetime as dt


class Cell:

    def __init__(self, value="", color=Color()):
        self.__value = value
        self.__color = color

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = str(value)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        if isinstance(color, Color):
            self.__color = color
        else:
            raise ValueError(f"Can't assign {color} to Cell color.")

    def to_int(self):
        return int(self.__value)

    def to_double(self):
        return float(self.__value)

    def to_date(self):
        return dt.strptime(self.__value, '%m/%d/%y %H:%M:%S')

    def reset(self):
        self.__value = ""
        self.__color = Color()

    def __eq__(self, other):
        if isinstance(other, str):
            return self.__value == other
        if isinstance(other, Cell):
            return self.__value == other.__value and self.__color == other.__color
        else:
            return False

    def __repr__(self):
        return f"[Class {self.__class__.__name__ } value: {self.__value:<10}, color: {self.__color}]"
