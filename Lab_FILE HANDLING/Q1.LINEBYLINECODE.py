#Q1.Write a function in python to read the content from a text file "ABC.txt" line
#by line and display the same on screen.

def readContent():
    filename = "ABC.txt"

# Open will Open the filein console and read its content line by line
    with open(filename, "r") as file:
         for line in file:

# we use end='' to avoids adding extra newlines
            print(line, end='')  

readContent()  


