import math

class Rectangle:
    """
    A rectangle shape defined by width and height.

    Attributes:
        width (int): how wide the rectangle is
        height (int): how tall the rectangle is
    """

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        """
        Compute the area of this rectangle.

        Returns:
            int: the area (width * height)
        """
        return self.width * self.height

    def describe(self) -> None:
        """
        Print a description of the rectangle.

        Returns:
            None
        """
        print(f"Rectangle {self.width} by {self.height} has area {self.area()}")


# TODO: Add Circle class
# - Attributes: radius (float|int)
# - Methods: area() -> float, describe() -> None
# - Docstrings should clearly document parameters and return types
class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def describe(self) -> None:
        print(f"Circle with radius {self.radius} has area {self.area()}")

# TODO: Add Triangle class
# - Attributes: base (float|int), height (float|int)
# - Methods: area() -> float, describe() -> None
# - Docstrings should clearly document parameters and return types

class Triangle:
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

    def describe(self) -> None:
        print(f"Triangle with base {self.base} and height {self.height} has area {self.area()}")

# TODO: Add helper function: cm2_to_m2(value_cm2: float) -> float

def cm2_to_m2(value_cm2: float) -> float:
    return value_cm2 / 10000