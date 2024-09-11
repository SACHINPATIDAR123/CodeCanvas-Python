#Question: Define a function print_area() that takes a Shape object and prints its
#area. Use this function with instances of Rectangle and Circle to demonstrate
#polymorphism

#Polymorphism
'''Polymorphism allows objects of different classes to be treated as objects of
a common base class. It enables a single function or method to operate in
different ways depending on the type of object it is called on'''

# Base class
class Shape:
    def area(self):

# This method should be overridden in derived classes

        raise NotImplementedError("Subclasses must implement this method")

# Derived class for Rectangle

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):

# Calculate and return the area of the rectangle

        return self.width * self.height

# Derived class for Circle

class Circle(Shape):
    PI = 3.14159 

    def __init__(self, radius):
        self.radius = radius

    def area(self):

# Calculate and return the area of the circle using the manually defined value of π

        return Circle.PI * (self.radius ** 2)

# Function to print the area of any Shape

def print_area(shape):
    print(f"The area is: {shape.area()}")  

# Create instances of Rectangle and Circle

rectangle = Rectangle(width=6, height=12)
circle = Circle(radius=8)


print_area(rectangle)  
print_area(circle)     

