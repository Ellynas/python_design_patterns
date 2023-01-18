# This doesn't work !!!
# init is called twice

class Database:
    _instance = None

    def __init__(self) -> None:
        print("loading a database")

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
        return cls._instance


def main():
    db1 = Database()
    db2 = Database()

    print(db1 == db2)


if __name__ == "__main__":
    main()
