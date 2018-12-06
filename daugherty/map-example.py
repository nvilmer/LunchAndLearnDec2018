# map and filter don't require import, but reduce does
from functools import reduce

# Arrays are easy in Python :)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
more_numbers = [10, 12, 14, 16, 18, 20]
big_numbers = [11435600, 245000001, 365768256, 1000000, 500250]
negative_numbers = [-10, -45, -36, 98, -102]
decimal_numbers = [1.4, 8.2, -3.9, 100.2, 60.7, 11.0, 124.6]

# Remember to convert numbers to string before concatenating in Python
print('numbers: ' + str(numbers))
print('more_numbers: ' + str(more_numbers))
print('big_numbers: ' + str(big_numbers))
print('negative_numbers: ' + str(negative_numbers))
print('decimal_numbers: ' + str(decimal_numbers))


# Python functions that work as lambdas; PEP8 complains if you assign lambdas and prefers def
def adder(u, w, x, y, z): return u + w + x + y + z


def even(x): return x % 2 == 0


def integer(x): return int(x)


# Python lambdas are single line, no statement and cannot control
print('anonymous example: ' + str(list(filter(lambda x: x % 3 == 0, numbers))))

# Python support map, filter, reduce
# Remember to convert map to list before printing
print('integers of decimal_numbers: ' + str(list(map(integer, decimal_numbers))))
print('adder of numbers in each list by position: '
      + str(list(map(adder, numbers, more_numbers, big_numbers, negative_numbers, decimal_numbers))))

# Filtering is easy
print('Even numbers: ' + str(list(filter(even, numbers))))
print('Even more_numbers: ' + str(list(filter(even, more_numbers))))
print('Even big_numbers: ' + str(list(filter(even, big_numbers))))
print('Even negative_numbers: ' + str(list(filter(even, negative_numbers))))
print('Even integer values of decimal_numbers: '
      + str(list(filter(even, map(integer, decimal_numbers)))))

# reduce works as expected
print('adder of numbers (reduce): ' + str(reduce(lambda x, y: x * y, numbers)))

# Combining lambdas is straight forward
# Here is how you do split statement across lines
print('sum of all even numbers: ' + str(list(map(adder, list(filter(even, numbers)), list(filter(even, more_numbers)),
                                                 list(filter(even, big_numbers)), list(filter(even, negative_numbers)),
                                                 list(filter(even, map(integer, decimal_numbers)))))))
