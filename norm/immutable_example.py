class Immutable:
    def __init__(self, var1, var2):
        super().__setattr__('_var1', var1)
        super().__setattr__('_var2', var2)

    def __setattr__(self, key, value):
        raise TypeError('MyImmutable cannot be modified after instantiation')

    def __str__(self):
        return 'MyImmutable var1: {}, var2: {}'.format(self._var1, self._var2)


i = Immutable("val1", "val2")
print(str(i))
# i.var1 = "change"


