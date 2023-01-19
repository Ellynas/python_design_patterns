"""
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape  a constructor that takes an interface Renderer  defined as

    class Renderer(ABC):
        @property
        def what_to_render_as(self):
            return None

as well as VectorRenderer and RasterRenderer classes. Each inheritor of the Shape  abstract class should have a constructor that takes a Renderer such that, subsequently, each constructed object's __str__()  operates correctly, for example,

str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels"
"""

from abc import ABC


class Renderer(ABC):
    @property
    def square_to_render_as(self) -> str:
        return ""

    @property
    def triangle_to_render_as(self) -> str:
        return ""


class VectorRenderer(Renderer):
    @property
    def square_to_render_as(self) -> str:
        return "Drawing Square as vectors"

    @property
    def triangle_to_render_as(self) -> str:
        return "Drawing Triangle as vectors"


class RasterRenderer(Renderer):
    @property
    def square_to_render_as(self) -> str:
        return "Drawing Square as pixels"

    @property
    def triangle_to_render_as(self) -> str:
        return "Drawing Triangle as pixels"


class Shape(ABC):
    def __init__(self, renderer):
        self.renderer: Renderer = renderer
        self.name = None

    def __str__(self) -> str:
        return ""


class Triangle(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Triangle"

    def __str__(self) -> str:
        return self.renderer.triangle_to_render_as


class Square(Shape):
    def __init__(self, renderer):
        super().__init__(renderer)
        self.name = "Square"

    def __str__(self) -> str:
        return self.renderer.square_to_render_as


def main():
    print(Triangle(RasterRenderer()))
    print(Square(RasterRenderer()))
    print(Triangle(VectorRenderer()))
    print(Square(VectorRenderer()))


if __name__ == "__main__":
    main()
