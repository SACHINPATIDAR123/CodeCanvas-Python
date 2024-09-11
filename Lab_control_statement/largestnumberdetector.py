
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

#we use float data type because the number provide by us is may be is in decimal.
#Determining the largest number

if number1 >= number2 and number1 >= number3:
    largest = number1
elif number2 >= number1 and number2 >= number3:
    largest = number2
else:
    largest = number3

#Printing the largest number
print("The largest number is:",largest)

"""It will give largest number out of three firstly
the code will check number1 then it will move to number2 then it will
move to number3"""

