from lab3.lab_python_oop.figure import Rectangle, Circle, Square


def main():
    rect = Rectangle(2, 3, 'blue')
    circle = Circle(5, 'green')
    square = Square(5, 'red')
    print(rect)
    print(circle)
    print(square)


if __name__ == '__main__':
    main()
