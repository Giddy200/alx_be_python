import math

class Shape:
    """
    Base class for geometric shapes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        Raises NotImplementedError to ensure derived classes override this method.
        """
        raise NotImplementedError("Subclass must implement abstract method")

class Rectangle(Shape):
    """
    A class to represent a rectangle, derived from Shape.
    """
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of a rectangle.
        """
        return self.length * self.width

class Circle(Shape):
    """
    A class to represent a circle, derived from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of a circle.
        """
        return math.pi * self.radius ** 2