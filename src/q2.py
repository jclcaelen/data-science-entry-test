def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """

    # Source: https://stackoverflow.com/questions/26544091/checking-if-type-list-in-python
    # Using isinstance() to check if first argument is a list
    if not isinstance(lst, list):
        return -1

    # Using a for loop to loop through lst, using range() to take X steps, using len() to determine X
    for i in range(len(lst)):
        if lst[i] == find_val:
            lst[i] = replace_val


    # Print after the replacement
    return lst


# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

find_and_replace([1, 2, 3, 4, 2, 2], 2, 5)
find_and_replace(["apple", "banana", "apple"], "apple", "orange")


# Validated using Jupyter Notebook IDE.
