__author__ = 'PrinceSallu'

def main():

    try:
        # Prompt the user to enter a list of integers and store the results in a list
        my_list = [int(i) for i in input("Enter a list of integers: ").split()]

        # Use the function list_info to sort the list and return the min, max, and average values
        min_value, max_value, average_value = list_info(my_list)

        # Print the sorted list and the result
        print(len(my_list), "elements:", my_list)
        print("min =", min_value, "max =", max_value, "aver =", average_value)

    except ValueError:
        print("You entered nothing or something that was not an integer")


def list_info(arg):
    arg.sort()
    return min(arg), max(arg), sum(arg) / len(arg)

main()

