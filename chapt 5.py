# Chapter 5: Classes and Object-Oriented Python

class Rectangle:
    """Represents a rectangle shape."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

rect = Rectangle(3, 4)
print(rect.area())  # 12
print(rect.perimeter())  # 14