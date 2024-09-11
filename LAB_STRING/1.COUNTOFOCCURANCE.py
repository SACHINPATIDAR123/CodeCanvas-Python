#1. Write a Python program to count the occurrences of each word in a
#given sentence

# FEED INPUT HERE
string = input("Enter string: ")
word = input("Enter word: ")

# Start count
count = 0

# breaaking into words
a = string.split(" ")

# Counting occurrences of the word
for i in range(len(a)):
    if word == a[i]:
        count += 1

# result
print("Count of the word is:")
print(count)
