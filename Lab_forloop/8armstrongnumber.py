#Question.8 Python program to check if a given number is an Armstrong number

def is_armstrong(n):
#here initialize sum to store the total of digits raised to the power of the number of digits
    sum = 0
    
# Convert the number to a string to easily loop through its digits
    num_str = str(n)
    
# Loop through each digit in the string
    for char in num_str:
# Convert the digit back to an integer and raise it to the power of the number of digits

        sum += int(char) ** len(num_str)
    
# Check if the sum equals the original number
    return n == sum

# ask the user to enter a number
num = int(input("Enter a number: "))

# Check if the number is an Armstrong number

if is_armstrong(num):

# Print if it is an Armstrong number

    print(num, "is an Armstrong number.")
else:

# Print if it is not an Armstrong number

    print(num, "is not an Armstrong number.")
