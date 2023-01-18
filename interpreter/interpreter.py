"""
Interpreter
- A component that processes structured text data. Does so by turning it into
  separate lexical tokens (lexing) and then interpreting sequences of said
  tokens (parsing)
"""

from enum import Enum, auto
from typing import Any, List


class Token:
    class Type(Enum):
        INTEGER = auto()
        PLUS = auto()
        MINUS = auto()
        LPAREN = auto()
        RPAREN = auto()

    def __init__(self, type, text):
        self.type = type
        self.text = text

    def __str__(self):
        return f"`{self.text}`"


def lex(input) -> List[Token]:
    tokens: List[Token] = []

    i = 0
    while i < len(input):
        if input[i] == "+":
            tokens.append(Token(Token.Type.PLUS, "+"))
        elif input[i] == "-":
            tokens.append(Token(Token.Type.MINUS, "-"))
        elif input[i] == "(":
            tokens.append(Token(Token.Type.LPAREN, "("))
        elif input[i] == ")":
            tokens.append(Token(Token.Type.RPAREN, ")"))
        else:  # must be a number
            digits = [input[i]]
            for j in range(i + 1, len(input)):
                if input[j].isdigit():
                    digits.append(input[j])
                    i += 1
                else:
                    tokens.append(Token(Token.Type.INTEGER, "".join(digits)))
                    break
        i += 1

    return tokens


# ↑↑↑ lexing ↑↑↑

# ↓↓↓ parsing ↓↓↓


class Integer:
    def __init__(self, value):
        self.value = value


class BinaryOperation:
    class Type(Enum):
        ADDITION = auto()
        SUBTRACTION = auto()

    def __init__(self):
        self.type: Any = None
        self.left: Any = None
        self.right: Any = None

    @property
    def value(self):
        if self.type == self.Type.ADDITION:
            return self.left.value + self.right.value
        elif self.type == self.Type.SUBTRACTION:
            return self.left.value - self.right.value

    @property
    def is_complete(self):
        if self.type and self.left and self.right:
            return True
        return False


def parse(tokens: List[Token]):
    result = BinaryOperation()
    have_lhs = False
    i = 0
    while i < len(tokens):
        if result.is_complete:
            new_left_value = Integer(result.value)
            result = BinaryOperation()
            result.left = new_left_value
            have_lhs = True
        token = tokens[i]

        if token.type == Token.Type.INTEGER:
            integer = Integer(int(token.text))
            if not have_lhs:
                result.left = integer
                have_lhs = True
            else:
                result.right = integer
        elif token.type == Token.Type.PLUS:
            result.type = BinaryOperation.Type.ADDITION
        elif token.type == Token.Type.MINUS:
            result.type = BinaryOperation.Type.SUBTRACTION
        elif token.type == Token.Type.LPAREN:  # note: no if for RPAREN
            j = i
            while j < len(tokens):
                if tokens[j].type == Token.Type.RPAREN:
                    break
                j += 1
            # preprocess subexpression
            subexpression = tokens[i + 1 : j]
            element = parse(subexpression)
            if not have_lhs:
                result.left = element
                have_lhs = True
            else:
                result.right = element
            i = j  # advance
        i += 1
    return result


def eval(input):
    tokens = lex(input)
    print(" ".join(map(str, tokens)))

    parsed = parse(tokens)
    print(f"{input} = {parsed.value}")


if __name__ == "__main__":
    eval("(13+4)-(12+1)")
    eval("1+(3-4)")
    eval("1+2+(3-4)")
