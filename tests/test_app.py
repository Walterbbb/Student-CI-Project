import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import add_numbers


class TestAddNumbers(unittest.TestCase):
    def test_add_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add_numbers(-1, 1), 0)


if __name__ == "__main__":
    unittest.main()
