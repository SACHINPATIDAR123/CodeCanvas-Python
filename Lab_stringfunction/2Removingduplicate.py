#2. Write a Python program to remove duplicate characters of a given string.
#Input = “String and String Function” 

string = "String and String Function"  # The input string

'''we have to Split the string into words,and then remove duplicates while keeping the 
ordern and rejoin them back into a single string'''

result = ' '.join(dict.fromkeys(string.split()))

print("String after removing duplicate words:", result)

