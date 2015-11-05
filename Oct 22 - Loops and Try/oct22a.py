__author__ = 'PrinceSallu'

done = False

# Loop until the "done" flag becomes true
while not done:
    try:
        reply = int(input("Enter a integer, zero when done: "))
        if reply != 0:
            print("Your input doubled is", reply * 2)
        else:
            done = True
    except:
        print("You did not enter an integer")

print("All done")

