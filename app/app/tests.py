"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    def test_add_numbers_accuracy(self):
        """test adding number togeter"""
        result = calc.add(4, 6)
        self.assertEqual(result, 10)

    def test_subtract_numbers(self):
        res = calc.subtract(10, 15)
        self.assertEqual(res, 5)
