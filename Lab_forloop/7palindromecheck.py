#Question.7 Python program to check if the given string is a palindrome

# We have to Input a string

string = input("Enter a string to check if it is a palindrome: ")

# Check if the string is equal to its reverse(palindrome)
# If the original string is the same as the reversed string, it's a palindrome

if string == string[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

