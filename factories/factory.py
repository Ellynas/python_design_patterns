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
