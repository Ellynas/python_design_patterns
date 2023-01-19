"""
Implement the Account.process() method to process different account commands.

The rules are obvious:

    success indicates whether the operation was successful

    You can only withdraw money if you have enough in your account
"""

import unittest
from enum import Enum


class Command:
    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, action: Action, amount):
        self.action = action
        self.amount = amount
        self.success = False


class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def process(self, command: Command):
        if command.action == Command.Action.DEPOSIT:
            self.balance += command.amount
            command.success = True
        elif command.action == Command.Action.WITHDRAW:
            command.success = self.balance >= command.amount
            if command.success:
                self.balance -= command.amount


class Evaluate(unittest.TestCase):
    def test(self):
        a = Account()

        cmd = Command(Command.Action.DEPOSIT, 100)
        a.process(cmd)

        self.assertEqual(100, a.balance)
        self.assertTrue(cmd.success)

        cmd = Command(Command.Action.WITHDRAW, 50)
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertTrue(cmd.success)

        cmd.amount = 150
        a.process(cmd)

        self.assertEqual(50, a.balance)
        self.assertFalse(cmd.success)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
