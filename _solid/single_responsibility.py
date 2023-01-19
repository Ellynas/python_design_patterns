"""
Single Responsibility Principle
- A class only have one reason to change
- Separation of concerns:
    - different classes handling different, independent
      tasks/problems
"""


class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)

    # methods below give class responsibility of persistence, bad idea!
    def save(self, filename):
        with open(filename, "w") as f:
            f.write(str(self))

    def load(self, filename):
        pass

    def load_from_web(self, url):
        pass


J = Journal()
J.add_entry("I cried today.")
J.add_entry("I ate a bug.")
print(f"Journal entries:\n{J}")


class PersistenceManager :
    # instead, create another class to handle that responsibility
    @staticmethod
    def save_to_file(journal, filename):
        with open(filename, "w") as f:
            f.write(str(journal))

    def load(self, filename):
        pass

    def load_from_web(self, url):
        pass
