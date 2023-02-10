from spreadsheets.cell import Cell


class Spreadsheet:
    __LIMIT = 100

    def __init__(self, rows, columns):
        self.__rows = Spreadsheet.validate_dimension(rows)
        self.__columns = Spreadsheet.validate_dimension(columns)
        self.__cells = [[Cell() for x in range(self.__columns)] for xx in range(self.__rows)]

    def get_size(self):
        return self.__rows, self.__columns

    def get_cell_at(self, row, col):
        return self.__cells[row][col]

    def set_cell_at(self, row, col, value):
        if isinstance(value, Cell):
            self.__cells[row][col] = value
        elif isinstance(value, str):
            self.__cells[row][col].set_value(value)

    def add_row(self, row):
        row = self.__validate_row_index(row)
        empty_row = [Cell() for _ in range(self.__columns)]
        self.__cells.insert(row, empty_row)
        self.__rows += 1

    def remove_row(self, row):
        row = self.__validate_row_index(row)
        del self.__cells[row]
        self.__rows -= 1

    def add_column(self, col):
        col = self.__validate_column_index(col)
        for row in self.__cells:
            row.insert(col, Cell())
        self.__columns += 1

    def remove_column(self, col):
        col = self.__validate_column_index(col)
        for row in self.__cells:
            del row[col]
        self.__columns -= 1

    def swap_rows(self, row1, row2):
        row1 = self.__validate_row_index(row1)
        row2 = self.__validate_row_index(row2)

        self.__cells[row1], self.__cells[row2] = self.__cells[row2], self.__cells[row1]

    def swap_columns(self, col1, col2):
        col1 = self.__validate_row_index(col1)
        col2 = self.__validate_row_index(col2)
        for row in self.__cells:
            temp = row[col1]
            row[col1] = row[col2],
            row[col2] = temp

    def __validate_row_index(self, index):
        if index < 0 or index > self.__rows:
            raise IndexError(f"{index} is out of range of rows.")
        return index

    def __validate_column_index(self, index):
        if index < 0 or index > self.__columns:
            raise IndexError(f"{index} is out of range of columns.")
        return index

    @staticmethod
    def validate_dimension(dim):
        if dim < 0 or dim > Spreadsheet.__LIMIT:
            raise ValueError(f"Dimension can't be {dim}")
        return dim

    def __repr__(self):
        result = ""
        for row in self.__cells:
            result += "[ "
            for col in row:
                result += repr(col) + ",\t"
            result += " ],\n"
        return result
