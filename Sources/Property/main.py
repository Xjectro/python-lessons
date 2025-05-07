class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width}cm"

    @property
    def height(self):
        return f"{self._height}cm"

    @width.setter
    def width(self, new_value):
        if new_value > 0:
            self._width = new_value
        else:
            raise ValueError("Width must be positive")

    @height.setter
    def height(self, new_value):
        if new_value > 0:
            self._height = new_value
        else:
            raise ValueError("Height must be positive")

    @width.deleter
    def width(self):
        del self._width

    @height.deleter
    def height(self):
        del self._height


rectangle = Rectangle(5, 10)

rectangle.width = 10
rectangle.height = 20

del rectangle.width
del rectangle.height

print(rectangle.width)
print(rectangle.height)
