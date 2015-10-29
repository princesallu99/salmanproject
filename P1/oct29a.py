__author__ = 'sjaved'

def add(num1, num2):
    num = num1 + num2
    print('sum is' , num)

add(3,4)


def add(num1, num2):
    num = num1 +num2
    return num

ans = add(3,4)
print('Twice the sum is', ans *2)


def add(arg1, arg2):
    return arg1 + arg2

num1 =3
num2 = 4
print('Twice the sum is', add(num1, num2) * 2)