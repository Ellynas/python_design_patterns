# Composite Command a.k.a. Macro
# also: Composite design pattern ;)

import unittest
from abc import ABC, abstractmethod
from enum import Enum

from typing import List


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
            return True
        print(f"Withdrew {amount} impossible (balance is {self.balance}), aborting")
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


class Command(ABC):
    def __init__(self):
        self.success = False

    @abstractmethod
    def invoke(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account: BankAccount, action: "Action", amount):
        super().__init__()
        self.amount = amount
        self.action = action
        self.account = account

    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def invoke(self):
        if self.success:
            return
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True
        elif self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return
        # strictly speaking this is not correct
        # (you don't undo a deposit by withdrawing)
        # but it works for this demo, so...
        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)


# try using this before using MoneyTransferCommand!
class CompositeBankAccountCommand(Command, List[Command]):
    def __init__(self, items=[]):
        super().__init__()
        for i in items:
            self.append(i)

    def invoke(self):
        if self.success:
            return
        for x in self:
            x.invoke()

    def undo(self):
        if not self.success:
            return
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct: BankAccount, to_acct: BankAccount, amount):
        super().__init__(
            [
                BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount),
                BankAccountCommand(from_acct, BankAccountCommand.Action.WITHDRAW, amount),
            ]
        )

    def invoke(self):
        for cmd in self:
            cmd.invoke()
        self.success = all([cmd.success for cmd in self])
        if not self.success:
            print("error detected, undoing")
            for cmd in self:
                cmd.undo()


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        BA = BankAccount()
        deposit1 = BankAccountCommand(BA, BankAccountCommand.Action.DEPOSIT, 1000)
        deposit2 = BankAccountCommand(BA, BankAccountCommand.Action.DEPOSIT, 1000)
        composite = CompositeBankAccountCommand([deposit1, deposit2])
        composite.invoke()
        print(BA)
        composite.undo()
        print(BA)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        # composite isn't so good because of failure
        amount = 1000  # try 1000: no transactions should happen
        wc = BankAccountCommand(ba1, BankAccountCommand.Action.WITHDRAW, amount)
        dc = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, amount)

        transfer = CompositeBankAccountCommand([wc, dc])

        transfer.invoke()
        print("ba1:", ba1, "ba2:", ba2)  # end up in incorrect state
        transfer.undo()
        print("ba1:", ba1, "ba2:", ba2)

    def test_better_tranfer(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 1000

        transfer = MoneyTransferCommand(ba1, ba2, amount)
        transfer.invoke()
        print("ba1:", ba1, "ba2:", ba2)
        transfer.undo()
        print("ba1:", ba1, "ba2:", ba2)


def main():
    TestSuite().test_better_tranfer()


if __name__ == "__main__":
    main()
