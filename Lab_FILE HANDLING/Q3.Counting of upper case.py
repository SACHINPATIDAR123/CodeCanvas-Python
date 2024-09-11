#3. Write a function in Python to count uppercase character in a text
#file “ABC.txt
def countuppercase():
# Name of the file to read
    filename = "ABC.txt"

# Initialize a counter to keep track of uppercase letters
    uppercase_count = 0

# Open the file in read mode
    with open(filename, "r") as file:
# Go through each line in the file
        for line in file:
# Go through each character in the current line
            for char in line:
# Check if the character is an uppercase letter
                if char.isupper():
# If it is an uppercase letter, increase the count by 1
                    uppercase_count += 1

# Print the total number of uppercase characters found in the file
    print(f"Total number of uppercase characters in the file '{filename}' are: {uppercase_count}")

# Call the function to execute the uppercase counting
countuppercase()
