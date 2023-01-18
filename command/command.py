"""
Command
- An object which represents an instruction to perform a particular action.
  Contains all the information necessary for the action to be taken.

Motivation
- Ordinary statements are perishable
- Cannot undo member assignment
- Cannot directly serialize a sequence of actions (calls)
- Want an object that represents an operation
  - person should change its age to value 22
  - car should do explode()
- Uses: GUI commands , multilevel undo/redo, macro recording and more!
"""


from abc import ABC, abstractmethod
from enum import Enum, auto


class BankAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, balance = {self.balance}")

    def withdraw(self, amount) -> bool:
        if self.balance - amount >= BankAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f"Withdrew {amount}, balance = {self.balance}")
            return True
        return False

    def __str__(self):
        return f"Balance = {self.balance}"


class Command(ABC):
    @abstractmethod
    def __call__(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class BankAccountCommand(Command):
    def __init__(self, account: BankAccount, action: "BankAccountCommand.Action", amount: int):
        self.amount = amount
        self.action = action
        self.account = account
        self.success = None

    class Action(Enum):
        DEPOSIT = auto()
        WITHDRAW = auto()

    def __call__(self):
        if self.success:
            print("already called that command, make a new one, aborting")
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
        self.success = None


if __name__ == "__main__":
    BA = BankAccount()
    CMD = BankAccountCommand(BA, BankAccountCommand.Action.DEPOSIT, 100)
    CMD()
    print("After $100 deposit:", BA)

    CMD()
    print("After a second call for a $100 deposit:", BA)

    CMD.undo()
    print("$100 deposit undone:", BA)

    CMD.undo()
    print("$100 deposit undone again ?", BA)

    ILLEGAL_CMD = BankAccountCommand(BA, BankAccountCommand.Action.WITHDRAW, 1000)
    ILLEGAL_CMD()
    print("After impossible withdrawal:", BA)
    ILLEGAL_CMD.undo()
    print("After undo:", BA)
