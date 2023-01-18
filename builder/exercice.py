class Field:
    def __init__(self, name, value):
        self.value = value
        self.name = name

    def __str__(self):
        return f"self.{self.name} = {self.value}"


class Class:
    def __init__(self, name):
        self.name = name
        self.fields = []

    def __str__(self):
        lines = [f"class {self.name}:"]
        if not self.fields:
            lines.append("  pass")
        else:
            lines.append("  def __init__(self):")
            for f in self.fields:
                lines.append(f"    {str(f)}")
        return "\n".join(lines)

    @staticmethod
    def new(name):
        return ClassBuilder(name)


class ClassBuilder:
    def __init__(self, root_name):
        self.__class = Class(root_name)

    def add_field(self, type, name):
        self.__class.fields.append(Field(type, name))
        return self

    def __str__(self):
        return self.__class.__str__()


def main():
    cb = Class.new("Person").add_field("name", '""').add_field("age", "0")
    print(cb)


if __name__ == "__main__":
    main()
