from math import cos, sin


class Point(object):
    # idealy you want the cnstructor to be private, but it's impossible in python
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

    @staticmethod
    def new_cartesian_point(x: float, y: float):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho: float, theta: float):
        return Point(rho * cos(theta), rho * sin(theta))


def main():
    p = Point.new_cartesian_point(2, 3)
    print(p)
    p2 = Point.new_polar_point(1, 2)
    print(p2)


if __name__ == "__main__":
    main()
