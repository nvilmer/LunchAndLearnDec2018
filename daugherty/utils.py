__author__ = 'Norm Vilmer'
__project__ = 'LunchAndLearnDec2018'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

        return cls._instances[cls]


class Utils(metaclass=Singleton):
    @staticmethod
    def even(numbers_in):
        return list(filter(lambda x: x % 2 == 0, numbers_in))

