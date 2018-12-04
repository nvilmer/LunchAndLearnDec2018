from unittest import TestCase
from daugherty.utils import Utils

class UtilsTest(TestCase):
    def testUtilsIsSingleton(self):
        a = Utils
        b = Utils()
        self.assertEqual(a, b)

    def testEvenNumbers(self):
        numbersIn = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numbersOut = Utils.evenNumbers(self, numbersIn)
        self.assertTrue(all(num % 2 == 0 for num in numbersOut))
