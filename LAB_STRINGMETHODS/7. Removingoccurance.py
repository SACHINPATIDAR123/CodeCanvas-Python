#Q7.Write a Python function that removes all occurrences of a specified
#character from a string.

# Original text
text = "Hello world"

# Character to remove
remove = "o"

# Remove all occurrences of char_to_remove from text
result = text.replace(remove, '')

# Print the resulting string
print("Result:", result)
