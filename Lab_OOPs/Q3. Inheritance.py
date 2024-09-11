#Question: Create a base class Employee with attributes name and salary. Create
#a derived class Manager that inherits from Employee and adds an additional
#attribute department. Implement a method in the Manager class to display the
#manager's details, including name, salary, and department.

#Inheritance
'''Definition: Inheritance allows a new class to inherit the properties and
methods of an existing class. This facilitates code reusability and establishes
a hierarchical relationship between classes'''

# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Derived class
class Manager(Employee):
    def __init__(self, name, salary, department):
# Initialize attributes from the base class
        super().__init__(name, salary)
# Additional attribute for Manager

        self.department = department
# Method to display manager's details

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: Inr.{self.salary}")
        print(f"Department: {self.department}")


manager = Manager(name="Sachin Patidar", salary=90000, department="Data Analytics")

#To Display the manager's details we call the function

manager.display_details()
