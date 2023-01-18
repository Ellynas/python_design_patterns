from typing import Any


class Singleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Database(metaclass=Singleton):
    def __init__(self) -> None:
        print("loading Database")


def main():
    db1 = Database()
    db2 = Database()
    print(db1 == db2)


if __name__ == "__main__":
    main()
