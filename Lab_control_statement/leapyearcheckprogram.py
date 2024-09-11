year = int(input("Enter a year: ")) #feed input 

# Checking if the year is a leap year or not.
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("year is a leap year.")
        else:
            print("year is not a leap year.")
    else:
        print("year is a leap year.")
else:
    print("year is not a leap year.")
    
 #leap year:
"""A leap year is a year that includes an extra day, February 29, to keep the
calendar year synchronized with the astronomical year. Leap years occur approximately
every 4 years and have 366 days instead of the usual 365. The rules for determining a leap year are:

Divisible by 4: The year must be divisible by 4.
Not divisible by 100: If the year is divisible by 100, it is not a leap year unless:
Divisible by 400: The year must also be divisible by 400 to be a leap year."""

#non leap year:
"""A non-leap year is a year that does not have the extra day in February and consists
of the usual 365 days. A non-leap year is any year that does not meet
the criteria for a leap year."""
