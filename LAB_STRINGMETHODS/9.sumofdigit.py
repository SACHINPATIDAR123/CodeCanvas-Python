#Q9. Write a Python function that takes a digits and characters string and
#return a sum of digits in the string.’

str1 = "Hello World 2345"
sumNum = 0

# Iterate through each character in the string
for x in str1:
    # Check if the character is a digit

    if x.isdigit():
        # to Convert the digit character to an integer

        z = int(x)
        # Add the integer value to the sum

        sumNum += z

# Print the result
print(sumNum)
