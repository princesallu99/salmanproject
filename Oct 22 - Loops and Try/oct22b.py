__author__ = 'PrinceSallu'

done = False

while not done:
    try:
        # Ask for two integers and put the results in two variables
        reply1, reply2 = input('Enter two integers, two zeros when done: ').split()

        # Try to cast each reply into two int variables
        # Note this might fail
        int1, int2 = [int(reply1), int(reply2)]

        # If the line above succeeds, check if both variables are zero
        if int1 == 0 and int2 == 0:
            # We're done
            done = True
        else:
            # Print the results and do again
            print("The sum of your inputs =", int1 + int2)
    except ValueError:
        # Do this if anything above fails
        print("You did not enter two integers")

print("All done")