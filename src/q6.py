def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """

    # while not requested, we just handle if argument passed is not a list
    if not isinstance(lst, list):
        return -1


    # initialise, to prevent any previously stored value assigned in memory
    i = 0

    # Using a while loop
    while i < len(lst):
        if lst[i] < 0:
            return lst[i]
        i += 1                # increase counter/index

    # if none found (completion of the loop and nothing returned)
    return "No negatives"


# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

find_first_negative([3, 5, -1, 7, -2, 8])
find_first_negative([2, 10, 7, 0])
