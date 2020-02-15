import unittest
from input_validation import validation_with_try as average


def test_average_exception(self):
    with self.assertRaises(ValueError):
        average(-95, 70, 50)


if __name__ == '__main__':
    unittest.main()
