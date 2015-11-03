__author__ = 'PrinceSallu'

#!/usr/local/bin/python3
# The line above makes sure the script executes in Python 3

# The output of the two print statements will appear on the same line
# with a space between the two strings
print ('Life is good',end=" ")
print ('now that we are using python\n')

# Get a reply after prompting the user and converting to an integer
reply = int (input ("Enter an integer between 78 and 85: "))

# Check if the reply is within a range
# Note the ":" after "if" and "else" and the consistent indentation
# Note this comparison method is unique to python
if (78 <= reply <= 85):
    # Execute this if true
    print ("You got it right")
    print ("Congrats")
else:
    # Execute this if false
    print ("You got it wrong")
    print ("Too bad")
