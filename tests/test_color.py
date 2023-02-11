from spreadsheets.color import Color
from tests.test_base import TestBase


class TestColor(TestBase):

    @staticmethod
    def test_get_rgb():
        color = Color()

        TestBase.check("get_rgb", color.get_rgb() == (255, 255, 255))
    
    @staticmethod
    def test_set_rgb():
        color = Color()
        color.set_rgb(10, 20, 30)

        TestBase.check("set_rgb", color.get_rgb() == (10, 20, 30))

