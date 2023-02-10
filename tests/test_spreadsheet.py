from spreadsheets.cell import Cell
from spreadsheets.spreadsheet import Spreadsheet
from tests.test_base import TestBase


class TestSpreadsheet(TestBase):
    @staticmethod
    def test_get_size():
        sheet = Spreadsheet(3, 3)

        TestBase.check("get_size", sheet.get_size() == (3, 3))

    @staticmethod
    def test_get_cell_at():
        sheet = Spreadsheet(3, 3)
        cell = sheet.get_cell_at(0, 0)

        TestBase.check("get_cell_at", isinstance(cell, Cell))

    @staticmethod
    def test_set_cell_at():
        sheet = Spreadsheet(3, 3)
        cell = Cell("abc")
        sheet.set_cell_at(0, 0, cell)

        TestBase.check("set_cell_at", sheet.get_cell_at(0, 0) == cell)

    @staticmethod
    def test_add_row():
        sheet = Spreadsheet(3, 4)
        sheet.add_row(3)

        TestBase.check("add_row", sheet.get_size() == (4, 4))

    @staticmethod
    def test_remove_row():
        sheet = Spreadsheet(3, 4)
        sheet.remove_row(2)

        TestBase.check("remove_row", sheet.get_size() == (2, 4))

    @staticmethod
    def test_add_column():
        sheet = Spreadsheet(3, 3)
        sheet.add_column(3)

        TestBase.check("add_column", sheet.get_size() == (3, 4))

    @staticmethod
    def test_remove_column():
        sheet = Spreadsheet(3, 4)
        sheet.remove_column(3)

        TestBase.check("remove_column", sheet.get_size() == (3, 3))

    @staticmethod
    def test_swap_rows():
        sheet = Spreadsheet(3, 3)
        cell00 = sheet.get_cell_at(0, 0)
        sheet.swap_rows(0, 1)

        TestBase.check("swap_rows", sheet.get_cell_at(1, 0) == cell00)

    @staticmethod
    def test_swap_columns():
        sheet = Spreadsheet(3, 3)
        cell00 = sheet.get_cell_at(0, 0)
        sheet.swap_columns(0, 1)

        TestBase.check("swap_rows", sheet.get_cell_at(0, 1) == cell00)
    @staticmethod
    def run_all():
        TestSpreadsheet.test_get_size()
        TestSpreadsheet.test_get_cell_at()
        TestSpreadsheet.test_set_cell_at()
        TestSpreadsheet.test_add_row()
        TestSpreadsheet.test_remove_row()
        TestSpreadsheet.test_add_column()
        TestSpreadsheet.test_remove_column()
        TestSpreadsheet.test_swap_rows()
        TestSpreadsheet.test_swap_columns()
