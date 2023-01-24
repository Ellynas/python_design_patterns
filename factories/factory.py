"""
Factories
 - A component responsible solely for the wholesale (not piecewise)
   creation of objects
Motivation
 - Object creation logic becomes too convoluted
 - Initializer is not descriptive
   - Name is always __init__
   - Cannot overload with same sets of arguments with
     different names
   - Can turn into 'optional parameter hell'
 - Wholesale object creation (non-piecewise, unlike Builder)
   can be outsourced to
   - A separate method (Factory Method)
   - That may exist in a separate clas (Factory)
   - Can create a hiearchy of factories of Abstract Factory
"""

from math import cos, sin


class Point(object):
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    class PointFactory(object):
        @staticmethod
        def cartesian_point(x: float, y: float):
            return Point(x, y)

        @staticmethod
        def polar_point(rho: float, theta: float):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory


def main():
    p = Point.factory.cartesian_point(2, 3)
    print(p)
    p2 = Point.factory.polar_point(1, 2)
    print(p2)


if __name__ == "__main__":
    main()
