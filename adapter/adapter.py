# adapter l'interface X pour se conformer aux requis de l'interface Y


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y


def draw_point(p):
    print(".", end="")


# ^^ you are given this

# vv You have this 


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


class LineToPointAdapter(list):
    def __init__(self, line: Line):
        super().__init__()
        print(f"Generating points for line [{line.start.x}, {line.start.y}][{line.end.x}, {line.end.y}]")

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.x)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw(rcs):
    print("\n\n--- Drawring some stuff ---\n")
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
    print()


def main():
    RS = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
    draw(RS)


if __name__ == "__main__":
    main()
