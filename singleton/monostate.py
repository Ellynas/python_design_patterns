# why use hat ?


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self) -> None:
        self.name = ""
        self.money_managed = 0

    def __str__(self) -> str:
        return f"{self.name} manages {self.money_managed}"


def main():
    cfo = CFO()
    cfo.name = "Steve"
    cfo.money_managed = 1
    print(cfo)

    cfo2 = CFO()
    cfo2.name = "Ruth"
    cfo2.money_managed = 10
    print(cfo2)
    print(cfo)


if __name__ == "__main__":
    main()
