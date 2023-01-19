"""
Since implementing a singleton is easy, you have a different challenge: write a function called is_singleton() . This method takes a factory method that returns an object and it's up to you to determine whether or not that object is a singleton instance.
"""


from unittest import TestCase
from copy import deepcopy


def is_singleton(factory):
    x = factory()
    y = factory()
    return x is y


class Evaluate(TestCase):
    def test_exercise(self):
        obj = [1, 2, 3]
        self.assertTrue(is_singleton(lambda: obj))
        self.assertFalse(is_singleton(lambda: deepcopy(obj)))
