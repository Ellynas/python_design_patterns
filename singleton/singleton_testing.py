from typing import Any
import unittest


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonDatabase(metaclass=Singleton):
    def __init__(self) -> None:
        self.population = {
            "tokyo": 10_000,
            "paris": 10_000,
            "your mom": 10_000_000,
            "me": 0,
        }


class DummyDatabase:
    def __init__(self) -> None:
        self.population = {
            "alpha": 1,
            "beta": 2,
            "gamma": 3,
            "me": 0,
        }


class SingletonRecordFinder:
    def total_population(self, record):
        result = 0
        for r in record:
            result += SingletonDatabase().population.get(r, 0)
        return result


class ConfigurableRecordFinder:
    def __init__(self, db=SingletonDatabase()) -> None:
        self.db = db

    def total_population(self, record):
        result = 0
        for r in record:
            result += self.db.population.get(r, 0)
        return result


class SingletonTest(unittest.TestCase):
    def test_is_singleton(self):
        db1 = SingletonDatabase()
        db2 = SingletonDatabase()
        self.assertIs(db1, db2)

    def test_singleton_total_population(self):
        rf = ConfigurableRecordFinder(DummyDatabase())    # type: ignore
        names = ["alpha", "gamma"]
        expected = 4
        total = rf.total_population(names)
        self.assertEqual(total, expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
