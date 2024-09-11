#Q10. Write a Python function to find the length of the longest substring in a
#given string that contains no repeating characters.

# enter any  string to perform operation
text = "abcabcbb"

#Set to keep track of unique characters in the current window
char_set = set()

#Initializing pointers and variable to store the maximum length of substring
left = 0
max_length = 0

# Iterate through each character in the string using the right pointer

for right in range(len(text)):

# If the current character is already in the set, 
# move the left pointer to the right to remove characters until no duplicate is found

    while text[right] in char_set:
        char_set.remove(text[left])
        left += 1
# Add the current character to the set

    char_set.add(text[right])

# Update the maximum length found

    max_length = max(max_length, right - left + 1)

# Print the length of the longest substring with a condition of no repeating characters

print(max_length)  

