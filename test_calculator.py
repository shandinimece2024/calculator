import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_calculate_with_happiness_and_sadness(self):
        self.assertEqual(calculate("+ happiness - sadness"), 0)


if __name__ == "__main__":
    unittest.main()
