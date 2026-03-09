def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    # We check if the variables given are numeric. Assumption is if numbers are given in the form of strings, we will convert them first. Unable to change them to float as they will get the new datatype.
    try:
        float(x)
        float(y)
    except:
        return -1

    # if passes the above, we perform the swap and print out the swapped values
    temp = x
    x = y
    y = x

    print(f"New x is now {y}, and new y is now {x}")


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17


swap("Apple", 10)
swap(9, 17)
