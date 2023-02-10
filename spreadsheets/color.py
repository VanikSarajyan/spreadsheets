class Color:

    def __init__(self, red=255, green=255, blue=255):
        self.__red = red
        self.__green = green
        self.__blue = blue

    def get_rgb(self):
        return self.__red, self.__green, self.__blue

    def set_rgb(self, red, green, blue):
        self.__red = Color.validate_color_component(red)
        self.__green = Color.validate_color_component(green)
        self.__blue = Color.validate_color_component(blue)

    def __eq__(self, other):
        if isinstance(other, tuple):
            return self.get_rgb() == other
        if isinstance(other, Color):
            return self.get_rgb() == other.get_rgb()
        else:
            return False

    @staticmethod
    def validate_color_component(component):
        component = int(component)
        if component > 255:
            component = 255
        elif component < 0:
            component = 0

        return component

    def __repr__(self):
        return f"[Class {self.__class__.__name__} ({self.__red:<3},{self.__green:<3},{self.__blue:<3})]"
