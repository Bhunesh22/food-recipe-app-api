
"""sample test"""

from django.test import SimpleTestCase

from .calc import Sum

class Clactest(SimpleTestCase):

    def test_add_nembers(self):

        res = Sum(5, 8)

        self.assertEqual(res, 13)