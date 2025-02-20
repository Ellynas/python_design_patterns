class Person:
    def __init__(self, name):
        self.name = name
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f"{self.name} born on {self.date_of_birth} " + f"works as {self.position}"

    @staticmethod
    def new():
        return PersonBirthDateBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person(None)

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonBirthDateBuilder(PersonJobBuilder):
    def born(self, date_of_birth):
        self.person.date_of_birth = date_of_birth
        return self


def main():
    ME = Person.new().called("Dimitri").works_as_a("Quant").born("1/1/1980").build()
    print(ME)


if __name__ == "__main__":
    main()
