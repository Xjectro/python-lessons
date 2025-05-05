import math


class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(
            f"This shape is {self.color} and {'filled' if self.is_filled else 'not filled'}."
        )


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"This circle has an area of {math.pi * self.radius * self.radius}.")


class Square(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"This square has an area of {self.width * self.height}.")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"This square has an area of {self.width * self.height}.")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"This triangle has an area of {0.5 * self.width * self.height}.")


circle = Circle(color="red", is_filled=True, radius=5)
square = Square(color="blue", is_filled=False, width=4, height=4)
triangle = Triangle(color="green", is_filled=True, width=3, height=4)

circle.describe()
square.describe()
triangle.describe()
