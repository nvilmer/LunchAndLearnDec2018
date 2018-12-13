# Arrays are easy in Python :
# tuples are immutable ()'s lists are mutable []'s
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
more_numbers = (10, 12, 14, 16, 18, 20)
big_numbers = [11435600, 245000001, 365768256, 1000000, 500250]
negative_numbers = [-10, -45, -36, 98, -102]
decimal_numbers = [1.4, 8.2, -3.9, 100.2, 60.7, 11.0, 124.6]


# Python functions that work as lambdas; PEP8 complains if you assign lambdas and prefers def
def adder(u, w, x, y, z): return u + w + x + y + z


# Simple function example
def integer(x): return int(x)


def my_func():
    def my_internal_func(y):
        return y+1
    return my_internal_func


using_my_func = my_func()
print(using_my_func(3))
print('###############')


# Iterator and Generator examples
def create_iterator(y):
    return [x*x for x in range(y)]


def create_generator(y):
    my_iter = create_iterator(y)
    for k in my_iter:
        yield k*k


my_iterator = create_iterator(5)
for i in my_iterator:
    print(i)

print('*****************')

for i in my_iterator:
    print(i)

print('*****************')

my_generator = create_generator(10)
for i in my_generator:
    print(i)

print('*****************')

for i in my_generator:
    print(i)
