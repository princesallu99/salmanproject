__author__ = 'PrinceSallu'

# Note this function returns one argument
def add(arg1, arg2):
    return arg1 + arg2

num1 = 3
num2 = 4
# Note the function is called within a "print" statement
# Note the parameters are passed to the arguments based on keyword argument
print('Twice the sum is', add(arg2=num1, arg1=num2) * 2)