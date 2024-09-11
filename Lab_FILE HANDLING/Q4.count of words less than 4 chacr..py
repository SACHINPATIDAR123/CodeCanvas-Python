#Q4.Write a function display_words() in python to read lines from a text
#file "story.txt", and display those words, which are less than 4 characters.

def display_words(filename):
    short_words = []

    with open(filename, "r") as file:
        for line in file:
            for word in line.split():
                if len(word) < 4:
                    short_words.append(word)

 # To print the words less than 4 char. into a single paragraph and print it

    print(" ".join(short_words))
# Print the total number of short words

    print(f"\nTotal number of short words (which are less than 4 characters): {len(short_words)}")

# To Call the function with the file name

display_words("story.txt")
