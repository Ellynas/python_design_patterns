"""
Given the definitions shown in code, you are asked to implement Line.deep_copy() to perform a deep copy of the given Line  object. This method should return a copy of a Line that contains copies of its start/end points.

Note: please do not confuse deep_copy() with __deepcopy__()!
"""


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, start=Point(), end=Point()):
        self.start = start
        self.end = end

    def deep_copy(self):
        return Line(Point(self.start.x, self.start.y), Point(self.end.x, self.end.y))


def main():
    pass


if __name__ == "__main__":
    main()
