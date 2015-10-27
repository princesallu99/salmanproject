__author__ = 'sjaved'

try:
    reply = -1
    while reply != 0:
        reply = int(input("Enter two positive integer, zero when done: "))
        print("Your input doubled is", reply*2)
except:
        print('You did not enter an integer')