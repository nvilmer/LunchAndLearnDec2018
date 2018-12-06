

# Unlike Java, it is not necessary to define classes in Python, but if you do
# you can declare and initialize members in __init__
class ScopeExampleClass(object):
    def __init__(self):
        self._taskCount = 0
        self.__completedTaskCount = 0
        self.isWorking = False

    def updateState(self):
        # no need for parenthesis here
        self.isWorking = self._taskCount > 0 and self._taskCount != self.__completedTaskCount

    def completeTask(self):
        # :( - I miss ++
        self.__completedTaskCount += 1
        self.updateState()

    def addTask(self):
        self._taskCount += 1
        self.updateState()


obj = ScopeExampleClass()
print("Initial isWorking: " + str(obj.isWorking))
obj.addTask()
print("After addTask() isWorking: " + str(obj.isWorking))
obj.completeTask()
print("After completeTask() isWorking: " + str(obj.isWorking))
print("taskCount: " + str(obj._taskCount))

