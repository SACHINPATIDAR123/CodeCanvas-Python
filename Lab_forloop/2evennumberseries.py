#Question.2 Print even number series by taking input from the user

# here we give the input from our end and convert it to an integer

n = int(input("enter a number:"))

# use loop through number 1 to n

for a in range (1,n+1):

# check if the number is even i.e.(divisible by 2)
    if a % 2 == 0:

#if the number is even, it will print the number from 0 to given number as even.
        print(a)
