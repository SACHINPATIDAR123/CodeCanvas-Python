"""1. Using input() function take one number from the user and
using ternary operators check whether the number is even or odd """

print("#1 Enter your number to detect whether the number is even or odd.")
# we have to enter number as interger
number = int(input("Enter a number: "))

# it will check whether the number is even or odd.
#here  % 2 stands for divding the number by 2 to identify even or odd.

result="Even" if number % 2 == 0 else "Odd"

# Print the result
print(f"The given number is {result}.")




#2. Using input function take two number and then swap the number

print("#2 Give input of two numbers for swaping the numbers.")
# we have to enter two number for comparision and swaping
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# for Swaping the numbers we simply use
num1, num2 = num2, num1

# To Print the swapped numbers we can use print.

print(f"After swapping: First number = {num1}, Second number = {num2}")



#3. Write a Program to Convert Kilometers to Miles

print("#3 To change KM into MILES feed your input.")
# Give input for distance in kilometers
kilometers = float(input("Enter distance in kilometers: "))

# To Convert kilometers into miles we are using the conversion factor (0.621371)
miles = kilometers * 0.621371

# This will Print the result with two decimal places.
print(f"{kilometers} kilometers is equal to {miles:.2f} miles")

#The input() function allows the user to enter a distance in kilometers. float() converts this input from a string to a number.
#(kilometers * 0.621371) performs the conversion from kilometers to miles using the standard conversion 0.621371.
#print(f"...") print the resulted number in mile.I use 2f that print result upto two decimal places.



#4.Find the Simple Interest on Rs. 200 for 5 years at 5% per year.
print("#4 Simple Interets")
# GIVEN VARIABLES

principal = 200     # Principal amount (in IN Rs.)
rate = 5            # Rate of interest per year (in %)
time = 5            # Time in years(5)

#We can Calculate Simple Interest by, it is basic calculations that we used here.
simpleinterest = (principal * rate * time) / 100

# It will Print the result in rs.
print(f"The Simple Interest of Rs. 200 for 5 years, is Rs. {simpleinterest}")


