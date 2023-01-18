"""
Composite
- A mechanism for treating individual (scalar) objects and composition of
  objects in a uniform matter

Motivation
- Objects use others' properties/members through inheritance and composition
- Composition lets us make compound objects
  - E.g., a mathematical expression composed of simple expressions; or
  - A grouping of shapes that consists of several shapes
- Composite design pattern is used to treat both single (scalar) and composite
  objects uniformly
  - I.e., Foo and Sequence (yielding Foo's) have common APIs
"""

from typing import List


class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children: List[GraphicObject] = []
        self._name = "Group"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def _print(self, items: list, depth):
        items.append("*" * depth)
        if self.color:
            items.append(self.color)
        items.append(f"{self.name}\n")
        for child in self.children:
            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return "".join(items)


class Circle(GraphicObject):
    @property
    def name(self):
        return "Circle"


class Square(GraphicObject):
    @property
    def name(self):
        return "Square"


def main():
    DRAWING = GraphicObject()
    DRAWING.name = "My Drawing"
    DRAWING.children.append(Square("Red"))
    DRAWING.children.append(Circle("Yellow"))

    GROUP = GraphicObject()
    GROUP.children.append(Circle("Blue"))
    GROUP.children.append(Square("Blue"))
    DRAWING.children.append(GROUP)

    print(DRAWING)


if __name__ == "__main__":
    main()
