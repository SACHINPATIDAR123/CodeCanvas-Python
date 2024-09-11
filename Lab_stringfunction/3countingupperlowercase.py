#3. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
#Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”  

# This is given input string
input_string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"  

# Initialising the counters for uppercase letters, lowercase letters, numeric digits, and special characters

uppercase_count = lowercase_count = numeric_count = special_count = 0

# iterate through each character in the input string
for char in input_string:
    if char.isupper():
        uppercase_count += 1  # to Count uppercase letters
    elif char.islower():
        lowercase_count += 1  # for Counting lowercase letters
    elif char.isdigit():
        numeric_count += 1  # for Counting numeric digits
    elif not char.isspace():
        special_count += 1  # to Count special characters

# Print the counts of each category
print(f"UpperCase : {uppercase_count}")
print(f"LowerCase : {lowercase_count}")
print(f"NumberCase : {numeric_count}")
print(f"SpecialCase : {special_count}")
