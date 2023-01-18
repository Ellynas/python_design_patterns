"""
Chain of responsibility
- A chain of components who all get a chance to process a command
  or a query, optionally having default processing implementation
  and an ability to terminate the processig chain.

Command Query Separation
- Command = asking for an action or change (e.g., please set your
  attack value to 2)
- Query = asking for information (e.g., please give me your attack)
- CQS = having separate means of sending commands and queries
"""


class Creature:

    BASE_ATTACK = 1
    BASE_DEFENSE = 1

    def __init__(self, name, attack, defense):
        self.defense = defense
        self.attack = attack
        self.name = name

    def __str__(self):
        return f"{self.name} ({self.attack}/{self.defense})"


class Goblin(Creature):

    BASE_ATTACK = 1
    BASE_DEFENSE = 1
    BASE_NAME = "Goblin"

    def __init__(self, name=BASE_NAME, attack=BASE_ATTACK, defense=BASE_DEFENSE):
        super().__init__(name, attack, defense)


class CreatureModifier:
    def __init__(self, creature):
        self.creature: Creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusesModifier(CreatureModifier):
    def handle(self):
        print("No bonuses for you!")
        self.creature.attack = self.creature.BASE_ATTACK
        self.creature.defense = self.creature.BASE_DEFENSE


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f"Doubling {self.creature.name}'s attack")
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f"Increasing {self.creature.name}" "s defense")
            self.creature.defense += 1
        super().handle()


if __name__ == "__main__":
    GOBLIN = Goblin()
    print(GOBLIN)

    ROOT = CreatureModifier(GOBLIN)

    # this one blocks the chain (no call to super().handle(), so no propagation)
    # ROOT.add_modifier(NoBonusesModifier(GOBLIN))

    ROOT.add_modifier(IncreaseDefenseModifier(GOBLIN))
    ROOT.add_modifier(DoubleAttackModifier(GOBLIN))
    ROOT.add_modifier(DoubleAttackModifier(GOBLIN))

    # ROOT.add_modifier(NoBonusesModifier(GOBLIN))

    ROOT.handle()  # apply modifiers
    print(GOBLIN)
