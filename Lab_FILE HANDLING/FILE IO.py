# 1. input() : Takes input from user (Takes input from the console)
def greet(name):
    print(f"Hello, {name}!!")

name = input("Enter your name: ")
greet(name)

# 2. print() : Prints output to the console
def string():
    print("This is a print statement")

string()

# 3. open() : Opens file
def fileOpen():
    # Open file in write mode and write text to it
    with open("example.txt", "w") as file:
        file.write("First line of the file.\nSecond line of the file")

fileOpen()

# 4. read() : Reads content of a file
def read():
    with open("example.txt", "r") as file:
        content = file.read()
        print("Content read using read():")
        print(content)

read()

# 5. readline() : Reads one line from a file
def readline():
    with open("example.txt", "r") as file:
        line = file.readline()
        print("First line read using readline():")
        print(line)

readline()

# 6. readlines() : Reads all lines from a file
def readlines():
    with open("example.txt", "r") as file:
        lines = file.readlines()
        print("Lines read using readlines():")
        print(lines)

readlines()

# 7. write() : Writes to a file in append mode
def write():
    with open("example.txt", "a") as file:  # 'a' for append mode
        file.write("\nThird line appended to the file.")

write()

# 8. writelines() : Writes a list of lines to a file
def writelines():
    lines_to_write = ["Fourth line.\n", "Fifth line.\n"]
    with open("example.txt", "a") as file:
        file.writelines(lines_to_write)

writelines()

# 9. close() : File close operation (corrected to show usage)
def close():
    with open("example.txt", "r") as file:
        print("Content before closing the file:")
        print(file.read())
    # File is automatically closed after the block ends
    # Trying to read here would raise an error if uncommented
    # print(file.read())  # This would raise an error

close()

# 10. flush() : Flushes the file buffer
def flush():
    with open("example.txt", "w") as file:
        file.write("This line will be written immediately.")
        file.flush()  # Forces the write to happen immediately

flush()

# 11. seek() and tell() : File cursor operations
def seekAndTell():
    with open("example.txt", "r") as file:
        print("Current file position:", file.tell())  # Outputs the position (should be 0)
        file.seek(10)  # Move to the 10th byte
        print("New file position after seek(10):", file.tell())

seekAndTell()

# 12. truncate() : Truncates the file to a specific size
def truncate():
    with open("example.txt", "r+") as file:  # 'r+' for read and write mode
        file.truncate(20)  # Truncate the file to 20 bytes

truncate()

# 13. with open() (context manager) : Simplified file handling
def open_file():
    with open("example.txt", "r") as file:
        content = file.read()
        print("Content read using with open():")
        print(content)

open_file()





