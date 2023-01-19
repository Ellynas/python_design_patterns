"""
Our system has any number of instances of Participant  classes. Each Participant has a value integer attribute, initially zero.

A participant can say()  a particular value, which is broadcast to all other participants.
At this point in time, every other participant is obliged to increase their value  by the value being broadcast.

Example:
    Two participants start with values 0 and 0 respectively
    Participant 1 broadcasts the value 3. We now have Participant 1 value = 0, Participant 2 value = 3
    Participant 2 broadcasts the value 2. We now have Participant 1 value = 2, Participant 2 value = 3
"""

import unittest


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class Participant:
    def __init__(self, mediator):
        self.value = 0
        self.mediator: Mediator = mediator
        self.mediator.alert.append(self.mediator_alert)

    def mediator_alert(self, sender, value):
        if sender != self:
            self.value += value

    def say(self, value):
        self.mediator.broadcast(self, value)


class Mediator:
    def __init__(self):
        self.alert = Event()

    def broadcast(self, sender, value):
        self.alert(sender, value)


class FirstTestSuite(unittest.TestCase):
    def test(self):
        m = Mediator()
        p1 = Participant(m)
        p2 = Participant(m)

        self.assertEqual(0, p1.value)
        self.assertEqual(0, p2.value)

        p1.say(2)

        self.assertEqual(0, p1.value)
        self.assertEqual(2, p2.value)

        p2.say(4)

        self.assertEqual(4, p1.value)
        self.assertEqual(2, p2.value)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
