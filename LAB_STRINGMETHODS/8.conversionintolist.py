#8..Write a Python function that takes a string and returns a list of characters in the string.



def string_to_char_list(text):
    '''
    This function takes a string and returns a list of characters in the string.

    Parameters:
    text (str): The input string.

    Returns:
    list: A list of characters in the string.
    '''
    # Convert the string to a list of characters
    return list(text)

input_string = "hello"
char_list = string_to_char_list(input_string)
print("List of characters:", char_list)  


