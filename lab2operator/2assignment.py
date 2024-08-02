# Q2. Write a program for Assignment Operators.

"""
Assignment Operators are used to assign values to the variables.
They can also perform operations and then assign the result to a variable.
Assignment Operators are as follows:
"""

# Assignment (=) : (a=value)
num1 = 40
print("Assign:",num1)

# Add Assignment (+=) : (a+=b => a=a+b)
num1 = 20
num2 = 5
num1 += num2
print("Add Assign:",num1)

# Subtract Assignment (-=) : (a-=b => a=a-b)
num1 = 25
num2 = 15
num1 -= num2
print("Subtract Assign:",num1)

# Multiply Assignment (*=) : (a*=b => a=a*b)
num1 = 78
num2 = 45
num1 *= num2
print("Multiply Assign:",num1)

# Divide Assignment (/=) : (a/=b => a=a/b)
num1 = 986
num2 = 35
num1 /= num2
print("Divide Assign:",num1)

# Modulus Assignment (%=) : (a%=b => a=a%b)
num1 = 25
num2 = 3
num1 %= num2
print("Modulus Assign:",num1)

# Exponent Assignment (**=) : (a**=b => a=a**b)
num1 = 698
num2 = 5
num1 **= num2
print("Exponent Assign:",num1)

# Floor Divide Assignment (//=) : (a//=b => a=a//b)
num1 = 986
num2 = 35
num1 //= num2
print("Floor Divide Assign:",num1)

# Bitwise AND Assignment (&=) : (a&=b => a=a&b)
num1 = 10
num2 = 8
num1 &= num2
print("AND Assign:",num1)

# Bitwise OR Assignment (|=) : (a|=b => a=a|b)
num1 = 10
num2 = 8
num1 |= num2
print("OR Assign:",num1)

# Bitwise XOR Assignment (^=) : (a^=b => a=a^b)
num1 = 10
num2 = 8
num1 ^= num2
print("XOR Assign:",num1)

# Bitwise Right Shift Assignment (>>=) : (a>>=n => a=a>>n)
num1 = 12
shiftPosition = 2
num1 >>= shiftPosition
print("Right Shift Assign:",num1)

# Bitwise Left Shift Assignment (<<=) : (a<<=n => a=a<<n)
num1 = 10
shiftPosition = 2
num1 <<= shiftPosition
print("Left Shift Assign:",num1)