"""
Bridge
- A mechanism that decouples an interface (hierarchy) from an implementation
  (hierarchy)
Motivation
- Prevents a 'Cartesian product' complexity explosion
"""

from abc import ABC


class Renderer(ABC):
    def render_circle(self, radius):
        pass

    def render_square(self, lenght):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle of radius {radius}")

    def render_square(self, lenght):
        print(f"Drawing a square of lenght {lenght}")


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")

    def render_square(self, lenght):
        print(f"Drawing pixels of a square of lenght {lenght}")


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer: Renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        # bridge
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


class Square(Shape):
    def __init__(self, renderer, lenght):
        super().__init__(renderer)
        self.lenght = lenght

    def draw(self):
        self.renderer.render_square(self.lenght)

    def resize(self, factor):
        self.lenght *= factor


def main():
    RASTER = RasterRenderer()
    VECTOR = VectorRenderer()
    CIRCLE = Circle(VECTOR, 5)
    CIRCLE.draw()
    CIRCLE.resize(2)
    CIRCLE.draw()
    CIRCLE = Circle(RASTER, 5)
    CIRCLE.draw()
    CIRCLE.resize(2)
    CIRCLE.draw()

    SQUARE = Square(VECTOR, 5)
    SQUARE.draw()
    SQUARE.resize(2)
    SQUARE.draw()
    SQUARE = Square(RASTER, 5)
    SQUARE.draw()
    SQUARE.resize(2)
    SQUARE.draw()


if __name__ == "__main__":
    main()
