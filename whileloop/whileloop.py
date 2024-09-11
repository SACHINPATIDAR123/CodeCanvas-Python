#Question.1 Write a python program to reverse a number using a while loop.

# here define reversenumber function
def reversenumber(number):
    # here Store the original number to print later
    originalnumber = number
    #  here Initialize the reversed number as 0
    reverse = 0
 
    # Loop until the number becomes 0
    while number > 0:
        # Get the last digit of the number
        digit = number % 10
        # Add the digit to the reversed number, shifting it to the left
        reverse = reverse * 10 + digit
        # Remove the last digit from the number
        number //= 10
 
    # Print the original number
    print(f"Original Number: {originalnumber}")
    # Print the reversed number
    print(f"Reversed Number: {reverse}")
 
# Test the function with the number 4567
reverse = 4567
reversenumber(reverse)


#Question.2 Write a python program to check whether a number is palindrome or not?

# here define a palindrome function
def palindrome(number):
    # here Store the original number to compare later
    originalnumber = number
    # here Initialize the reversed number to 0
    reversednumber = 0

    # here Reverse the digits of the number
    while number > 0:
        #here Get the last digit of the number
        digit = number % 10
        # here Add it to the reversed number (shift digits left)
        reversednumber = reversednumber * 10 + digit
        # here Remove the last digit from the number
        number //= 10

    # here Compare the original number with the reversed number
    return originalnumber == reversednumber

# here test the number is palindrome or not 
number = 343
if palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")


#Question.3 Write a python program finding the factorial of a given number using a while loop.
    
# here Set the value 7  to calculate the factorial
value = 7
# here Start with 1 (the initial value of factorial)

factorial = 1

# Use a while loop to calculate the factorial
while value > 0:
    # Multiply the current factorial by the current value
    factorial = factorial * value
    # Decrease the value by 1
    value = value - 1

# Print and show the factorial
print("Factorial:", factorial)



#Question.4 Accept numbers using input() function until the user enters 0.If user input 0 then break the while loop
#and display the sum of all the numbers.

# Initialize a variable to store the sum of numbers
totalsum = 0

# Use a while loop to accept numbers until user enters 0
while True:
    # Accept a number from the user
    num = int(input("Enter a number (0 to stop): "))

    if num == 0:     
# Check if the user wants to stop    
        break
    
# Add the number to the total sum
    totalsum += num
# Accept a number from the user
print("Sum of all numbers:", totalsum)




