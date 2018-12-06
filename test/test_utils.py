import unittest, tempfile, shutil
from os import path
from daugherty.utils import Utils, Config


class UtilsTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def testUtilsIsSingleton(self):
        first_instance = Utils()
        second_instance = Utils()
        self.assertIs(first_instance, second_instance)

    def testFilterEvenNumbers(self):
        numbers_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numbers_out = Utils.filter_even_numbers(numbers_in)
        self.assertTrue(all(num % 2 == 0 for num in numbers_out))

    def testFilterOddNumbers(self):
        numbers_in = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        numbers_out = Utils.filter_odd_numbers(numbers_in)
        self.assertTrue(all(num % 2 != 0 for num in numbers_out))

    def testLoadConfig(self):
        with open(path.join(self.test_dir, 'config.properties'), 'w') as config_file:
            config_file.write('# Test config.properties\n')
            config_file.write('user.name=bob\n')
            config_file.write('user.location=dallas\n')

        config = Config()
        config.load_properties(self.test_dir + '/config.properties')
        self.assertEqual(config.getProperties()['user.name'], 'bob')
        self.assertEqual(config.getProperties()['user.location'], 'dallas')
