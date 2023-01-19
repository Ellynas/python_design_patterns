"""
You are given a game scenario with classes Goblin and GoblinKing. Please implement the following rules:

    A goblin has base 1 attack/1 defense (1/1), a goblin king is 3/3.

    When the Goblin King is in play, every other goblin gets +1 Attack.

    Goblins get +1 to Defense for every other Goblin in play (a GoblinKing is a Goblin!).

Example:

    Suppose you have 3 ordinary goblins in play. Each one is a 1/3 (1/1 + 0/2 defense bonus).

    A goblin king comes into play. Now every goblin is a 2/4 (1/1 + 0/3 defense bonus from each other + 1/0 from goblin king)

The state of all the goblins has to be consistent as goblins are added and removed from the game.
"""


import unittest
from abc import ABC, abstractmethod
from enum import Enum, auto

from typing import List

# creature removal (unsubscription) ignored in this exercise solution


class Creature(ABC):
    def __init__(self, game: "Game", attack, defense):
        self.initial_defense = defense
        self.initial_attack = attack
        self.game = game

    @property
    def attack(self):
        """
        Logic :
        - I need to know my attack.
        - I will build a query with my base attack value, and the fact that that value is, in fact, my attack
        - I will then ask every other creature ine the game how their presence affects my attack, telling them that it is _I_ that asks
        - I will return the now updated value of the attack value in the query
        """
        q = Query(self.initial_attack, WhatToQuery.ATTACK)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @property
    def defense(self):
        q = Query(self.initial_defense, WhatToQuery.DEFENSE)
        for c in self.game.creatures:
            c.query(self, q)
        return q.value

    @abstractmethod
    def query(self, source: "Creature", query: "Query"):
        pass


class WhatToQuery(Enum):
    ATTACK = auto()
    DEFENSE = auto()


class Query:
    def __init__(self, initial_value, what_to_query: WhatToQuery):
        self.what_to_query = what_to_query
        self.value = initial_value


class Goblin(Creature):
    def __init__(self, game, attack=1, defense=1):
        super().__init__(game, attack, defense)

    def query(self, source: Creature, query: Query):
        if isinstance(source, Goblin) and self != source and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 1


class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, 3, 3)

    def query(self, source: Creature, query: Query):
        if isinstance(source, Goblin) and self != source and query.what_to_query == WhatToQuery.ATTACK:
            query.value += 1
        else:
            super().query(source, query)


class Wolf(Creature):
    def __init__(self, game, attack=2, defense=2):
        super().__init__(game, attack, defense)

    def query(self, source: Creature, query: Query):
        # Goblins are afraid of wolves
        if isinstance(source, Goblin) and query.what_to_query == WhatToQuery.DEFENSE:
            query.value = max(query.value - 1, 0)


class Game:
    def __init__(self):
        self.creatures: List[Creature] = []


class FirstTestSuite(unittest.TestCase):
    def test(self):
        game = Game()
        goblin = Goblin(game)
        game.creatures.append(goblin)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(1, goblin.defense)

        goblin2 = Goblin(game)
        game.creatures.append(goblin2)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)

        goblin3 = GoblinKing(game)
        game.creatures.append(goblin3)
        self.assertEqual(2, goblin.attack)
        self.assertEqual(3, goblin.defense)

        wolf = Wolf(game)
        game.creatures.append(wolf)
        self.assertEqual(goblin.defense, 2)
        self.assertEqual(wolf.attack, 2)
        self.assertEqual(wolf.defense, 2)

        game.creatures.remove(wolf)
        self.assertEqual(goblin.defense, 3)

        game.creatures.remove(goblin3)
        self.assertEqual(1, goblin.attack)
        self.assertEqual(2, goblin.defense)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
