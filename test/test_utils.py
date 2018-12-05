import unittest
from daugherty.utils import Utils


class UtilsTest(unittest.TestCase):
    def testUtilsIsSingleton(self):
        first_instance = Utils()
        second_instance = Utils()
        self.assertIs(first_instance, second_instance)

    def testEvenNumbers(self):
        numbers_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numbers_out = Utils.even(numbers_in)
        self.assertTrue(all(num % 2 == 0 for num in numbers_out))
