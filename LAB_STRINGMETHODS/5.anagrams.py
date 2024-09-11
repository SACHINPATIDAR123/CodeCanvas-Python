#Q5. Write a Python function that checks if two given strings are
#anagrams (contain the same characters with the same frequencies).

# Input strings
str1 = "   Listen   "
str2 = "Silent"

# Remove leading and trailing whitespace, convert to lowercase,
#and remove spaces

str1 = str1.strip().replace(" ", "").lower()
str2 = str2.strip().replace(" ", "").lower()

# Check if the sorted characters of both strings are the same
if sorted(str1) == sorted(str2):
    print(f"Do '{str1}' and '{str2}' have the same characters with the same frequencies? Yes")
else:
    print(f"Do '{str1}' and '{str2}' have the same characters with the same frequencies? No")

