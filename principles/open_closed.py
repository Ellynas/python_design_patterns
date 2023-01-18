"""
Open-closed principle
- Classes should be open for extension but closed for
  modification
"""

from enum import Enum, auto


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Size(Enum):
    SMALL = auto()
    MEDIUM = auto()
    LARGE = auto()


class Product:
    def __init__(self, name, color, size):
        self.size = size
        self.color = color
        self.name = name


class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p


# Enterprise Patterns: Specification
class Specification:
    def is_satisfied(self, item):
        pass

    # syntatic sugar
    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class Filter:
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.specs = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.specs))


class OrSpecification(Specification):
    def __init__(self, *args):
        self.specs = args

    def is_satisfied(self, item):
        return any(map(lambda spec: spec.is_satisfied(item), self.specs))


class ItemFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


APPLE = Product("Apple", Color.GREEN, Size.SMALL)
TREE = Product("Tree", Color.GREEN, Size.LARGE)
HOUSE = Product("House", Color.BLUE, Size.LARGE)

PRODUCTS = [APPLE, TREE, HOUSE]
PF = ProductFilter()
print("Green products (old):")
for p in PF.filter_by_color(PRODUCTS, Color.GREEN):
    print(f" - {p.name} is green")

BF = ItemFilter()
print("Green products (new):")
GREEN = ColorSpecification(Color.GREEN)
for p in BF.filter(PRODUCTS, GREEN):
    print(f" - {p.name} is green")

print("Large products:")
LARGE = SizeSpecification(Size.LARGE)
for p in BF.filter(PRODUCTS, LARGE):
    print(f" - {p.name} is large")

print("Large blue items:")
large_blue = LARGE and ColorSpecification(Color.BLUE)
for p in BF.filter(PRODUCTS, large_blue):
    print(f" - {p.name} is large and blue")

print("Large or green items:")
# Does not work with the or operator
large_or_green = LARGE | GREEN
for p in BF.filter(PRODUCTS, large_or_green):
    print(f" - {p.name} is large or green")
