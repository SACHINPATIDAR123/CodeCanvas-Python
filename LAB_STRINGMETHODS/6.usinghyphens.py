#Q6. .Write a Python function that splits a string into a list of words and then joins the list back into a

#single string with hyphens (-) between the words.

#FEEDING INPUT
text = "Hello world"

# By - we can Split the string into words and join with hyphens

result = '-'.join(text.split())

# Print the resulting string
print(result)

#return type of join is string
