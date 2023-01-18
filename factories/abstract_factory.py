from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import List, Tuple


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print("this tea is good")


class Coffee(HotDrink):
    def consume(self):
        print("this coffee is good")


class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount) -> HotDrink:
        pass


class TeaFactory(ABC):
    def prepare(self, amount) -> HotDrink:
        print(f"teabag, water, pour {amount}...")
        return Tea()


class CoffeeFactory(ABC):
    def prepare(self, amount) -> HotDrink:
        print(f"grind coffee, water, pour {amount}, wait...")
        return Coffee()


class HotDrinkMachine(object):
    class AvailableDrink(Enum):
        TEA = auto()
        COFFEE = auto()

    factories: List[Tuple[str, HotDrinkFactory]] = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.capitalize()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def order_drink(self) -> HotDrink:
        print("Available drinks:")
        for i, f in enumerate(self.factories):
            print(f"{i}- {f[0]}")

        s = input(f"Please pick drink (0-{len(self.factories) - 1}): ")
        idx = int(s)
        s = input("Specify amout: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


def main():
    hdm = HotDrinkMachine()
    drink = hdm.order_drink()
    drink.consume()


if __name__ == "__main__":
    main()
