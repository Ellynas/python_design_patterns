"""
You are given a class called Sentence, which takes a string such as 'hello world'. You need to provide an interface such that the indexer returns a flyweight that can be used to capitalize a particular word in the sentence.

Typical use would be something like:

    sentence = Sentence('hello world')
    sentence[1].capitalize = True
    print(sentence)  # writes "hello WORLD"
"""

import unittest


class Sentence:
    def __init__(self, plain_text):
        self.words = plain_text.split(" ")
        self.tokens = {}

    class WordToken:
        def __init__(self, capitalize=False):
            self.capitalize = capitalize

    def __getitem__(self, index) -> WordToken:
        if not self.tokens.get(index, None):
            self.tokens[index] = self.WordToken()
        return self.tokens[index]

    def __str__(self):
        result = []
        for i in range(len(self.words)):
            w = self.words[i]
            if i in self.tokens and self.tokens[i].capitalize:
                w = w.upper()
            result.append(w)
        return " ".join(result)


class Evaluate(unittest.TestCase):
    def test_exercise(self):
        s = Sentence("alpha beta gamma beta")
        s[1].capitalize = True
        self.assertEqual(str(s), "alpha BETA gamma beta")


def main():
    unittest.main()


if __name__ == "__main__":
    main()
