#Question.1 Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.

#here define the div function will takes two parameter
def div(value1,value2):
    
    # Return the result of dividing value1 by value2
    return value1/value2

# here call the div function with two arguments 25 and 5
output=div(25,5)

# print the output of the division
print("The output of the division is",output)



#Question 2.Declare a square() function with one parameter.Then call the function and pass one number anddisplay the square of that ndef square(value): # we declare the square function with one parameter
    
# here define the square function with takes one parameter
def square(value):
    
# Return the square of 'value' by raising it to the power of 2
    return value ** 2

# here Call the 'square' function with the argument 8 
output = square(8)

# print the square of number
print("the square of number is ",output)



#Queston.3  Using max() and min() functions display the maximum and minimum of 5 random numbers.

# here import the random module to list of random numbers
import random

# here Create a list of 5 unique random numbers between 1 and 99 
numbers = random.sample(range(1,100), 5) 

#  here Print the list of 5 random  numbers
print("numbers:", numbers)

#  here Find and print the maximum number in the list
print("maximum:", max(numbers))

#  here Find and print the minimum number in the list
print("minimum:", min(numbers))



#Question.4  Accept a name from the user and display that in lower case using lower() function

# here Get the user's name
name = input("Enter the name: ")

#  here Change the name to lowercase
lowercasename = name.lower()

# here print name in lowercase
print("The name in lowercase is", lowercasename)



