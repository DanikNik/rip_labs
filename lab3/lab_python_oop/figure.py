from abc import ABC, abstractmethod
from math import pi

from lab3.lab_python_oop.color import Color


class Figure(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Figure):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width

        self.color = Color()
        self.color.set_color(color)

        self.figure_name = "Rectangle"

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f'<{self.figure_name}, w:{self.width}, h:{self.height}, c: {self.color.get_color()}, a: {self.area()}>'


class Circle(Figure):
    def __init__(self, rad, color):
        self.rad = rad

        self.color = Color()
        self.color.set_color(color)

        self.figure_name = "Circle"

    def area(self):
        return pi * self.rad ** 2

    def __repr__(self):
        return f'<{self.figure_name}, r: {self.rad}, c: {self.color.get_color()}, a: {self.area()}>'


class Square(Rectangle):
    def __init__(self, a, color):
        super().__init__(a, a, color)

        self.figure_name = "Square"

    def __repr__(self):
        return f'<{self.figure_name}, s: {self.width}, c: {self.color.get_color()}, a: {self.area()}>'
