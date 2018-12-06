__author__ = 'Norm Vilmer'
__project__ = 'LunchAndLearnDec2018'


# Single as a metaclass
class Singleton(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls.__instances[cls]


class Utils(metaclass=Singleton):
    @staticmethod
    def filter_even_numbers(numbers_in):
        return list(filter(lambda x: x % 2 == 0, numbers_in))

    @staticmethod
    def filter_odd_numbers(numbers_in):
        return list(filter(lambda x: x % 2 != 0, numbers_in))

class Config(metaclass=Singleton):
    __props = {}

    def load_properties(self, filepath):
        with open(filepath, "rt") as propfile:
            for line in propfile:
                string_line = line.strip()
                if string_line and not string_line.startswith('#'):
                    parts = string_line.split('=')
                    key = parts[0].strip()
                    value = '='.join(parts[1:]).strip().strip('"')
                    self.__props[key] = value
        return self.__props

    def getProperties(self):
        return self.__props


