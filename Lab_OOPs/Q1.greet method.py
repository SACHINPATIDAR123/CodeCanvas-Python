#Question: Create a Python class named Person with attributes name and age.Implement a method
#greet that prints a greeting message including the person's name.Create an instance of the
#Person class and call the greet method.

class Person:
# Constructor method to initialize the name and age attributes
    def __init__(self, name, age):
        self.name = name  #name attribute
        self.age = age    #Set the age attribute
    
# Method of printing a greeting message
    def greet(self):
        print(f"Hello, my name is {self.name}.") 

# Create an instance of the Person class with name "Alice" and age 30
person_instance = Person(name="Sachin", age=24)

# Calling the object
person_instance.greet() 
