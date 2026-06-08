import unittest

from calculator import calculate


class CalculatorTests(unittest.TestCase):
    def test_calculate_with_happiness_and_sadness(self):
        self.assertEqual(calculate("+ happiness - sadness"), 0)

    def test_single_token_expressions(self):
        self.assertEqual(calculate("+ happiness"), 1)
        self.assertEqual(calculate("- sadness"), -1)

    def test_multiple_tokens(self):
        self.assertEqual(calculate("+ happiness + happiness"), 2)

    def test_invalid_token_raises(self):
        with self.assertRaises(ValueError):
            calculate("+ joy")

    def test_empty_expression(self):
        self.assertEqual(calculate(""), 0)


if __name__ == "__main__":
    unittest.main()
