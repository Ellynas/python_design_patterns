# 1) event broker
# 2) command-query separation (cqs)
# 3) observer
from abc import ABC, abstractmethod
from enum import Enum, auto

from typing import List, Callable


class Events(List[Callable]):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = auto()
    DEFENSE = auto()


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.value = default_value  # bidirectional
        self.what_to_query = what_to_query
        self.creature_name = creature_name


class Game:
    def __init__(self):
        self.events = Events()

    def perform_query(self, sender: "Creature", query: Query):
        self.events(sender, query)


class Creature:
    def __init__(self, game: Game, name, attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.name, WhatToQuery.DEFENSE, self.initial_attack)
        self.game.perform_query(self, q)
        return q.value

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class CreatureModifier(ABC):
    def __init__(self, game: Game, creature: Creature):
        self.creature = creature
        self.game = game

    @abstractmethod
    def handle(self, sender: Creature, query: Query):
        pass

    def __enter__(self):
        self.game.events.append(self.handle)
        return self

    def __exit__(self, *_):
        self.game.events.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 3


if __name__ == "__main__":
    GAME = Game()
    GOBLIN = Creature(GAME, "Strong Goblin", 2, 2)
    print(GOBLIN)
    with DoubleAttackModifier(GAME, GOBLIN), IncreaseDefenseModifier(GAME, GOBLIN):
        print(GOBLIN)
    print(GOBLIN)
