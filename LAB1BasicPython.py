#Q1. PRINT HELLO WORLD

print("Hello, World!") #OUTPUT OF THIS CODE WILL BE HELLO, WORLD!



#Q.2 Describe Local Variable and Global Variable Code

"""Definition: Local variables are declared within a specific function or
block of code and are only accessible within that function or block.
Scope: Limited to the function or block where they are declared.
Once the function or block execution is completed, the local variable is destroyed.
Lifetime: Exists only during the execution of the function or block.
It is created when the function is called and destroyed when the function exits."""

"""Definition: Global variables are declared outside of all functions or blocks
and can be accessed from any part of the code, including inside functions.
Scope: Global scope, meaning they are accessible throughout the entire program.
Lifetime: Exists for the duration of the program's execution, from the time it starts until it end"""

# Global variable
global_var = "I am a global variable"

def example_function():
    # Local variable
    local_var = "I am a local variable"
    print(local_var)          # This will print the local variable
    print(global_var)         # This will print the global variable


# if we Try to access local_var outside the function it will result in an error
# print(local_var)  # Uncommenting this will raise a NameError


#Q.3 Write a code that describe Indentation error.


""" print("This line is correctly indented")

if True:
print("This line will cause an indentation error")""" #this line cause an indenatation error


#Q.4 Write a Code That Describes Local and Global Variables with the Same Name.


# Global variable
A = 10

print("Global A:", A) # This will Print the global variable

A = 20
print("Local A:", A) # This will print Local variable with the same name.

# Change the local variable
A = 30
print("Updated local A:", A)




#Q.5 Write a Code for String, Int, and Float Input


intro= "Python was created by Guido van Rossum in the year," #this will return to an string with ouput Python was created by Guido van Rossum in the year,
print(type(intro))#this is used to define the data type and will return to string as above data is string tpye data type.
print(intro)
year= 1989 #this will return to the  int type data
print(type(year)) #this is used to define the data type and will return to int as above data is string int data type.
print(year)
string="first version introduced was"
print(string)
version= 0.90 #this will return to the float type data
print(type(version)) #this is used to define the data type and will return to float as above data is float type data.
print(version)







