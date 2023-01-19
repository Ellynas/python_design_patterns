"""
Consider the quadratic equation and its canonical solution.
The part b^2-4*a*c is called the discriminant. Suppose we want to provide an API with two different strategies for calculating the discriminant:
    In OrdinaryDiscriminantStrategy, if the discriminant is negative, we return it as-is. This is OK, since our main API returns Complex  numbers anyway.
    In RealDiscriminantStrategy, if the discriminant is negative, the return value is NaN (not a number). NaN propagates throughout the calculation, so the equation solver gives two NaN values. In Python, you make such a number with float('nan').

Please implement both of these strategies as well as the equation solver itself. With regards to plus-minus in the formula, please return the + result as the first element and - as the second. Note that the solve() method is expected to return complex values.
"""

import math
import cmath
import unittest
from abc import ABC, abstractmethod


class DiscriminantStrategy(ABC):
    @abstractmethod
    def calculate_discriminant(self, a, b, c) -> float:
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c) -> float:
        return b * b - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c) -> float:
        result = b * b - 4 * a * c
        return result if result >= 0 else float("nan")


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy: DiscriminantStrategy = strategy

    def solve(self, a, b, c):
        """Returns a pair of complex (!) values"""
        disc = complex(self.strategy.calculate_discriminant(a, b, c), 0)
        root_disc = cmath.sqrt(disc)
        return ((-b + root_disc) / (2 * a), (-b - root_disc) / (2 * a))


class Evaluate(unittest.TestCase):
    def test_positive_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_positive_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 10, 16)
        self.assertEqual(complex(-2, 0), results[0])
        self.assertEqual(complex(-8, 0), results[1])

    def test_negative_ordinary(self):
        strategy = OrdinaryDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertEqual(complex(-2, 1), results[0])
        self.assertEqual(complex(-2, -1), results[1])

    def test_negative_real(self):
        strategy = RealDiscriminantStrategy()
        solver = QuadraticEquationSolver(strategy)
        results = solver.solve(1, 4, 5)
        self.assertTrue(math.isnan(results[0].real))
        self.assertTrue(math.isnan(results[1].real))
        self.assertTrue(math.isnan(results[0].imag))
        self.assertTrue(math.isnan(results[1].imag))


def main():
    unittest.main()


if __name__ == "__main__":
    main()
