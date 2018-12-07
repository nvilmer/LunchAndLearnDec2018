

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
