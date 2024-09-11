#1. Function without Parameters

#1.1 What is a function without parameters, and when might you use one?

"""A function without parameters is a function that
does not take any input arguments,(Arguments are the
values passed inside the parenthesis of the function.
A function can have any number of arguments separated by a comma.) 
when it is called. It performs a specific task or computation based on
internal logic or state, but it does not require any external data to operate."""

#when might you use one,

"""
1. Static Tasks: When you have tasks that don’t need any external input
and always give the same result or perform the same action every time.

Example: Printing a fixed greeting message like "Hello, world!"

2. Initialization: To set up certain values or perform setup tasks that
don’t depend on any input. This is useful when you need to prepare or configure something at the start.

Example: Setting up a default configuration or initializing certain variables.

3. Fixed Operations: For operations that work with fixed data or constants
and don’t need to change based on any input. This type of function handles
tasks where the logic doesn’t change regardless of external conditions.

Example: Returning a constant value like pi or performing a fixed computation.

These functions are helpful in scenarios where the operation is consistent and
doesn’t need to adapt based on different inputs."""

#1.2 How do you define and call a function that does not take any arguments?

#Defining and Calling a Function Without Parameters

"""To define a function without parameters, you simply write
the function name followed by empty parentheses (), and then
provide the function body with the code to execute"""

def ask():
    
    print("How are, you!")
    
#output;- mention() output Hello, sachin!

#if we want to call the fucntion we simply write mention followed by parantheses and there after we can call it.

#1.3 Can a function without parameters return a value? If so, how?

"""Yes, a function without parameters can return a value. Even though it
does not accept any input arguments, it can still perform computations or
retrieve data internally and return a result.

How to Return a Value from a Function Without Parameters

Define the Function: Inside the function, use the return statement
to specify the value that should be returned.

Call the Function: When you call the function, it will execute and
return the value specified by the return statement.

Store or Use the Returned Value: You can store the returned value in a
variable or use it directly in expressions or output."""

def greet():               #defining the fucntion
    return "Hello,sachin"  #Return to value

#Calling the function and storing the returned value

result = greet()    
print(result)

#what i learnt is that
#Yes, a function without parameters can return a value.
#Use the return statement inside the function (print) to return a value.




    












    
