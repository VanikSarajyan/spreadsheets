from tests.test_color import TestColor
from tests.test_cell import TestCell

for test in (TestColor, TestCell):
    print(f"Running tests of {test.__name__}")
    test.run_all()
