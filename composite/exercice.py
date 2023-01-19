"""
Consider the code presented below. We have two classes called SingleValue and ManyValues. SingleValue stores just one numeric value, but ManyValues can store either numeric values or SingleValue objects.

You are asked to give both SingleValue and ManyValues a property member called sum that returns a sum of all the values that the object contains. Please ensure that there is only a single method that realizes the property sum, not multiple methods.
"""


import unittest
from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):
    @property
    def sum(self):
        result = 0
        for c in self:
            if isinstance(c, ValueContainer):
                result += c.sum
            elif isinstance(c, int) or isinstance(c, float):
                result += c
            else:
                print(f"ignoring {c}, cannot deal with it")
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass


class FirstTestSuite(unittest.TestCase):
    def test(self):
        single_value = SingleValue(11)
        other_values = ManyValues()
        other_values.append(22)
        other_values.append(33)
        # make a list of all values
        all_values = ManyValues()
        all_values.append(single_value)
        all_values.append(other_values)
        self.assertEqual(all_values.sum, 66)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
