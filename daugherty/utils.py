__author__ = 'Norm Vilmer'
__project__ = 'LunchAndLearnDec2018'

class Singleton(type):
    __instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.__instances[cls]

class Utils(metaclass=Singleton):
    def evenNumbers(self, numbersIn):
        return list(filter(lambda x: x % 2 == 0, numbersIn))

