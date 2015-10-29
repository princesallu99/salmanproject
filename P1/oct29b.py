__author__ = 'sjaved'

def min_max(arg1, arg2):
    if arg1>= arg2:
        return arg2, arg1
    else:
        return arg1, arg2

smaller, larger = min_max(12, 5)
print('smaller=', smaller, "larger=", larger)