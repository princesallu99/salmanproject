__author__ = 'sjaved'

#!/usr/local/bin/python3

# The output of the two print statements will appear on the same line
# with a space between the two strings
print ('Life is good',end=" ")
print ('now that we are using python\n')

# Try to do the section below.
# If there is an error, go to the "except" section below
try:
    # Get a reply after prompting the user and converting to an integer
    reply = int (input ("Enter an integer between 78 and 85: "))

    # Check if the reply is within a range
    if (78 <= reply <= 85):
        # Execute this if true
        print ("You got it right")
        print ("Congrats")
    else:
        # Execute this if false
        print ("You got it wrong")
        print ("Too bad")

except:
    # If there are any errors, do the code below
    print ('You did not enter an integer')