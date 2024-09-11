#Q2.Write a function in Python to count and display the total number of words
#in a text file “ABC.txt”

def countwords():
    filename = "ABC.txt"

# Initialize the count for words to zero
    word_count = 0

# Open the file in read mode
    with open(filename, "r") as file:
# Read each line one by one
        for line in file:
# Split the line into words and count them
            word_count += len(line.split())

# Print the total number of words in the file
    print(f"The number of words present in the file '{filename}' is: {word_count}")

# Call the function to execute the word count
countwords()

