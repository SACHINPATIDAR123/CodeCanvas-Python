#Question: Define a class Account with private attributes for account_number and
#balance. Implement methods to deposit and withdraw money, ensuring that the
#balance cannot be directly accessed or modified from outside the class.
#Demonstrate the use of these methods.

#Encapsulation:-

'''Encapsulation is the concept of bundling data and methods that operate on that
data into a single unit, usually a class. It restricts direct access to some of an object's
components, which can help prevent accidental interference and misuse.'''

class Account:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def get_balance(self):
        return self.__balance

    def get_account_number(self):
        return self.__account_number

# Creating an instance of the Account class
account = Account(account_number="9401448XXX", initial_balance=1000)

# Demonstrating depositing money
account.deposit(200)  

# Demonstrating withdrawing money
account.withdraw(500)  

# Display balance and account number
print(f"Account Number: {account.get_account_number()}")  
print(f"Balance: INR{account.get_balance()}")  
