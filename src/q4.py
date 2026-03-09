def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """

    # Check if s is a string
    if not isinstance(s, str):
        return -1


    # Create a temp variable to extract and store the reversed, using a for loop
    # For loop is as such where the last char is of n-1 index, and we stop at -1 to include 0th index, and -1 step: backwards
    reversed_s = ""
    for i in range(len(s)-1, -1, -1)
        reversed_s += s[i]
    
    return reversed_s


# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

string_reverse("Hello World")
string_reverse("Python")
