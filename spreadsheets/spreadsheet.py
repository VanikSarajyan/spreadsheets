from spreadsheets.cell import Cell


class Spreadsheet:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__cells = []

    def get_size(self):
        pass
    def get_cell_at(self, row, col):
        pass

    def set_cell_at(self, row, col, value):
        pass

    def add_row(self, row):
        pass

    def remove_row(self, row):
        pass

    def add_column(self, col):
        pass

    def remove_column(self, col):
        pass

    def swap_rows(self, row1, row2):
        pass

    def swap_columns(self, col1, col2):
        pass
