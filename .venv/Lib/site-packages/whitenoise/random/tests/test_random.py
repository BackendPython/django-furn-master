from unittest import TestCase

from whitenoise.random import random_string

class TestRandom(TestCase):
    def testUpper(self):
        retval = random_string(6, lower=False, digit=False, symbol=False)
        self.assertEqual(retval.upper(), retval)
