#1. Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve”

s = "P@#yn26at^&i5ve"  # The is our input string

# it will Count the number of letters (a-z, A-Z) in the string in both cases

letters = sum(c.isalpha() for c in s)

# Count the number of digits (0-9) in the string

digits = sum(c.isdigit() for c in s)

"""Count the number of special symbols by subtracting
letters and digits from the total length"""
specials = len(s) - letters - digits

# Print the counts of letters, digits, and special symbols
print(f"Letters: {letters}, Digits: {digits}, Specials: {specials}")
