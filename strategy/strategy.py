"""
Strategy
- Enables the exact behavior of a system to be selected at run-time

Motivation
- Many algorithms can be decomposed into higher and lower level parts
- Making tea can be decomposed into
  - The process of making a hot beverage (boil water, pour into cup); and
  - Tea-specific things (put teabag into water)
- The high-level algorithm can then be reused for making coffee or hot
  chocolate
  - Supported by beverage-specific strategies
"""


from abc import ABC, abstractmethod
from enum import Enum, auto


class OutputFormat(Enum):
    MARKDOWN = auto()
    HTML = auto()


# not required but a good idea
class ListStrategy(ABC):
    @abstractmethod
    def start(self, buffer: list):
        pass

    @abstractmethod
    def end(self, buffer: list):
        pass

    @abstractmethod
    def add_list_item(self, buffer: list, item):
        pass


class MarkdownListStrategy(ListStrategy):
    def start(self, buffer):
        pass

    def end(self, buffer):
        pass

    def add_list_item(self, buffer, item):
        buffer.append(f" * {item}\n")


class HtmlListStrategy(ListStrategy):
    def start(self, buffer):
        buffer.append("<ul>\n")

    def end(self, buffer):
        buffer.append("</ul>\n")

    def add_list_item(self, buffer, item):
        buffer.append(f"  <li>{item}</li>\n")


class TextProcessor:
    def __init__(self, list_strategy=HtmlListStrategy()):
        self.buffer = []
        self.list_strategy = list_strategy

    def append_list(self, items):
        self.list_strategy.start(self.buffer)
        for item in items:
            self.list_strategy.add_list_item(self.buffer, item)
        self.list_strategy.end(self.buffer)

    def set_output_format(self, format):
        if format == OutputFormat.MARKDOWN:
            self.list_strategy = MarkdownListStrategy()
        elif format == OutputFormat.HTML:
            self.list_strategy = HtmlListStrategy()

    def clear(self):
        self.buffer.clear()

    def __str__(self):
        return "".join(self.buffer)


if __name__ == "__main__":
    items = ["foo", "bar", "baz"]

    TP = TextProcessor()
    TP.set_output_format(OutputFormat.MARKDOWN)
    TP.append_list(items)
    print(TP)

    TP.set_output_format(OutputFormat.HTML)
    TP.clear()
    TP.append_list(items)
    print(TP)
