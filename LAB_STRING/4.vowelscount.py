#4.Write a Python program to count and display the vowels of a given text

#String=”Welcome to python Training”

# Take user input
text = input("Enter your string: ")

# Initiate a counter for vowels from 0
vowel_count = 0

# Define the set of vowels
vowels = 'aeiouAEIOU' #USING BOTH UPPER AND LOWER CASE

# for iterating through each character in the string
for char in text:

 # Check if the character is a vowel

 if char in vowels:
  vowel_count += 1

# Display the count of vowels

print("Number of vowels:", vowel_count)

'''I first tried by giving lower case but when i feed a string with upper
case it does not count string conatning vowels in upper case so i changes code'''
