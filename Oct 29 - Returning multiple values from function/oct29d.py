__author__ = 'PrinceSallu'

# Note this function uses a conditional expression
# and returns a list
def min_max(arg1, arg2):
    return [arg1, arg2] if arg1 < arg2 else [arg1, arg2]

num1 = 12
num2 = 5

# Note two values are passed to the function and two values are returned
smaller, larger = min_max(num1, num2)
print('smaller=', smaller, "larger=", larger)

