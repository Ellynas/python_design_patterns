from enum import Enum, auto


class Stat(Enum):
    strength = auto()
    agility = auto()
    intelligence = auto()


class Creature:
    def __init__(self):
        # self.strength = 10
        # self.agility = 10
        # self.intelligence = 10
        self.stats = {Stat.strength: 10, Stat.agility: 20, Stat.intelligence: 30}

    @property
    def strength(self):
        return self.stats[Stat.strength]

    @strength.setter
    def strength(self, value):
        self.stats[Stat.strength] = value

    @property
    def intelligence(self):
        return self.stats[Stat.intelligence]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Stat.intelligence] = value

    @property
    def agility(self):
        return self.stats[Stat.agility]

    @agility.setter
    def agility(self, value):
        self.stats[Stat.agility] = value

    @property
    def sum_of_stats(self):
        # unstable
        # return self.strength + self.intelligence + self.agility
        return sum(self.stats.values())

    @property
    def max_stat(self):
        # return max(
        #     self.strength, self.intelligence. self.agility
        # )
        return max(self.stats.values())

    @property
    def average_stats(self):
        # return self.sum_of_stats / 3.0
        return float(sum(self.stats.values()) / len(self.stats))


CREATURE = Creature()
print(CREATURE.average_stats)
