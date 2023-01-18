class Person:
    def __init__(self):
        # address
        self.street_address = None
        self.postcode = None
        self.city = None

        # employment
        self.company_name = None
        self.position = None
        self.annual_income = None

    def __str__(self):
        return (
            f"Address: {self.street_address}, {self.postcode}, {self.city}"
            + f"\nEmployed at {self.company_name} as a {self.position} earning {self.annual_income}"
        )


class PersonBuilder(object):
    def __init__(self, person=Person()) -> None:
        self.person = person

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, company_name):
        self.person.company_name = company_name
        return self

    def as_a(self, position):
        self.person.position = position
        return self

    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person) -> None:
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def at_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


def main():
    person = (
        PersonBuilder()
        .works.at("google")
        .as_a("consultant")
        .earning("so so much")
        .lives.at("that address")
        .in_city("Silicon valey")
        .at_postcode(1234)
        .build()
    )
    print(person)


if __name__ == "__main__":
    main()
