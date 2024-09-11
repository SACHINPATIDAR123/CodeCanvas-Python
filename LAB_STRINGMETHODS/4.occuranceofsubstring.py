#4Write a Python function to find all the occurrences of a substring in
#a given string.

# Original string
s = "abracadabra"

# Substring to find
substring = "abra"

# Find all occurrences of the substring in the string
start = 0
occurrences = []

while True:
    start = s.find(substring, start)
    if start == -1:
        break
    occurrences.append(start)
    start += len(substring)  # Move past the current occurrence

# Print all occurrences of the substring
print(f"Occurrences of '{substring}' in '{s}':", occurrences)
