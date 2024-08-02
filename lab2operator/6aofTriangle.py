# Q2. Calculate the area of triangle.

"""
The area of triangle can be calculated using formula:
     Area of Triangle = 1/2 * Base * Height
"""

# Here I used input() as int(), which means it can only take input as integer. 
# But if user wants to input float, it will give error.
base = int(input("Enter the Base of the Triangle: "))
height = int(input("Enter the Height of the Triangle: "))

areaOfTriangle = 1/2 * base * height
print("Area of Triangle is", areaOfTriangle)