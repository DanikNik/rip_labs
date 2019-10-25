class Color:
    def __init__(self):
        self._color = None

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color

    def del_color(self):
        del self._color

    color = property(get_color, set_color, del_color, "Color property")