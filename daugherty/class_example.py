from abc import ABC, abstractmethod


# Unlike Java, it is not necessary to define classes in Python, but if you do
# you can declare and initialize members in __init__
class TaskCounter(object):
    def __init__(self):
        self._taskCount = 0
        self.__completedTaskCount = 0
        self.isWorking = False

    def update(self):
        # no need for parenthesis here
        self.isWorking = self._taskCount > 0 and self._taskCount != self.__completedTaskCount

    def complete_task(self):
        # :( - I miss ++
        self.__completedTaskCount += 1
        self.update()

    def add_task(self):
        self._taskCount += 1
        self.update()


# In Python, you use the ABC library to do abstract classes
# There are no interfaces because multiple inheritance exists (be careful)
class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self, data):
        pass


class MyConcreateClass(MyAbstractClass):
    def my_abstract_method(self, data):
        return 'data: ' + data


# will fail to instanciate abstract class
# test = MyAbstractClass()
test = MyConcreateClass()
print(test.my_abstract_method("some data"))
