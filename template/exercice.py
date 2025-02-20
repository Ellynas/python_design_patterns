"""
Imagine a typical collectible card game which has cards representing creatures.
Each creature has two values: Attack and Health. Creatures can fight each other, dealing their Attack damage, thereby reducing their opponent's health.

The class CardGame implements the logic for two creatures fighting one another. However, the exact mechanics of how damage is dealt is different:
    TemporaryCardDamage: In some games (e.g., Magic: the Gathering), unless the creature has been killed, its health returns to the original value at the end of combat.
    PermanentCardDamage: In other games (e.g., Hearthstone), health damage persists.

You are asked to implement classes TemporaryCardDamageGame and PermanentCardDamageGame  that would allow us to simulate combat between creatures.

Some examples:
    With temporary damage, creatures 1/2 and 1/3 can never kill one another. With permanent damage, second creature will win after 2 rounds of combat.
    With either temporary or permanent damage, two 2/2 creatures kill one another.
"""

import unittest
from abc import ABC


class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack


class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        first: Creature = self.creatures[c1_index]
        second: Creature = self.creatures[c2_index]
        self.hit(first, second)
        self.hit(second, first)
        first_alive = first.health > 0
        second_alive = second.health > 0
        if first_alive == second_alive:
            return -1
        return c1_index if first_alive else c2_index

    def hit(self, attacker: Creature, defender: Creature):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        old_health = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = old_health


class PermanentDamageCardGame(CardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack


class Evaluate(unittest.TestCase):
    def test_impasse(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), "Combat should yield -1 since nobody died.")
        self.assertEqual(-1, game.combat(0, 1), "Combat should yield -1 since nobody died.")

    def test_temporary_murder(self):
        c1 = Creature(1, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(1, game.combat(0, 1))

    def test_double_murder(self):
        c1 = Creature(2, 1)
        c2 = Creature(2, 2)
        game = TemporaryDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1))

    def test_permanent_damage_death(self):
        c1 = Creature(1, 2)
        c2 = Creature(1, 3)
        game = PermanentDamageCardGame([c1, c2])
        self.assertEqual(-1, game.combat(0, 1), "Nobody should win this battle.")
        self.assertEqual(1, c1.health)
        self.assertEqual(2, c2.health)
        self.assertEqual(1, game.combat(0, 1), "Creature at index 1 should win this")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
