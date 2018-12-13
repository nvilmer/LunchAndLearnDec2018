#!/c/Python37/python

import shutil
import tempfile
# map and filter don't require import, but reduce does
from functools import reduce
from os import path

from daugherty.class_example import TaskCounter
from daugherty.function_example import *
from daugherty.utils import *
from norm.site_package_lister import *


def run_site_package_lister():
    print_sys_path()
    print_packages()


def run_class_example():
    task_counter = TaskCounter()
    print("Counter isWorking: " + str(task_counter.isWorking))
    task_counter.add_task()
    print("After addTask() isWorking: " + str(task_counter.isWorking))
    task_counter.complete_task()
    print("After completeTask() isWorking: " + str(task_counter.isWorking))
    print("taskCount: " + str(task_counter._taskCount))


def run_function_example():
    print('numbers: ' + str(numbers))
    print('more_numbers: ' + str(more_numbers))
    print('big_numbers: ' + str(big_numbers))
    print('negative_numbers: ' + str(negative_numbers))
    print('decimal_numbers: ' + str(decimal_numbers))

    # Python lambdas are single line, no statement and cannot control
    print('anonymous example: ' + str(list(filter(lambda x: x % 3 == 0, numbers))))

    # Python support map, filter, reduce
    # Remember to convert map to list before printing
    print('integers of decimal_numbers: ' + str(list(map(integer, decimal_numbers))))
    print('adder of numbers in each list by position: '
          + str(list(map(adder, numbers, more_numbers, big_numbers, negative_numbers, decimal_numbers))))


def run_utils():
    # Filtering is easy
    print('Even numbers: ' + str(Utils.filter_even_numbers(numbers)))
    print('Even more_numbers: ' + str(Utils.filter_even_numbers(more_numbers)))
    print('Even big_numbers: ' + str(Utils.filter_even_numbers(big_numbers)))
    print('Even negative_numbers: ' + str(Utils.filter_even_numbers(negative_numbers)))
    print('Even integer values of decimal_numbers: '
          + str(Utils.filter_even_numbers(map(integer, decimal_numbers))))

    # reduce works as expected
    print('adder of numbers (reduce): ' + str(reduce(lambda x, y: x * y, numbers)))

    # Combining lambdas is straight forward
    print(list(Utils.filter_even_numbers(numbers)))


def run_config():
    test_dir = tempfile.mkdtemp()
    with open(path.join(test_dir, 'config.properties'), 'w') as config_file:
        config_file.write('# Test config.properties\n')
        config_file.write('user.name=bob\n')
        config_file.write('user.location=dallas\n')

    config = Config()
    config.load_properties(test_dir + '/config.properties')
    print(list(config.getProperties()))
    shutil.rmtree(test_dir)


if __name__ == '__main__':
    run_site_package_lister()
    run_class_example()
    run_function_example()
    run_utils()
    run_config()
