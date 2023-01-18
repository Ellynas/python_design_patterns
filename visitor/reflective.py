from abc import ABC


class Expression(ABC):
    # still an intrusive approach, violates OCP
    def print(self, buffer):
        ExpressionPrinter.print(self, buffer)


class DoubleExpression(Expression):
    def __init__(self, value):
        self.value = value


class AdditionExpression(Expression):
    def __init__(self, left, right):
        self.right = right
        self.left = left


class ExpressionPrinter:
    # still breaks OCP because new types require M×N modifications.
    # will still work "silently" if you add a SubstractionExpression class for exemple
    @staticmethod
    def print(expression, buffer: list):
        """Will fail silently on a missing case."""
        if isinstance(expression, DoubleExpression):
            buffer.append(str(expression.value))
        elif isinstance(expression, AdditionExpression):
            buffer.append("(")
            ExpressionPrinter.print(expression.left, buffer)
            buffer.append("+")
            ExpressionPrinter.print(expression.right, buffer)
            buffer.append(")")


if __name__ == "__main__":
    # represents 1+(2+3)
    E = AdditionExpression(DoubleExpression(1), AdditionExpression(DoubleExpression(2), DoubleExpression(3)))
    BUFFER = []

    # ExpressionPrinter.print(E, BUFFER)

    E.print(BUFFER)
    print("".join(BUFFER))
