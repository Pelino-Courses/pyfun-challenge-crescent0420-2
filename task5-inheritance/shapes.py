from math import pi


class Shape:
    """
    Base class for geometric shapes.

    Methods:
        area(): Returns the area of the shape (default: NotImplementedError).
        perimeter(): Returns the perimeter of the shape (default: NotImplementedError).
    """

    def area(self):
        raise NotImplementedError("Subclasses must implement area().")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter().")

    def __str__(self):
        return f"{self.__class__.__name__}()"


class Circle(Shape):
    """
    Circle shape class.

    Parameters:
        radius (float): Radius of the circle (must be positive).

    Methods:
        area(): Returns the area of the circle.
        perimeter(): Returns the circumference of the circle.
    """

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    """
    Rectangle shape class.

    Parameters:
        width (float): Width of the rectangle (must be positive).
        height (float): Height of the rectangle (must be positive).

    Methods:
        area(): Returns the area.
        perimeter(): Returns the perimeter.
        square(): Class method to create a square.
    """

    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    @classmethod
    def square(cls, side):
        """Create a square (special case of a rectangle)."""
        return cls(side, side)


class Triangle(Shape):
    """
    Triangle shape class (only for right-angled triangles or with known base/height).

    Parameters:
        base (float): Base of the triangle (must be positive).
        height (float): Height of the triangle (must be positive).

    Methods:
        area(): Returns the area.
        perimeter(): Not implemented by default (use subclass if needed).
    """

    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        raise NotImplementedError("Perimeter calculation not supported for base/height triangle.")

    def __str__(self):
        return f"Triangle(base={self.base}, height={self.height})"
