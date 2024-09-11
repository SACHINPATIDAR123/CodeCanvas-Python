#2.Function with Parameter:

#2.1  How do you define a function that takes parameters.

#Function with Parameters
"""A function with parameters is a function that takes one or more inputs,
called parameters, which are used within the function to perform its task.
Parameters allow you to customize the behavior of the function based on the values passed to it."""

#How to Define a Function with Parameters
"""
Use the def Keyword: Start with the def keyword to define the function.
Specify the Function Name: Choose a name for the function.
Add Parameters in Parentheses: List the parameters inside parentheses ().
These are the variables that will receive the values when the function is called.
Provide the Function Body: Write the code that uses these parameters to perform a specific task.
End with a Colon: The function definition ends with a colon :
"""
#1
print("code 1 , addition")

def add(a, b):
    return a + b
result = add(5, 3)
print(result)
#2
print("code 2, multiplication")

def multiply(x, y):
    return x * y

result = multiply (2,6)
print(result)
#3
print("code 3 greeting")

def greet(name):
    print(f"Hello,{name}")
def ask(question):
    print(question)
    
#calling the function
    
greet("Sachin")       # Output: Hello, sachin
ask("How are you")    # Output: How are you

#2.2  What are the rules for passing arguments to a function?
"""
A function can take multiple arguments, these arguments can be objects,
variables(of same or different data types) and functions. Python
functions are first class objects. In the example below, a function is
assigned to a variable. This assignment doesn’t call the function. It takes
the function object referenced by shout and creates a second name pointing to it, yell."""

#When passing arguments to a function in Python, there are several rules and conventions to follow:


"""Positional Arguments: These are arguments passed to a function in the order they are defined.
For example:"""

def greet(name, address):
    print(f"Hello {name}, are you from {address}")

greet("sachin", "bhopal")


#2.3 How can you use parameters to make a function more flexible or reusable?

#Using parameters in functions is a powerful way to make your code more flexible and reusable.

#Customization
"""Parameters allow you to pass different values to a function, which can change its
behavior. For instance, if you have a function that calculates the area of a rectangle,
you can use parameters to specify the length and width."""

def calculate_area(length, width):
    return length * width

area1 = calculate_area(5, 10)  
area2 = calculate_area(7, 3)     

#Reusability

"""
By using parameters, you can reuse the same function
with different inputs without rewriting it. This avoids code
duplication and makes maintenance easier. """

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("RAJ"))  # Hello, raj!
print(greet("Sagar"))  # Hi,sagar!

#Flexibility
#Variable-Length Arguments.

"""
Functions can accept a variable number of arguments using *args and **kwargs,
making them adaptable to different inputs.
Arbitrary arguments in Python enable functions to accept an unlimited number
of arguments. This allows for flexibility when creating functions that require
an unknown number of arguments.Arbitrary arguments are denoted with an asterisk (*)
before the argument name . These arguments can create a list  or dictionary of the passed
arguments."""

def summarize(*args):
    return sum(args)

print(summarize(1, 2, 3, 4))  # 10

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Arav", age=20, city="Delhi")














