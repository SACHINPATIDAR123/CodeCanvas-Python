#4. Write a Python Count vowels in a string 
#input= “Welcome to Python Assignment” 

# This is our input string

input_string = "Welcome to Python Assignment"  

# Defining given vowels

vowels = "aeiouAEIOU"

# Count the vowels in the input string
vowel_count = sum(1 for char in input_string if char in vowels)

# Print the total number of vowels
print(f"Total vowels are: {vowel_count}")
