# this works !

def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self) -> None:
        print("loading Database")


def main():
    db1 = Database()
    db2 = Database()
    print(db1 == db2)


if __name__ == "__main__":
    main()
