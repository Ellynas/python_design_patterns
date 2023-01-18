class Person:
    def __init__(self, id, name):
        self.__id = id
        self.name = name

    @property
    def id(self):
        return self.__id

    def __str__(self) -> str:
        return f"id: {self.id}, name: {self.name}"


class PersonFactory:
    id = 0

    @classmethod
    def create_person(cls, name):
        p = Person(cls.id, name)
        cls.id += 1
        return p


def main():
    p1 = PersonFactory.create_person("toto")
    print(p1)
    p2 = PersonFactory.create_person("tata")
    print(p2)
    p3 = PersonFactory.create_person("titi")
    print(p3)


if __name__ == "__main__":
    main()
