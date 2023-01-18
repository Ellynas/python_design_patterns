"""
Mediator
- A component that facilitates communication between other components
  without them necessarily being aware of each other or having
  direct (reference) access to each other

Motivation
- Components may go in and out of a system at any time
  - Chat room participants
  - Players in a MMORPG
- It makes no sense for them to have direct references to one another
  - Those references may go dead
- Solution: have them all refer to some central component that facilitates
  communication
"""

from typing import Optional, List


class Person:
    def __init__(self, name):
        self.name = name
        self.chat_log = []
        self.room: Optional[ChatRoom] = None

    def receive(self, sender, message):
        s = f"{sender}: {message}"
        print(f"[{self.name}'s chat session] {s}")
        self.chat_log.append(s)

    def say(self, message):
        if self.room:
            self.room.broadcast(self.name, message)

    def private_message(self, who, message):
        if self.room:
            self.room.message(self.name, who, message)


class ChatRoom:
    """here, this is the mediator"""
    def __init__(self):
        self.people: List[Person] = []

    def broadcast(self, source, message):
        for p in self.people:
            if p.name != source:
                p.receive(source, message)

    def join(self, person: Person):
        join_msg = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.room = self
        self.people.append(person)

    def message(self, source, destination, message):
        for p in self.people:
            if p.name == destination:
                p.receive(source, message)


if __name__ == "__main__":
    ROOM = ChatRoom()

    JOHN = Person("John")
    JANE = Person("Jane")

    ROOM.join(JOHN)
    ROOM.join(JANE)

    JOHN.say("hi ROOM")
    JANE.say("oh, hey JOHN")

    SIMON = Person("Simon")
    ROOM.join(SIMON)
    SIMON.say("hi everyone!")

    JANE.private_message(SIMON.name, "glad you could join us!")
