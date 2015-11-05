__author__ = 'PrinceSallu'

# Note this function has two return statements
# Note each return statement returns two values
def min_max(arg1, arg2):
    if arg1 >= arg2:
        return arg2, arg1
    else:
        return arg1, arg2

num1 = 12
num2 = 5

# Note two values are passed to the function and two values are returned
smaller, larger = min_max(num1, num2)
print('smaller=', smaller, "larger=", larger)
