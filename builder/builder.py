# piecewise construction
# several methods to constructs an object step by step

from typing import List


class HtmlElement(object):
    indent_size = 2

    def __init__(self, name: str = "", text: str = "") -> None:
        self.name = name
        self.text = text
        self.child_elements: List[HtmlElement] = []

    def __str(self, indent: int):
        lines = []
        i = " " * (indent * self.indent_size)
        lines.append(f"{i}<{self.name}>")

        if self.text:
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{self.text}")

        for e in self.child_elements:
            lines.append(e.__str(indent + 1))

        lines.append(f"{i}</{self.name}>")
        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)

    @staticmethod
    def create(name):
        return HtmlBuilder(name)


class HtmlBuilder(object):
    def __init__(self, root_name: str) -> None:
        self.root_name = root_name
        self.__root = HtmlElement(root_name)

    def add_child(self, name: str, text: str):
        self.__root.child_elements.append(HtmlElement(name, text))
        return self

    def __str__(self) -> str:
        return str(self.__root)


def main():
    builder = HtmlElement.create("ul")
    builder.add_child("li", "hello").add_child("li", "world")
    print(builder)


if __name__ == "__main__":
    main()
