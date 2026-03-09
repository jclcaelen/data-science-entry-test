def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """

    # Though not requested, will apply the same check that the dictionary is given to check
    if not isinstance(dct, dict):
        return -1

    # Check if key exists
    if key not in dct:
        print(f"Error: key '{key}' does not exist in the dictionary")
        return -1


    # Update the key with new value
    dct[key] = value


    # Print the updated dictionary
    print("Updated dictionary: ", dct)


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

update_dictionary({}, "name", "Alice")
update_dictionary({"age": 25}, "age", 26)


# Validated using Jupyter Notebook IDE.
