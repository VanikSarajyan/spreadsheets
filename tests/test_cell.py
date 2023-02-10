from spreadsheets.cell import Cell
from spreadsheets.color import Color
from tests.test_base import TestBase
from datetime import datetime


class TestCell(TestBase):
    @staticmethod
    def test_get_value():
        cell = Cell()

        TestBase.check('get_value', cell.get_value() == "")

    @staticmethod
    def test_set_value():
        cell = Cell()

        cell.set_value("abc")
        TestBase.check('set_value', cell.get_value() == "abc")

    @staticmethod
    def test_get_color():
        cell = Cell()

        TestBase.check("get_color", cell.get_color() == (255, 255, 255))

    @staticmethod
    def test_set_color():
        cell = Cell()
        color = Color()

        cell.set_color(color)
        TestBase.check("set_color", cell.get_color() == (255, 255, 255))

    @staticmethod
    def test_to_int():
        cell = Cell("5")

        TestBase.check("to_int", cell.to_int() == 5)

    @staticmethod
    def test_to_double():
        cell = Cell("5.5")

        TestBase.check("to_int", cell.to_double() == 5.5)

    @staticmethod
    def test_to_date():
        cell = Cell("09/19/22 13:55:26")
        date = datetime.strptime("09/19/22 13:55:26", '%m/%d/%y %H:%M:%S')

        TestBase.check("to_date", cell.to_date() == date)

    @staticmethod
    def test_reset():
        cell = Cell("abc")
        cell.reset()

        TestBase.check("reset", cell.get_value() == "")
    @staticmethod
    def run_all():
        TestCell.test_get_value()
        TestCell.test_set_value()
        TestCell.test_get_color()
        TestCell.test_set_color()
        TestCell.test_to_int()
        TestCell.test_to_double()
        TestCell.test_to_date()
        TestCell.test_reset()
