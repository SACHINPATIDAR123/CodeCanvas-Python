#Q2. Write a Python function that checks
#if a given string is a palindrome (reads the same forward and backward).
# PLEASE FEED INPUT HERE

string = input("Enter a string to check if it is a palindrome: ")

# Check if the string is equal to its reverse (palindrome)
# If the original string is the same as the reversed string, it's a palindrome
if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

'''A palindrome is a word, phrase, number, or other sequence of characters that reads the
same forward and backward, ignoring spaces, punctuation, and capitalization.'''
