import sys


def print_sys_path():
    print('sys.path:')
    print(*sys.path, sep='\n')


def print_packages():
    print('packages: ' + str(list(package for package in sys.path)))

