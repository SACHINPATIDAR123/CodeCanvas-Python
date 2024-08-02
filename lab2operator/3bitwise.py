# Q3. Write a program for Bitwise Operators.

"""
Bitwise Operator are used to perform bit-level operations on integer values.
Bitwise Operators are as follows:
"""

# Bitwise NOT Operator (~) : Performs a bitwise NOT operation, inverting each bit of an integer.
num1 = 6  # In binary: 0110
notOperator = ~num1
print("Bitwise NOT Operator:",notOperator)

# Bitwise AND Operator (&) : Performs a bitwise AND operation on each pair of corresponding bits of two integers.
num1 = 15  # In binary: 1111
num2 = 10  # In binary: 1010
andOperator = num1 & num2
print("Bitwise AND Operator:",andOperator)  # 1010 = 10

# Bitwise OR Operator (|) : Performs a bitwise OR operation on each pair of corresponding bits of two integers.
num1 = 3   # In binary: 0011
num2 = 12  # In binary: 1100
orOperator = num1 | num2
print("Bitwise OR Operator:",orOperator)  # 1111 = 15

# Bitwise XOR Operator (^) : Performs a bitwise XOR operation on each pair of corresponding bits of two integers.
num1 = 7  # In binary: 0111
num2 = 9  # In binary: 1001
xorOperator = num1 ^ num2
print("Bitwise XOR Operator:",xorOperator)  # 1110 = 14

# Bitwise Right Shift Operator (>>) : Shifts the bits of the first operand to the right by the number of positions specified by the second operand, discarding the bits shifted off.
num1 = 12  # In binary: 1100
shiftPosition = 2  # Number of position to shift: 2
rightShiftOperator = num1 >> shiftPosition
print("Bitwise Right Shift Operator:",rightShiftOperator)  # 11 = 3

# Bitwise Left Shift Operator (<<) : Shifts the bits of the first operand to the left by the number of positions specified by the second operand, filling the new bits with 0s.
num1 = 12  # In binary: 1100
shiftPosition = 2  # Number of position to shift: 2
leftShiftOperator = num1 << shiftPosition
print("Bitwise Left Shift Operator:",leftShiftOperator)  # 110000 = 48