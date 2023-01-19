"""
You are given a class called Square and a function calculate_area() which calculates the area of a given rectangle.

In order to use Square in calculate_area, instead of augmenting it with width/height members, please implement the SquareToRectangleAdapter class.
This adapter takes a square and adapts it in such a way that it can be used as an argument to calculate_area().
"""

import unittest


class Square:
    def __init__(self, side=0):
        self.side = side


def calculate_area(rc: "SquareToRectangleAdapter"):
    return rc.width * rc.height


class SquareToRectangleAdapter:
    def __init__(self, square):
        self.square: Square = square

    @property
    def width(self):
        return self.square.side

    @property
    def height(self):
        return self.square.side


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        sq = Square(11)
        adapter = SquareToRectangleAdapter(sq)
        self.assertEqual(121, calculate_area(adapter))
        sq.side = 10
        self.assertEqual(100, calculate_area(adapter))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
