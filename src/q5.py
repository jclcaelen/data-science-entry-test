def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """

    # Unlike q1.py, where we just check if the given variable can be typecast to float, we use isinstance here to check if it is an integer or float.
    # https://stackoverflow.com/questions/33311258/python-check-if-variable-isinstance-of-any-type-in-list, shows we can use a tuple for multiple types
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))):
        return -1


    # Check if divisible, return true if yes, and false if no. we use modular %, where 0 means divisible.
    # However, if divisor is given as 0, we need to flag the error
    if divisor == 0:
        print("Error: Division by 0")
        return -1

    if num % divisor == 0:
        return True
    else:
        return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

check_divisibility(10, 2)
check_divisibility(7, 3)


# Validated using Jupyter Notebook IDE.
