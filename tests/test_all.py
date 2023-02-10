from tests.test_color import TestColor
from tests.test_cell import TestCell
from tests.test_spreadsheet import TestSpreadsheet

for test in (TestColor, TestCell, TestSpreadsheet):
    print(f"Running tests of {test.__name__}")
    test.run_all()
