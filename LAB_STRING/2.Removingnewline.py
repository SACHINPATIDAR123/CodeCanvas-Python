#Q2. Write a Python program to remove a newline in Python

#String = "\nBest \nDeeptech \nPython \nTraining\n"

# string with \n
string ="\nBest \nDeeptech \nPython \nTraining\n"

# Remove leading and trailing whitespace characters using strip
cleaned = string.strip()

singleline = cleaned.replace("\n", " ")

# Print the cleaned string
print("Cleaned:", singleline)
