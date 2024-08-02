# Q4. Write a program to calculate greatest of three numbers.

# Used float as input so that user can give input as integer and float both.
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
num3 = float(input("Enter third number:"))


# Using Operators:
greatest = (num1 * (num1>num2 and num1>num3)+   # This part will evaluate to 'num1' if num1 is greater than 'num2' and 'num3', otherwise return '0'.
            num2 * (num2>num1 and num2>num3)+   # This part will evaluate to 'num2' if num1 is greater than 'num1' and 'num3', otherwise return '0'.
            num3 * (num3>num1 and num3>num2))   # This part will evaluate to 'num3' if num1 is greater than 'num1' and 'num2', otherwise return '0'.
                                                # The correct value (greatest) will be non zero, while others will be '0'. Adding these gives the greatest number.
print("The greatest of three numbers is", greatest)

# OR

# Using if-elif statement:
if num1>num2 and num1>num3:
    print("First number is greatest:", num1)
elif num2>num3 and num2>num1:
    print("Second number is greatest:", num2)
else:
    print("Third number is greatest:", num3)


